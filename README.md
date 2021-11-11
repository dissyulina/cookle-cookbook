# **Cookle**

![Cookle website in various devices](static/images/readme/am-i-responsive.jpg "Cookle website in various devices")  

Cookle is a recipe sharing web application that allows user to easily create and save their recipes online, as well as search for recipes and conveniently save them to the cookbook. Inspired by online recipe sharing platform such as Allrecipes and Cookpad, Cookle was designed as a modern and fun web-application with a great UI/UX in mind, and 
 
Please note that this web application was created for the Code Institute’s Milestone Project 3 as part of their Diploma in Full Stack Software Development. The requirements are to build a web application using HTML, CSS, JavaScript, Python+Flask, MongoDB, and other additional libraries as needed. The site should allow user to perform basic CRUD functionality (Create, Read, Update, and Delete), thus make use of this site and engage with the community.

[View live website here](https://cookle-cookbook.herokuapp.com/)

<br/>   

## **Table of Contents**   


## **UX Development Plane**   
<br/>    

### **1. Strategy Plane**    
#### **User Stories**   
As a new/ unregistered user, I want to:
1. Be able to search a recipe easily
2. See the popular recipes of the site
3. Explore all recipes that listed in the site
4. Be able to view a full recipe that I'm interested in
5. Navigate intuitively and can spot the Sign Up button right away
6. Understand what the site is about and how it works

As a returning/ registered user, I want to:
1. Immediately be able to spot the Log In button
2. See the newest added recipes on the site
3. Once logged in, easily navigate  to my account settings, my cookbook, and other pages available to me.
4. Be able to Edit or Delete my profile
5. Be able to Create a recipe and share it to the site, and to Edit or Delete it afterwards as needed
6. Be able to Save a recipe that I like to my cookbook, and to remove it from my cookbook as needed.
7. Be able to give a like to a recipe, and also unlike it as needed.
8. Be able to write a review on a recipe page, and to edit or delete my review
9. Be able to share a recipe on social media easily
10. Be able to print a recipe easily
11. Find a contact page for my inquiries

As an Administrative Account holder, I want to:
1. Be able to do all the functionalities as a registered user can
2. Add, Edit, or Delete a category of recipes
3. Be able to edit any recipes listed on the site as needed.
4. Be able to delete any recipes listed on the site as needed.
5. Be able to delete offensive reviews on the site as needed.
6. Be able to delete/remove a user as needed.  
<br/>   

#### **Online Research**   
As a part of the planning process, online research was done to gain some inspiration on UI and UX of a recipe sharing website, including:
1. [Allrecipes](https://www.allrecipes.com/)   
2. [Cookpad](https://cookpad.com/uk?via=jp)   
3. Similar recipe sharing site created by Code Institute peers (searched in channel peer-code-review on Slack)   
<br/>   

#### **Project Goals**  
The primary goal of **Cookle** is to provide a recipe sharing web application, that is visually appealing in design and intuitive for a first time user, that allows user perform basic functionality to create and save their recipes (also edit and delete their recipes), search recipes, save their favorite recipes to the cookbook and conveniently access them in the future. Additional functionalities include: to like a recipe, write a review on a recipe (also edit or delete their review), print a recipe, and share to social media.  
<br/>   

#### **User Goals**   
The user is looking for:
1. A recipe sharing website that is simple, easy to use, with fun and modern interface.
2. A recipe sharing website where the user can share their recipes online to the community. 
3. A recipe sharing website where the user can benefit something too, they can save recipes they like to their online cookbook.

The target user for this game is:
-  All ages
-  People that interested in cooking or baking
-  People that enjoy the convenience of using technology and social media 
-  People that don't mind to share their own recipes online

<br/>   

#### **Site Owner Goals**  
The site owner is looking to:  
1. Providing this a platform for online recipe sharing with complete functionality, and potentially being a regular user themselves. 
2. Might also benefit from the collection of the data as a whole.   
3. Still having a control to add tags or categories to the data, to remove data that aren't suitable for the site's purpose or rules.
<br/>   

#### **Strategy Table**  
Based on the user stories and goals above, the developer brainstormed all of the opportunities that could be implemented in the site. All of these opportunities were mapped based on their importance (driven by goals and user needs), and viability (given limited time and resources), to determine which opportunities were going to be included and which were not.   


The chart below is the mapping of all of the opportunities. The yellow circle signifies which opportunities/ features have the highest combination of importance and viability.   
![The mapping of the opportunities](assets/readme/opportunities-mapping.png "The mapping of the opportunities")

<br />  

### **2. Scope Plane**  
Based on the mapping in the Strategy Plane, a scope was defined for the site with room for future improvements.
* **Functional Requirements**   
   The users will be able to:
   - Sign up and log in to the site by providing username and password.
   - View and Edit their profile (option to change username, email address, and/or user image).
   - Delete their account
   - Upload a recipe 
   - Edit their own recipe
   - Delete their own recipe
   - View all recipes on the site
   - Search for recipes
   - Save favorite recipes to cookbook
   - Remove a previously saved recipes from cookbook
   - View the cookbook that is filled with their own recipes and their saved favorite recipes
   - Like a recipe
   - Remove a like 
   - Write a review on a recipe
   - Edit their own review
   - Delete their own review 
   - Print a recipe page
   - Share a recipe page   

   The admin/ site owners will be able to:
   - Have all functionalities as a user does
   - Add a category of recipes
   - Edit a category
   - Delete a category
   - Delete any recipes listed on the site (if needed)
   - Delete any offensive reviews on the site (if needed)
   - Delete any user (if needed)  
<br/>     

* **Non functional requirements**  
   - The users will be able to invite friends to join the site by providing the email address. As the site is a community based recipe sharing, the number of members are very important to hopefully add more data (in this instance, recipes) to the site.   
   - The users will be able to navigate easily and intuitively throughout the site, able to log in and log out at every page the users currently at.   
<br/>   

* **Content requirements**   
   - An individual recipe page that includes: recipe name, description, serving size, time, category, ingredients, and direction. It also features reviews and number of likes as an additional information on how good the recipe is.
   - The home page features:
     - 8 popular recipes, which are the recipes that received the most likes.
     - 8 newest uploaded recipes
     - Product (cookbooks) recommendation, so that the site's owners could conceivably earn money from people looking to buy the book.
   - The online cookbook features all recipes that had been saved to cookbook by users, and users' uploaded recipes as well.   

<br/>   

### **3. Structure Plane**    
The website was organized in a Hierarchical Tree Structure that ensures the user can navigate easily and intuitively. Below is the website workflow (was designed using [Creately](https://creately.com/)). 
![The structure and workflow of the website](static/images/readme/structure.png "The structure and workflow of the website")  
Navigation to Home Page, Explore Recipes Page, View Profile Page, Create Recipe Page, My Cookbook Page, and to Log Out are always available on Navbar. So for instance if the users decide to log out when they are in the middle of creating a recipe, they can do it easily.  

#### **Organisation of Functionality and Content**
* **Navbar**:   
   - For Guest User: Home, Explore Recipes, Sign Up, Log In   
   - For Logged In User: Home, Explore Recipes, A profile picture dropdown button with nav links to: View Profile, Create Recipes, My Cookbook, Log Out.   
* **Home Page**: Search Recipes, Carousel of 8 Popular Recipes, Carousel of 8 Newest Recipes, Carousel of Cookbooks Reccomendation, Invite a friend.
* **Explore Recipes Page**: Searh Recipes, All Recipes in the site can be viewed here.
* **Individual Recipe Page**: 
   - For Guest User: View the recipe, Share recipe, Print recipe, Add recipe to cookbook and Like recipe (will be directed to login page).
   - For Logged In User: View the recipe, Share recipe, Print recipe, Add recipe to cookbook/ Remove from cookbook, Like recipe/ Remove a like, Write review.
   - For Logged In User who created that recipe: additional option to Edit recipe and Delete recipe.   
   - For Logged In User who had written a review on that page: additional option to Edit review and Delete review.
* **View Profile Page**: Edit profile, Delete account.
* **Create Recipe Page**: Create a recipe.
* **My Cookbook**: View own recipes and previously saved recipes.
* **Footer**: same navigation links as Navbar, with additional Contact Us and social media information.   


#### **Database Structure**

### **4. Skeleton Plane**
Wireframes/ mock-ups were created using Figma to design the navigation and interface of the website. For a better and clearer visualization before coding, and also to check if the color scheme and images match and work great together, the wireframes were created fully designed.

[Wireframes for Home Page](static/images/readme/wireframes/homepage-wireframe.png)



