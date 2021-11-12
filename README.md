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
Database schema was designed using [diagram.io](https://dbdiagram.io/home).   
![Database structure](static/images/readme/database.png "Database structure")   

<br/>   

### **4. Skeleton Plane**
Wireframes/ mock-ups were created using Figma to design the navigation and interface of the website. For a better and clearer visualization before coding, and also to check if the color scheme and images match and work great together, the wireframes were created with such details, in three different device sizes: desktop, tablet, and mobile.   

* [Wireframes for Home Page](static/images/readme/wireframes/homepage-wireframe.png)   
* [Wireframes for Explore Recipes Page](static/images/readme/wireframes/explore-recipes-wireframe.png)   
* [Wireframes for Individual Recipe Page](static/images/readme/wireframes/individual-recipe-wireframe.png)   
* [Wireframes for Sign Up Page](static/images/readme/wireframes/sign-up-wireframe.png)   
* [Wireframes for Create and Edit Recipe Page](static/images/readme/wireframes/create-edit-recipe-wireframe.png)   
* [Wireframes for My Cookbook Page](static/images/readme/wireframes/my-cookbook-wireframe.png)   
* [Wireframes for View Profile Page](static/images/readme/wireframes/view-profile-wireframe.png)  


#### **Design Changes on The Final Product**
While I relied heavily on these Wireframes in order to maintain the desired design, there are several differences between the Mockups and the final product:

* Colors of the buttons were altered to separate the functionality more consistently:
  - Green buttons for things that related to user/ profile: Sign Up, Log In, Edit Profile, Delete Account   
  - Orange buttons for things that related to the recipes and reviews   
  The shades were a bit darkened to achieve the desirable contrast with the text inside, while still maintaining the green and orange color scheme.   
* The site name 'Cookle' was displayed in the landing page for branding purpose
* The text 'search' inside the search button is changed to a magnifying glass icon to save spaces.   
* Write a review button on individual recipe page was placed closer to the review section for easier access, especially in small devices.   
* On Explore Recipe page, in the wireframes there were navigation pills to choose the category. The same navigation pills were also used in My Cookbook to separate the self-created recipes and the saved recipes. After applying this pills, I found it hard to apply pagination to the page that use navigation pills. Because of that, the navigation pills in Explore recipes were changed to select element to choose the category.

<br/>   

### **5. Surface Plane**   
#### **Color Scheme**   
The overall theme of the site was orange and green, which were derived from the hero image. Using [Coolors](https://coolors.co), I add the colors from the hero image, darkened the green and orange as necessary to achieve a higher contrast with white text inside.   
![The color scheme](static/images/readme/color-scheme.jpg "The color scheme")  

#### **Typography**  
All of the fonts were sourced from [Google Fonts](https://fonts.google.com).   
* Main fonts: Nunito Sans   
  A sans-serif type of font was chosen to give a simple, clean, and modern look to the site. As the background is already filled with blob patterns and fun colors, it is important to balance it out with a simple font.
* Logo fonts: Pacifico   
  A cursive type of font Pacifico was used only for the logo 'Cookle', and was chosen to contrast it with the main font. So that it's easily recognisable between website content.

#### **Imagery**  
- Hero Image was chosen because it’s bright, fun, and capturing attention on the first impression. It is also picturing various food items that corresponds to a recipe sharing web application. The hero image was chosen at the first stage of designing the site and determines the whole color theme of the website, thus it has a very important role.
- The background image for all pages (excluding index.html) was actually the hero image without most of its drawing components. Using online editor [Photopea](https://www.photopea.com/), I edited the hero image.   

<br/>   

## **Features**  
### **Existing Features**  
### **a. General Design Features**  
   - **Fully responsive** - Each page of the site is fully responsive on all device sizes (with minimum dimension 320px or an iPhone 5) and features intuitive navigational buttons.   
   - **Navbar** - The Navbar is responsive and turns to a hamburger menu in smaller device. The Navbar is fixed, dissapering on scroll down, and showing again on scroll up. This feature gives the best of both worlds where the user can always access the Navbar without it taking up the space for content.
      * For guest users, the Sign Up and Log In buttons are visible right away, conventionally placed at the top-right of the page.
      * After the user successfully logged in, the previously Sign Up and Log In buttons turn to a profile picture navigation drop down, which provvides the links to Create Recipe, to View Profile, to go to My Cookbook, and to Log Out.
   - **Flash Messages** - Flash messages provide the user the necessary feedback of their action whether it's successfully executed or not.
   - **Recipe Cards** - Recipe cards are used consistently throughout the website, providing users with the image of the recipe, the recipe's name, total likes, and add to cookbook button (a plus sign icon). This add to cookbook button is also displayed even when the user hasn't logged in/ registered, in order to give the user a glimpse of what they can get by registering to the website. When guest users click this button, it will direct them to the login page.
   - **Footer** - The footer is available on all pages, provides the navigation links like Navbar, with additional contact information and social media icons. 
   - **A Secure Website** - In addition to front-end manipulation (for instance the Edit Recipe button is hidden for users that don't own that recipe), a back-end defensive programming was also built to prevent any unallowed action performed by a user.   

### **b. Page Design Features**     

   - **Home Page / Landing Page**
     * **Search Bar** : Right away centered in the middle of the hero-image, a Search Bar allows users to search a recipe. After the users click the search button, they will be brought to the Explore Recipes page with the result of their query. 
     * **Carousel** : There are three carousels in the home page, displaying 8 Popular Recipes, 8 Newest Recipes, and 6 Cookbook Recommendation. Carousel was chosen to add some interactive section for the user, also to allow more contents to be displayed.
     * **Sign Up** : A small section inviting the users to register to site by explaining how the website works.
     * **Invite Your Friends** : Also a small section to convince users to invite their friends and family to join Cookle.   

   - **Explore Recipes**   
     * **Search Bar** : Search bar function allowing users to search for a recipe.
     * **Category Select** : Category select element allowing users to view all recipes based on a category.
     * **Reset Button** : A reset button was placed under the search bar and the select category, allowing users to reset the query and show all recipes instead.
     * **Recipe Cards** : All recipes in the website is displayed alphabetically ordered in cards. If users use the search or category select, the cards are sorted by number of likes. 
     * **Pagination** : Pagination functionality will be activated when the recipes displayed are more than 12 recipes.   
   
   - **Sign Up Page**   
     * **Input Fields** : The input fields allow users to enter their information to register to the website. It's built with validation messages as a respond if the users fill it incorrectly. 
     * **Image Preview** : One of the fields that the users can fill out is a profile image (url). This will come with an image preview for the image url that the users provide.
     * **Confirm Password** :  The password field is hashed using [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security). Once the password field is filled, there is a confirm password field to ensure the users had written the desirable password. The submit form button is disabled untill both passwords matches.
     * **Log In Option** : At the bottom of the form, there's a reminder to the users to log in instead if they already have an account.

     
   







