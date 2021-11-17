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
    """
    Function to get the popular recipes and recent recipes for carousels
    """
    popular_recipes = mongo.db.recipes.find().sort("total_likes", -1).limit(8)
    recent_recipes = mongo.db.recipes.find().sort("_id", -1).limit(8)

    # If user logged in, get data for profile picture
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("index.html", popular_recipes=popular_recipes,
                               recent_recipes=recent_recipes, user=user)

    else:
        return render_template("index.html", popular_recipes=popular_recipes,
                               recent_recipes=recent_recipes)


# -- Pagination --
"""
Pagination adapted from:
https://github.com/rebeccatraceyt/bake-it-til-you-make-it/blob/master/app.py
https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
"""
PER_PAGE = 12


def paginated(recipes):
    """
    Function for pagination
    """
    page, per_page, offset = get_page_args(page_parameter="page",
                                           per_page_parameter="per_page")
    offset = page * PER_PAGE - PER_PAGE
    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    """
    Function for pagination
    """
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
    """
    Function to display all recipes cards
    Sorted alphabetically by recipe name
    """
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    categories = mongo.db.categories.find().sort("category_name", 1)
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)

    # Get saved recipes data if user logged in
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        saved_recipes = user["saved_recipes"]
        return render_template("recipes.html",
                               categories=categories,
                               recipes=recipes_paginated,
                               pagination=pagination,
                               user=user,
                               saved_recipes=saved_recipes)
    else:
        return render_template("recipes.html",
                               categories=categories,
                               recipes=recipes_paginated,
                               pagination=pagination)


# -- Search Recipes --
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Function to search recipes and display the result
    Results are sorted by number of likes (descending)
    """
    query = request.form.get("query")
    categories = mongo.db.categories.find().sort("category_name", 1)
    recipes = list(mongo.db.recipes.find(
        {"$text": {"$search": query}}).sort(
            "total_likes", -1))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)

    # Get saved recipes data if user logged in
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        saved_recipes = user["saved_recipes"]
        return render_template("recipes.html",
                               categories=categories,
                               recipes=recipes_paginated,
                               pagination=pagination,
                               user=user,
                               saved_recipes=saved_recipes)
    else:
        return render_template("recipes.html",
                               categories=categories,
                               recipes=recipes_paginated,
                               pagination=pagination)


# -- Filter Recipes --
@app.route("/filter_recipes", methods=["GET", "POST"])
def filter_recipes():
    """
    Function to filter the recipes by their category
    Results are sorted by number of likes (descending)
    """
    category_name = request.form.get("category")
    categories = mongo.db.categories.find().sort("category_name", 1)
    recipes = list(mongo.db.recipes.find(
                   {"category_name": category_name}).sort(
                    "total_likes", -1))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)

    # get saved recipes data if user logged in
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        saved_recipes = user["saved_recipes"]
        return render_template("recipes.html",
                               categories=categories,
                               recipes=recipes_paginated,
                               pagination=pagination,
                               user=user,
                               saved_recipes=saved_recipes)
    else:
        return render_template("recipes.html",
                               categories=categories,
                               recipes=recipes_paginated,
                               pagination=pagination)


# -- User register/ sign up --
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function for user registration / signing up
    """
    if "user" in session:
        # remove user from session cookie
        flash("You have been logged out", "info")
        session.pop("user")
        return render_template("register.html")
    else:
        if request.method == "POST":
            # check if username already exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists", "warning")
                return redirect(url_for("register"))

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
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
    """
    Function for user login to the site
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
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
    """
    Function for user to view their profile page
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is the correct user
    """
    if "user" in session:
        # Check if user is correct
        if session["user"] == username:
            # user variable to grab user's data
            user = mongo.db.users.find_one(
                {"username": session["user"]})
            uploaded_recipes = mongo.db.recipes.find(
                {"_id": {"$in": user["uploaded_recipes"]}})
            saved_recipes = mongo.db.recipes.find(
                {"_id": {"$in": user["saved_recipes"]}})

            return render_template("profile.html",
                                   user=user,
                                   saved_recipes=saved_recipes,
                                   uploaded_recipes=uploaded_recipes)
        else:
            # if wrong user
            flash("You are not authorized to view that page", "danger")
            return redirect(url_for("profile",
                                    username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Edit profile page --
@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    """
    Function for user to edit their profile
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is the correct user
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"_id": ObjectId(user_id)})
        username = user["username"]

        # Check if user is correct
        if session["user"] == username:
            if request.method == "POST":
                submit = {
                    "username": request.form.get("username").lower(),
                    "email": request.form.get("email"),
                    "about": request.form.get("about"),
                    "user_image": request.form.get("profile-url"),
                }
                mongo.db.users.update({"_id": ObjectId(user_id)},
                                      {"$set": submit})

                # update username and user image in recipes and reviews coll
                update = {
                    "username": request.form.get("username").lower(),
                    "user_image": request.form.get("profile-url"),
                }
                mongo.db.recipes.update({"user_id": ObjectId(user_id)},
                                        {"$set": update})
                mongo.db.reviews.update({"user_id": ObjectId(user_id)},
                                        {"$set": update})

                flash("Profile Successfully Edited", "success")
                return redirect(url_for("profile", username=session["user"]))
            return render_template("edit-profile.html", user=user)
        else:
            # if wrong user
            flash("You are not authorized to view that page", "danger")
            return redirect(url_for("profile",
                                    username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Change Password page --
@app.route("/change_password/<user_id>", methods=["GET", "POST"])
def change_password(user_id):
    """
    Function for user to change their password
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is the correct user
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"_id": ObjectId(user_id)})
        username = user["username"]

        # Check if user is correct
        if session["user"] == username:
            if request.method == "POST":
                submit = {
                    "password": generate_password_hash(
                        request.form.get("password")),
                }
                mongo.db.users.update({"_id": ObjectId(user_id)},
                                      {"$set": submit})
                flash("Password Successfully Changed", "success")
                return redirect(url_for("profile", username=session["user"]))

            user = mongo.db.users.find_one(
                {"_id": ObjectId(user_id)})
            return render_template("change-password.html", user=user)
        else:
            # if wrong user
            flash("You are not authorized to view that page", "danger")
            return redirect(url_for("profile",
                                    username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Delete my profile --
@app.route("/delete_profile/<user_id>")
def delete_profile(user_id):
    """
    Function for user to delete their account
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is the correct user
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"_id": ObjectId(user_id)})
        username = user["username"]

        # Check if user is correct
        if session["user"] == username:
            mongo.db.users.remove(
                {"username": username.lower()})
            flash("Profile Deleted", "info")
            session.pop("user")
            return redirect(url_for("register"))

        else:
            # if wrong user
            flash("You are not authorized to view that page.", "danger")
            return redirect(url_for("profile",
                                    username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- User log out --
@app.route("/logout")
def logout():
    """
    Function for user to log out
    """
    # remove user from session cookie
    flash("You have been logged out", "info")
    session.pop("user")
    return redirect(url_for("login"))


# -- Add/create a recipe --
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Function to add a recipe
    Add some conditional defensive code to check
        if the user is logged in
    Also add the new recipe_id to user's cookbook
    """
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
                "user_image": user["user_image"],
                "total_reviews": 0,
                "reviews": []
            }
            new_recipe_id = mongo.db.recipes.insert_one(submit).inserted_id
            mongo.db.users.update_one({"username": session["user"]},
                                      {"$push": {
                                          "uploaded_recipes": new_recipe_id}})
            flash("Recipe Successfully Added", "success")
            return redirect(url_for("get_single_recipe",
                                    recipe_id=new_recipe_id))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add-recipe.html",
                               categories=categories,
                               user=user)
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Get data for a single recipe --
@app.route("/recipe/<recipe_id>")
def get_single_recipe(recipe_id):
    """
    Function for individual recipe page
    Display the recipe's data and all reviews for the recipe
    """
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    reviews = mongo.db.reviews.find().sort("_id", -1)
    if recipe["total_reviews"] > 0:
        review = mongo.db.reviews.find_one({"_id": {"$in": recipe["reviews"]}})

    # If the user logged in, get data for saved recipe and likes
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        saved_recipes = user["saved_recipes"]
        liked_recipes = user["liked_recipes"]
        # If the recipe has been added to user's cookbook
        if ObjectId(recipe_id) in saved_recipes:
            saved_recipe = True
        else:
            saved_recipe = False
        # If the recipe has been liked by the user
        if ObjectId(recipe_id) in liked_recipes:
            liked_recipe = True
        else:
            liked_recipe = False

        if recipe["total_reviews"] > 0:
            return render_template("single-recipe.html",
                                   recipe=recipe,
                                   user=user,
                                   saved_recipe=saved_recipe,
                                   liked_recipe=liked_recipe,
                                   reviews=reviews,
                                   review=review)
        else:
            return render_template("single-recipe.html",
                                   recipe=recipe,
                                   user=user,
                                   saved_recipe=saved_recipe,
                                   liked_recipe=liked_recipe,
                                   reviews=reviews)
    else:
        saved_recipe = False
        liked_recipe = False

    return render_template("single-recipe.html",
                           recipe=recipe,
                           reviews=reviews)


# -- Edit a recipe --
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Function for user to edit their own recipe
    This function is also accessible by the Admin
        (to edit some mistakes to keep the db clean)
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is the correct user or admin
    """
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    recipe = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})
    username = recipe["username"]
    if "user" in session:
        # If the user logged in
        if session["user"] == username or session["user"] == "admin":
            # If correct user
            category = mongo.db.categories.find_one(
                {"category_name": request.form.get("category_name")})
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
                    "category_id": category["_id"],
                }
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)},
                                        {"$set": submit})
                flash("Recipe Successfully Edited", "success")
                return redirect(url_for("get_single_recipe",
                                        recipe_id=recipe_id))

            categories = mongo.db.categories.find().sort("category_name", 1)
            return render_template("edit-recipe.html",
                                   recipe=recipe,
                                   categories=categories,
                                   user=user)

        else:
            # If wrong user
            flash("You are not authorized to do that.", "danger")
            return redirect(url_for("get_single_recipe", recipe_id=recipe_id))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Delete a recipe --
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Function for user to delete their own recipe
    This function is also accessible by the Admin
        (to edit spam/unfit posts to keep the db clean)
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is the correct user or admin
    """
    recipe = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})
    username = recipe["username"]
    if session["user"] == username or session["user"] == "admin":
        # If correct user
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe Successfully Deleted", "success")
        return redirect(url_for("get_recipes"))
    else:
        # If wrong user
        flash("You are not authorized to do that.", "danger")
        return redirect(url_for("get_single_recipe", recipe_id=recipe_id))


# -- Manage Categories (Admin only)--
@app.route("/get_categories")
def get_categories():
    """
    Function for admin to view all categories
    Only accessible by Admin
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is admin
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        if user["is_admin"]:
            categories = list(mongo.db.categories.find().sort(
                              "category_name", 1))
            return render_template("categories.html",
                                   categories=categories,
                                   user=user)
        else:
            # if user is not admin
            flash("You are not authorized to do view this page.", "danger")
            return redirect(url_for("profile",
                                    username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Add New Category (Admin only) --
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Function for admin to add a new categories
    Only accessible by Admin
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is admin
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        if user["is_admin"]:
            if request.method == "POST":
                category = {
                    "category_name": request.form.get("category_name"),
                }
                mongo.db.categories.insert(category)
                flash("New Category Successfully Added", "success")
                return redirect(url_for("get_categories"))

            return render_template("add-category.html", user=user)
        else:
            # If user is not admin
            flash("You are not authorized to do view this page.", "danger")
            return redirect(url_for("profile",
                            username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Edit Category (Admin only) --
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Function for admin to edit categories
    Only accessible by Admin
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is admin
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        if user["is_admin"]:
            if request.method == "POST":
                submit = {
                    "category_name": request.form.get("category_name"),
                }
                mongo.db.categories.update(
                    {"_id": ObjectId(category_id)}, submit)
                # update recipes in recipes coll with the new category name
                mongo.db.recipes.update_many(
                    {"category_id": ObjectId(category_id)}, {"$set": submit})
                flash("Category Successfully Edited", "success")
                return redirect(url_for("get_categories"))

            category = mongo.db.categories.find_one(
                {"_id": ObjectId(category_id)})
            return render_template("edit-category.html",
                                   category=category,
                                   user=user)
        else:
            # If user is not admin
            flash("You are not authorized to do view this page.", "danger")
            return redirect(url_for("profile",
                            username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Delete Category (admin only) --
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Function for admin to delete categories
    Only accessible by Admin
    Add some conditional defensive code to check:
    - if the user is logged in
    - if the logged in user is admin
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        # Check if user is admin
        if user["is_admin"]:
            mongo.db.categories.remove({"_id": ObjectId(category_id)})
            flash("Category Successfully Deleted", "success")
            return redirect(url_for("get_categories"))
        else:
            # If user is not admin
            flash("You are not authorized to do view this page.", "danger")
            return redirect(url_for("profile",
                            username=session["user"]))
    else:
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Save Recipe to Cookbook --
@app.route("/save_to_cookbook/<recipe_id>", methods=["GET", "POST"])
def save_to_cookbook(recipe_id):
    """
    Function for users to save recipe to their cookbook,
    Also to remove from their cookbook if it's already in the cookbook
        (added a confirmation modal on front-end before removing)
    Add conditional defensive code to check
        if the user is logged in
    """
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
                                          {"$push": {
                                            "saved_recipes": ObjectId(
                                                  recipe_id)}})
                flash("Recipe Added to My Cookbook", "success")
                return redirect(request.referrer)

            else:
                # If recipe is already in cookbook, remove it from the cookbook
                mongo.db.users.update_one({"username": session["user"]},
                                          {"$pull": {
                                            "saved_recipes": ObjectId(
                                                  recipe_id)}})
                flash("Recipe Removed from My Cookbook", "info")
                return redirect(request.referrer)

        else:
            # if user created the recipe, they cannot save it
            flash("You created this recipe. It's in your cookbook.",
                  "info")
            return redirect(request.referrer)

    else:
        flash("Please log in or sign up.", "warning")

    return redirect(url_for("get_single_recipe", recipe_id=recipe_id))


# -- Like a recipe  --
@app.route("/like_recipe/<recipe_id>")
def like_recipe(recipe_id):
    """
    Function for users to like a recipe
    Also to unlike a recipe if it's already liked
    Add conditional defensive code to check
        if the user is logged in
    """
    if "user" in session:
        user = mongo.db.users.find_one(
                {"username": session["user"]})
        liked_recipes = user["liked_recipes"]

        # Checks if recipe is already liked by the user
        if ObjectId(recipe_id) not in liked_recipes:
            # Like this recipe
            mongo.db.users.update_one({"username": session["user"]},
                                      {"$push": {
                                          "liked_recipes": ObjectId(
                                              recipe_id)
                                      }})
            mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                        {"$inc": {"total_likes": 1}})
            return redirect(url_for("get_single_recipe",
                                    recipe_id=recipe_id))
        else:
            # If the user already liked this recipe, unlike the recipe
            mongo.db.users.update_one({"username": session["user"]},
                                      {"$pull": {
                                          "liked_recipes": ObjectId(
                                              recipe_id)
                                      }})
            mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                        {"$inc": {"total_likes": -1}})
            return redirect(url_for("get_single_recipe",
                                    recipe_id=recipe_id))
    else:
        flash("Please log in or sign up.", "warning")

    return redirect(url_for("get_single_recipe",
                            recipe_id=recipe_id))


# -- My Cookbook Page --
@app.route("/cookbook/<username>")
def get_cookbook(username):
    """
    Function for users to view their cookbook page
    Separated in three tabs:
        uploaded recipes, saved recipes, all (uploaded + saved)
    Add conditional defensive code to check:
        - if the user is logged in
        - if the user is correct
    """
    if "user" in session:
        if session["user"] == username:
            # user variable to grab user's data
            user = mongo.db.users.find_one(
                {"username": session["user"]})
            uploaded_recipes = list(mongo.db.recipes.find(
                {"_id": {"$in": user["uploaded_recipes"]}}
                ).sort("recipe_name", 1))
            saved_recipes = list(mongo.db.recipes.find(
                {"_id": {"$in": user["saved_recipes"]}}
                ).sort("recipe_name", 1))
            all_recipes = list(mongo.db.recipes.find(
                {'$or': [{"_id": {"$in": user["uploaded_recipes"]}},
                         {"_id": {"$in": user["saved_recipes"]}}]}
                         ).sort("recipe_name", 1))

            # pagination
            all_recipes_paginated = paginated(all_recipes)
            all_pagination = pagination_args(all_recipes)
            uploaded_recipes_paginated = paginated(uploaded_recipes)
            uploaded_pagination = pagination_args(uploaded_recipes)
            saved_recipes_paginated = paginated(saved_recipes)
            saved_pagination = pagination_args(saved_recipes)

            return render_template("cookbook.html",
                                   user=user,
                                   all_recipes=all_recipes_paginated,
                                   all_pagination=all_pagination,
                                   uploaded_recipes=uploaded_recipes_paginated,
                                   uploaded_pagination=uploaded_pagination,
                                   saved_recipes=saved_recipes_paginated,
                                   saved_pagination=saved_pagination)
        else:
            # if wrong user
            flash("You are not authorized to view that page", "danger")
            return redirect(url_for("profile",
                                    username=session["user"]))

    else:
        # If not logged in
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Write a review --
@app.route("/write_review/<recipe_id>", methods=["GET", "POST"])
def write_review(recipe_id):
    """
    Function for users to write a review
    Add conditional defensive code to check
        if the user is logged in
    """
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    if "user" in session:
        # If user logged in
        if request.method == "POST":
            user = mongo.db.users.find_one(
                {"username": session["user"]})
            username = user["username"]
            user_image = user["user_image"]
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
            return redirect(url_for("get_single_recipe",
                                    recipe=recipe,
                                    user=user,
                                    recipe_id=recipe_id))

        return render_template("single-recipe.html", recipe=recipe, user=user)

    else:
        # If not logged in
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Edit a review (only available for the user's own review) --
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Function for users to edit their review
    Add conditional defensive code to check
        - if the user is logged in
        - if the user is correct
    """
    review = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})
    recipe_id = review["recipe_id"]

    if "user" in session:
        # If the user logged in
        username = review["username"]
        if session["user"] == username:
            # If correct user
            if request.method == "POST":
                submit = {
                    "review_text": request.form.get("edit_review"),
                }
                mongo.db.reviews.update_one(
                    {"_id": ObjectId(review_id)}, {"$set": submit})
                flash("Review Successfully Edited", "success")

                return redirect(url_for("get_single_recipe",
                                        recipe_id=recipe_id))

            return redirect(request.referrer)

        else:
            # If wrong user
            flash("You are not authorized to do that.", "danger")
            return redirect(url_for("get_single_recipe", recipe_id=recipe_id))

    else:
        # If not logged in
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


# -- Delete a review --
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    Function for users to delete their review
    This functionality is also accessible by Admin
        (to delete spam/ malicious comments if needed)
    Add conditional defensive code to check
        - if the user is logged in
        - if the user is correct or is admin
    """
    review = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})
    recipe_id = review["recipe_id"]

    if "user" in session:
        # If the user logged in
        username = review["username"]
        if session["user"] == username or session["user"] == "admin":
            # If correct user
            mongo.db.reviews.remove({"_id": ObjectId(review_id)})
            mongo.db.recipes.update_one(
                {"_id": ObjectId(recipe_id)},
                {"$pull": {"reviews": ObjectId(review_id)},
                 "$inc": {"total_reviews": -1}})

            flash("Review Successfully Deleted", "success")
            return redirect(url_for("get_single_recipe", recipe_id=recipe_id))

        else:
            # If wrong user
            flash("You are not authorized to do that.", "danger")
            return redirect(url_for("get_single_recipe", recipe_id=recipe_id))

    else:
        # If not logged in
        flash("Please log in or sign up.", "warning")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
