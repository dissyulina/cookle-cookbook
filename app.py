import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# -- Home Page --
@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    popular_recipes = mongo.db.recipes.find().sort("total_likes", -1).limit(5)
    recent_recipes = mongo.db.recipes.find().sort("_id", -1).limit(5)
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("index.html", popular_recipes=popular_recipes,
                               recent_recipes=recent_recipes, user=user)
    
    else:
        return render_template("index.html", popular_recipes=popular_recipes,
                               recent_recipes=recent_recipes)


# Pagination 
"""
Pagination adapted from:
    https://github.com/rebeccatraceyt/bake-it-til-you-make-it/blob/master/app.py and
    https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
"""
PER_PAGE = 12

def paginated(recipes):
    page, per_page, offset = get_page_args(page_parameter="page",
                                           per_page_parameter="per_page")
    offset = page * PER_PAGE - PER_PAGE
    return recipes[offset: offset + PER_PAGE]

def pagination_args(recipes):
    page, per_page, offset = get_page_args(page_parameter="page",
                                           per_page_parameter="per_page")
    total = len(recipes)
    return Pagination(page=page,
                      per_page=PER_PAGE,
                      total=total,
                      css_framework="bootstrap4")


# -- Display all recipes --
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    # pagination code adapted from:
    # https://github.com/rebeccatraceyt/bake-it-til-you-make-it/blob/master/app.py
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)

    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("recipes.html", recipes=recipes_paginated, pagination=pagination, user=user)
    else:
        return render_template("recipes.html", recipes=recipes_paginated, recipes_paginated=recipes_paginated, pagination=pagination)


# -- Search Recipes --
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}).sort("total_likes", -1))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("recipes.html", recipes=recipes_paginated, pagination=pagination, user=user)
    else:
        return render_template("recipes.html", recipes=recipes_paginated, pagination=pagination)


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
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if "user" in session:
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
                "username": session["user"],
                "total_reviews": 0,
                "reviews": []
            }
            new_recipe_id = mongo.db.recipes.insert_one(submit).inserted_id
            # Adds the new recipe_id to user's cookbook (ref: https://docs.mongodb.com/manual/reference/operator/update/push/)
            # mongo.db.recipes.find_one(new_recipe_id)
            mongo.db.users.update_one({"username": session["user"]},
                                    {"$push": {"uploaded_recipes": new_recipe_id}})
            flash("Recipe Successfully Added", "success")
            return redirect(url_for("get_recipes"))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add-recipe.html", categories=categories, user=user)
    else:
        flash("You're not logged in. Please log in or sign up first.", "warning")
        return redirect(url_for("login"))


# -- Get data for a single recipe --
@app.route("/recipe/<recipe_id>")
def get_single_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    reviews = mongo.db.reviews.find().sort("_id", 1)
    # review = mongo.db.reviews.find({"_id": ObjectId(review_id)})
    if recipe["total_reviews"] > 0:
        review = mongo.db.reviews.find_one({"_id": {"$in": recipe["reviews"]}})
    
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
        
        if recipe["total_reviews"] > 0:
            return render_template("single-recipe.html", recipe=recipe,
                           user=user, saved_recipe=saved_recipe,
                           liked_recipe=liked_recipe, reviews=reviews, review=review)
        else:
            return render_template("single-recipe.html", recipe=recipe,
                           user=user, saved_recipe=saved_recipe,
                           liked_recipe=liked_recipe, reviews=reviews)

    else:
        saved_recipe = False
        liked_recipe = False
        
    return render_template("single-recipe.html", recipe=recipe, reviews=reviews)


# -- Edit a recipe --
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # If the user logged in
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if "user" in session:
        if request.method == "POST":
            mongo.db.recipes.update_one(
                {"_id": ObjectId(recipe_id)}, {
                    '$set': {
                            "category_name": request.form.get("category_name"),
                            "recipe_name": request.form.get("recipe_name"),
                            "description": request.form.get("description"),
                            "ingredients": request.form.getlist("ingredients"),
                            "directions": request.form.getlist("directions"),
                            "recipe_image": request.form.get("recipe_image"),
                            "serving": request.form.get("serving"),
                            "time": request.form.get("time"),
                            }
                    })
            flash("Recipe Successfully Edited", "success")
            return redirect(url_for("get_recipes"))

        recipe = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("edit-recipe.html", recipe=recipe, categories=categories, user=user)
    else:
        flash("You're not logged in. Please log in or sign up first.", "warning")
        return redirect(url_for("login"))


# -- Delete a recipe --
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted", "success")
    return redirect(url_for("get_recipes"))


# -- Manage Categories --
@app.route("/get_categories")
def get_categories():
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if "user" in session:
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories, user=user)


# -- Add New Category (admin only) --
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if "user" in session:
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name"),
            }
            mongo.db.categories.insert(category)
            flash("New Category Successfully Added", "success")
            return redirect(url_for("get_categories"))
    
        return render_template("add-category.html", user=user)


# -- Edit Category (admin only) --
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if "user" in session:
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name"),
            }
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("Category Successfully Edited", "success")
            return redirect(url_for("get_categories"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("edit-category.html", category=category, user=user)


# -- Delete Category (admin only) --
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted", "success")
    return redirect(url_for("get_categories"))


# -- Save Recipe to Cookbook --
@app.route("/save_to_cookbook/<recipe_id>", methods=["GET", "POST"])
def save_to_cookbook(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    if "user" in session:
        if session["user"] != recipe["username"]:
            user = mongo.db.users.find_one(
                {"username": session["user"]})

            saved_recipes = user["saved_recipes"]

            # Checks if recipe is already in cookbook
            if ObjectId(recipe_id) not in saved_recipes:
                # Adds recipe_id to user's cookbook
                mongo.db.users.update_one({"username": session["user"]},
                                        {"$push": {"saved_recipes": ObjectId(recipe_id)}})
                flash("Recipe Added to My Cookbook", "success")
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
            flash("You created this recipe. You can't remove this from your cookbook", "info")
            return redirect(url_for("get_single_recipe",
                                    recipe_id=recipe_id))

    else:
        flash("You're not logged in. Please log in or sign up first.", "warning")

    return redirect(url_for("get_single_recipe", recipe_id=recipe_id))


# -- Like a recipe  --
@app.route("/like_recipe/<recipe_id>")
def like_recipe(recipe_id):
    if "user" in session:
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
    else:
        flash("You're not logged in. Please log in or sign up first.", "warning")
    
    return redirect(url_for("get_single_recipe",
                            recipe_id=recipe_id))


# -- My Cookbook Page --
@app.route("/cookbook/<username>")
def get_cookbook(username):
    if session["user"] == username:
        # user variable to grab user's data
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        uploaded_recipes = list(mongo.db.recipes.find(
            {"_id": {"$in": user["uploaded_recipes"]}}))
        saved_recipes = list(mongo.db.recipes.find(
            {"_id": {"$in": user["saved_recipes"]}}))
        
        # to find from 2 lists, ref: https://stackoverflow.com/questions/47075081/concatenate-pymongo-cursor
        all_recipes = list(mongo.db.recipes.find(
            {'$or': [{"_id": {"$in": user["uploaded_recipes"]}},
                     {"_id": {"$in": user["saved_recipes"]}}]}))

        # pagination
        all_recipes_paginated = paginated(all_recipes)
        all_pagination = pagination_args(all_recipes) 
        uploaded_recipes_paginated = paginated(uploaded_recipes)
        uploaded_pagination = pagination_args(uploaded_recipes)
        saved_recipes_paginated = paginated(saved_recipes)
        saved_pagination = pagination_args(saved_recipes)
        
        return render_template("cookbook.html", user=user,
                               all_recipes=all_recipes_paginated,
                               all_pagination=all_pagination,
                               uploaded_recipes=uploaded_recipes_paginated,
                               uploaded_pagination=uploaded_pagination,
                               saved_recipes=saved_recipes_paginated,
                               saved_pagination=saved_pagination)

    return redirect(url_for("login"))


# -- Write a review --
@app.route("/write_review/<recipe_id>", methods=["GET", "POST"])
def write_review(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    username = user["username"]
    user_image = user["user_image"]
    
    if "user" in session:
        if request.method == "POST":
            submit = {
                "review_text": request.form.get("write_review"),
                "username": username,
                "user_image": user_image,
                "recipe_id": ObjectId(recipe_id)
            }
            new_review_id = mongo.db.reviews.insert_one(submit).inserted_id

            mongo.db.recipes.update_one(
                {"_id": ObjectId(recipe_id)}, {
                    "$push": {"reviews": new_review_id},
                    "$inc": {"total_reviews": 1}
                }
            )
                                
            flash("Review Successfully Added", "success")
            return redirect(url_for("get_single_recipe", recipe=recipe, user=user, recipe_id=recipe_id))
        
        return render_template("single-recipe.html", recipe=recipe, user=user)


# -- Edit a review (only available for the user's own review) --
@app.route("/edit_review/<review_id>/", methods=["GET", "POST"])
def edit_review(review_id):
    # recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    review = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})
    recipe_id = review["recipe_id"]
    if "user" in session:
        if request.method == "POST":
            submit = {
                "review_text": request.form.get("edit_review")
            }
            mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": submit})
            flash("Review Successfully Edited", "success")
            return redirect(url_for("get_single_recipe", recipe_id=recipe_id))

        return render_template("single-recipe.html", review=review, user=user)


# -- Delete a comment (only available for the user's own review) --
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    review = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})
    recipe_id = review["recipe_id"]
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {
                                "$pull": {"reviews": ObjectId(review_id)},
                                "$inc": {"total_reviews": -1}})

    flash("Review Successfully Deleted", "success")
    return redirect(url_for("get_single_recipe", recipe_id=recipe_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
