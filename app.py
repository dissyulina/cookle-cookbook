import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# -- Display all recipes --
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# -- User register/ sign up --
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "warning")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "name": request.form.get("name").lower(),
            "email": request.form.get("email"),
            "about": request.form.get("about"),
            "user_image": request.form.get("profile-url"),
            "saved_recipes": [],
            "uploaded_recipes": [],
            "liked_recipes": [],
            "is_admin": False
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!", "success")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# -- User log in --
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    # flash("Welcome, {}".format(request.form.get("username"),"success"))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "warning")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "warning")
            return redirect(url_for("login"))

    return render_template("login.html")


# -- User's profile page --
@app.route("/profile/<username>")
def profile(username):
    if session["user"] == username:
        # user variable to grab user's data
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        uploaded_recipes = mongo.db.recipes.find(
            {"_id": {"$in": user["uploaded_recipes"]}})
        saved_recipes = mongo.db.recipes.find(
            {"_id": {"$in": user["saved_recipes"]}})

        return render_template("profile.html", user=user,
                               saved_recipes=saved_recipes,
                               uploaded_recipes=uploaded_recipes)

    return redirect(url_for("login"))


# -- Edit profile page --
@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if request.method == "POST":
        submit = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "about": request.form.get("about"),
            "user_image": request.form.get("profile-url"),
        }
        mongo.db.users.update({"_id": ObjectId(user_id)}, {"$set": submit})
        flash("Profile Successfully Edited", "success")
        return redirect(url_for("profile", username=session["user"]))

    user = mongo.db.users.find_one(
        {"_id": ObjectId(user_id)})
    return render_template("edit-profile.html", user=user)


# -- User log out --
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# -- Add/create a recipe --
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "directions": request.form.getlist("directions"),
            "recipe_image": request.form.get("recipe_image"),
            "serving": request.form.get("serving"),
            "time": request.form.get("time"),
            "total_likes": 0,
            "username": session["user"]
        }
        new_recipe_id = mongo.db.recipes.insert_one(submit).inserted_id
        # Adds the new recipe_id to user's cookbook (ref: https://docs.mongodb.com/manual/reference/operator/update/push/)
        mongo.db.recipes.find_one(new_recipe_id)
        mongo.db.users.update_one({"username": session["user"]},
                                 {"$push": {"uploaded_recipes": new_recipe_id}})
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add-recipe.html", categories=categories)


# -- Get data for a single recipe --
@app.route("/recipe/<recipe_id>")
def get_single_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    
    # If the user logged in
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        saved_recipes = user["saved_recipes"]
        liked_recipes = user["liked_recipes"]
        # If the recipe is listed in user's cookbook
        if ObjectId(recipe_id) in saved_recipes:
            saved_recipe = True
        else:
            saved_recipe = False
        # If the recipe is liked by the user
        if ObjectId(recipe_id) in liked_recipes:
            liked_recipe = True
        else:
            liked_recipe = False
        
        return render_template("single-recipe.html", recipe=recipe,
                           user=user, saved_recipe=saved_recipe,
                           liked_recipe=liked_recipe)

    else:
        saved_recipe = False
        liked_recipe = False
        
    return render_template("single-recipe.html", recipe=recipe)


# -- Edit a recipe --
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "directions": request.form.getlist("directions"),
            "recipe_image": request.form.get("recipe_image"),
            "serving": request.form.get("serving"),
            "time": request.form.get("time"),
            "total_likes": 0,
            "username": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Edited", "success")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit-recipe.html", recipe=recipe, categories=categories)


# -- Delete a recipe --
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted", "success")
    return redirect(url_for("get_recipes"))


# -- Manage Categories --
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# -- Add New Category (admin only) --
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
        }
        mongo.db.categories.insert(category)
        flash("New Category Successfully Added", "success")
        return redirect(url_for("get_categories"))
  
    return render_template("add-category.html")


# -- Edit Category (admin only) --
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Edited", "success")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit-category.html", category=category)


# -- Delete Category (admin only) --
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted", "success")
    return redirect(url_for("get_categories"))


# -- Save Recipe to Cookbook --
@app.route("/save_to_cookbook/<recipe_id>", methods=["GET", "POST"])
def save_to_cookbook(recipe_id):
    """
    Adds recipe to the current users' cookbook
    Favouriting functionality inspired by:
    https://github.com/johnnycistudent/recipe-app/blob/master/app.py
    """
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})

    if session["user"] != recipe["username"]:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        saved_recipes = user["saved_recipes"]

        # Checks if recipe is already in cookbook
        if ObjectId(recipe_id) not in saved_recipes:
            # Adds recipe_id to user's cookbook
            mongo.db.users.update_one({"username": session["user"]},
                                      {"$push": {"saved_recipes": ObjectId(recipe_id)}})
            flash("Recipe added to My Cookbook", "success")
            return redirect(url_for("get_single_recipe",
                                recipe_id=recipe_id))

        else:
            # If recipe is already in cookbook, remove it from the cookbook
            mongo.db.users.update_one({"username": session["user"]},
                                      {"$pull": {"saved_recipes": ObjectId(recipe_id)}})
            flash("Recipe Removed from My Cookbook", "info")
            return redirect(url_for("get_single_recipe",
                                recipe_id=recipe_id))

    else:
        # if user created the recipe, they cannot save it
        flash("This recipe is created by you!")
        return redirect(url_for("get_single_recipe",
                                recipe_id=recipe_id))


# -- Like a recipe  --
@app.route("/like_recipe/<recipe_id>")
def like_recipe(recipe_id):
    user = mongo.db.users.find_one(
            {"username": session["user"]})
    liked_recipes = user["liked_recipes"]

    # Checks if recipe is already liked by the user
    if ObjectId(recipe_id) not in liked_recipes:
        # Like this recipe
        mongo.db.users.update_one({"username": session["user"]},
                                  {"$push": {"liked_recipes":
                                             ObjectId(recipe_id)}})
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                    {"$inc": {"total_likes": 1}})
        return redirect(url_for("get_single_recipe",
                                recipe_id=recipe_id))
    else:
        # If the user already liked this recipe, unlike the recipe
        mongo.db.users.update_one({"username": session["user"]},
                                  {"$pull": {"liked_recipes":
                                             ObjectId(recipe_id)}})
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                    {"$inc": {"total_likes": -1}})
        return redirect(url_for("get_single_recipe",
                                recipe_id=recipe_id))


# -- My Cookbook Page --
@app.route("/cookbook/<username>")
def get_cookbook(username):
    if session["user"] == username:
        # user variable to grab user's data
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        uploaded_recipes = mongo.db.recipes.find(
            {"_id": {"$in": user["uploaded_recipes"]}})
        saved_recipes = mongo.db.recipes.find(
            {"_id": {"$in": user["saved_recipes"]}})

        all_recipes = list(uploaded_recipes) + list(saved_recipes)
        return render_template("cookbook.html", user=user,
                               all_recipes=all_recipes,
                               saved_recipes=saved_recipes,
                               uploaded_recipes=uploaded_recipes)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
