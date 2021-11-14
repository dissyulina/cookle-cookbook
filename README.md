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
   - **A Secure Website** - In addition to front-end manipulation (for example the Edit Recipe button is hidden for users that don't own that recipe), a back-end defensive programming was also built to prevent any unallowed action performed by a user.   
   - **CONTACT MODAL**
   - **Modal Confirmation**

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
     * **Input Fields** : The input fields allow users to enter their information to register to the website. 
       The input fields consist of: 
       - Name (required) 
       - Username (required) 
       - Email (required) 
       - Password (required) 
       - Repeat Password (required)
       - About you and your love for cooking (optional)
       - Profile Image (optional)
       They're built with validation messages as a respond if the users fill it incorrectly. 
     * **Image Preview** : One of the fields that the users can fill out is a profile image (url). This will come with an image preview for the image url the users provide.
     * **Confirm Password** :  The password field is hashed using [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security). Once the password field is filled, there is a confirm password field to ensure the users had written the desirable password. The submit form button is disabled untill both passwords matches.
     * **Sign Up (Submit) Button** : A sign up button to submit the registration form.
     * **Log In Option** : At the bottom of the form, there's a reminder to the users to log in instead if they already have an account.  
   
   - **Log In Page** 
     * **Input Fields** : The input fields allow users to enter their information to login to the website, by providing Username and Password.
     * **Log In (Submit) Button** : A log in button to submit the login form.
     * **Sign Up Option** : At the bottom of the form, there's a reminder to the users to sign up instead if they are not a member.   
    
   - **Profile Page**   
     * **View Profile** : Small section where users can see their profile image, username, email address, and about you.
     * **User Management Buttons** : Users can find buttons to Edit their profile, or Delete their account on the top right of the page.   
     * **Call to Action Buttons (Recipe Sharing)** : From this page users can also directly access all pages, including Create Recipe page, Explore Recipes page, and My Cookbook page.
     * **Collapsible Uploaded Recipes** : Users can see all their uploaded recipes in one page, in a collapsible button to save spaces. There's a vertical ellipsis button at the end of every recipe title, that provides edit or delete option. The recipe title is also clickable, and users can directly go to the recipe page.
     * **Collapsible Saved Recipes** : Same as the collapsible uploaded recipes, users can also see all their saved recipes in one page in a collapsible button. There's a remove recipe button (trash can icon) at the end of every recipe title, that provides the functionality to remove the recipe from users' cookbook. The recipe title is clickable as well, and users can directly go to the recipe page.  

   - **Edit Profile Page**  
     * **Input Fields** : The input fields are prepopulated with users existing information.
       The input fields that can be edited include: 
       - Username (required) 
       - Email (required) 
       - About you and your love for cooking (optional)
       - Profile Image (optional)
     * **Image Preview** : One of the fields that the users can fill out is a profile image (url). This will come with an image preview for the image url the users provide.
     * **Submit and Cancel Buttons** : A submit and cancel buttons for the form. After one of the buttons is clicked, it will direct the users back to the Profile page.

   - **Create Recipe Page**  
     * **Input Fields** : The input fields allow users to enter the recipe's information to the website. 
       The input fields consist of: 
       - Recipe's Name (required) 
       - Description of the recipe (optional)
       - Serving (optional)
       - Preparation + Cooking Time (optional)  
       - Category (required)
       - Ingredients (required)
       - Directions (required)
       - Recipe's Image (optional)
     * **Image Preview** : One of the fields that the users can fill out is a recipe image (url). This will come with an image preview for the image url the users provide.  
     * **Submit and Cancel Buttons** : A submit and cancel buttons for the form. After one of the buttons is clicked, it will direct the users to Explore Recipes page.  

   - **Single Recipe Page** 
     * **Recipe's Information** : All information from the Create Recipe form are displayed in one page.
     * **Reviews section** : Right below the recipe, there's a review section where all reviews are displayed. Every review consists of a profile picture and username of the writer and the review itself.
     * **Call to Action Buttons**
       - **Share Button** : On the top right of the page, users can find Share to social media button (Share to Whatsapp, Facebook, Twitter, and Pinterest). It's considered beneficial for the site if the users want to share this recipe to social media, as this could lead to more recognition to the site and would hopefully bring more members. I used sharer.js which is a small javascript libary for this functionality.
       - **Print Button** : Next to the Share button, users can find Print button that provide convinience for users to print the recipe.
       - **Edit Recipe and Delete Recipe Buttons** : These two buttons are placed next to the print button and only displayed for user that has created the recipe. The Edit Recipe button will bring the user to the Edit Recipe page. While clicking the Delete Recipe button will bring up a modal to confirm before removing the recipe.
       - **Add to Cookbook Button** : Users can add this recipe to their cookbook by clicking this button. The button will changed to Saved to Cookbook (with a check icon) if the recipe is added to the Cookbook. If it's clicked again, there's a modal confirmation to confirm if the users actually want to remove this recipe from their cookbook. The modal is completed with Cancel and Remove buttons.
       - **Like Button** : Users can like the recipe by clicking this button, and unlike it by clicking it again. A user can like a recipe without saving it on cookbook, and vice versa. The number of likes is an important data for the site, as this number affects the popular recipes carousel on home page, and the search query result is sorted according to number of likes.
       - **Add Review Button** : Users can add a review by clicking the Add Review Button. It will shows a text area form right above the reviews section, completed with a Submit Review and Cancel button.
       - **Edit Review and Delete Review Buttons** : For the reviews that were written by the user, a vertical ellipsis button is placed at the right side of a review, providing option to Edit or to Delete the review.  
    
   - **Edit Recipe Page**
     * **Input Fields** : The input fields are prepopulated with the recipe's existing information. 
       The input fields that can be edited include: 
       - Recipe's Name (required) 
       - Description of the recipe (optional)
       - Serving (optional)
       - Preparation + Cooking Time (optional)  
       - Category (required)
       - Ingredients (required)
       - Directions (required)
       - Recipe's Image (optional)
     * **Image Preview** : One of the fields that the users can fill out is a recipe image (url). This will come with an image preview for the image url the users provide.  
     * **Submit and Cancel Buttons** : A submit and cancel buttons for the form. After one of the buttons is clicked, it will direct the users back to the Single Recipe page.  

   - **My Cookbook Page**  
     * **Navigation Pills** : My cookbook page consists of three different pills which are: All Recipes (Uploaded + Saved Recipes), Uploaded Recipes, and Saved Recipes. Users can click the navigation pills to navigate between the recipes.
     * **Recipe Cards** : All recipes in the cookbook are displayed alphabetically in cards. 
     * **Call to Action Button** : Users can navigate easily to create a new recipe or to explore recipes from this page.
       - **Create Recipes** : This button will direct users to the Add Recipe form.   
       - **Explore Recipes** : This button will direct users tp the Explore Recipes page.  

   - **Categories Page** (only available to admin)  
     * **All Categories** : All categories are displayed in this page. For now there are 5 categories in the site: Appetizer, Main, Dessert, Snack, and Other. Admin can edit these categories in the future, add a new category, or delete it.
     * **Add Category Button** : As the recipes database grow bigger, admin can add new categories such as drinks, vegetarian, kids menu, etc. It will direct the user to the Add Category Page.
     * **Edit Category Button** : Edit category button is placed for every category. It will direct the users to Edit Category page.
     * **Delete Category Button** : Delete category button is also placed for every category. When clicked, there will be a modal pop up to confirm before deleting.   

   - **Add Category Page** (only available to admin)
     * **Input Field** : The input field allow users to enter a new category name to the website. 
     * **Add Category and Cancel Buttons** : An add category (submit) and cancel buttons for the form.
    
   - **Edit Category Page** (only available to admin)
     * **Input Field** : The input field is alredy prepopulated with the existing category, and it allow users to edit the category.
     * **Edit Category and Cancel Buttons** : An edit category (submit) and cancel buttons for the form.

<br/>   

#### **Features to be implemented in the future**   

Due to limited resources (time constraint, skill of the developer at the moment, and other reasons), some features couldn't be implemented now. In the future on the next development phase, these features would be great addition to the game:   
1. Forgot Password Functionality   
   This functionality would give users an option to change password without logging in first to the website. This would usually be done by sending a secure link to change password to user's email address. For now the users can only change their password by logging in and clicking the change password button.

2. Separate page for review   
   As for now, the reviews were displayed on the same page with the recipe. However if there are a lot of reviews, it would disturbed the recipe page layout because it would be too long. The idea is to displayed only 5 latest reviews and add a link navigation to see all reviews.  

3. A profile page where for public view with all recipes that the user has created   
   A username is not yet clickable for this project. However in futute development of this project, a profile page for public viewing can be built. By clicking a username, another user can view the public profile page, and can see all recipes that this user had created. 

4. Users can upload image from computer   
   It is advisable by Code Institute to use url to upload images in this project. To upload a file from a computer and locate it on somewhere will be covered on the upcoming lesson, Fullstack with Django.     
  
<br/>   

## **Issues and Bugs**  
### **Solved Issues**  
I ran into several issues and bugs while developing the website. Some of the tough ones are listed below, along with the solutions that successfully solved them.   

1. **Issue**: I chose MDB (Material Design Bootstrap) as a main front-end library in this project, having heard that MDB provides the great UI components like Materialize, but also gives the convenience of responsive design as Bootstrap. In the middle of the project I wanted to build some multi-cards carousel for popular recipes, newest recipes, and cookbooks we love on the Home Page. It came by surprise that when I searched this feature on MDB, the multi-items / cards carousel feature was locked and it's only available for paid users. I searched on google and tried to apply various methods that I found, with so many failures, as it was difficult to build a carousel without using a library.   

   **Solution**:  

2. **Issues** : On My Cookbook page, I used navigation pills to separate the recipes into three pills/tabs: Uploaded (self-created) Recipes, Saved Recipes, and All Recipes (Uploaded Recipes + Saved Recipes). I've made the arrays of ```created_recipes``` and ```saved_recipes```  under the  ```Users``` document, therefore I had to concaenate the two arrays, take the ```recipe_id``` and find them inside the ```Recipes``` document.    

   **Solution** : After many search on google, I found [this topic](https://stackoverflow.com/questions/47075081/concatenate-pymongo-cursor) on Stack Overflow, using ```'$or'``` to concatenate two cursors, and applied it successfully.   

3. **Issue** : By reading the pagination method in another students' projects, I could apply the pagination to the Explore Recipes Page without too much difficulties. However when I applied the pagination to My Coobook Page, which has navigation pills inside, I encountered a problem. For example if I was inside the second pill (Saved Recipes), and then I cliked the second page/ next page, it should've brought me to the second page of Saved Recipes. But instead, it went back to the first pill (All Recipes) on second page. After investigating on developer tools, it seemed that when the pagination was clicked, the page reloaded, and the active class automatically went back to the first pill.   

   **Solution** : Once I understood the problem, I used javascript and session storage to manipulate the active class. The last clicked pills is saved the session storage, and on page reloads, add and remove active class manually according to the data from session storage. This way the pagination can be clicked and the page still stays on the active pill.  

### **Known Issues & Unsolved Bugs**  
1. Continuing from Pagination issues on My Cookbook Page, I noticed one more problem that still persisted. For example if I clicked second pill (Saved Recipe), and then I clicked page-2 of Saved Recipe. From there I wanted to go to first pill (All Recipes), it should've displayed All Recipe page-1. But instead it brought me to All Recipes page-2 (the same page as the previous pill). I googled it and found on [Stack Overflow](https://stackoverflow.com/questions/41719318/flask-many-pagination-on-one-single-page-using-flask-paginate-0-4-5) that it was because there were multiple paginations in one page, each linked to the respective pill. The solution was to handle this is with asynchronous requests (Ajax). I should have three separate endpoints for the three lists of items, each paginated individually. The main HTML page will issue Ajax requests to these three endpoints, and moving between pages in one list should not affect the other two lists at all. 
Unfortunately, I didn't find enough documentation about this topic and couldn't apply a solution for this problem. Hopefully as I gain more knowledge and experience, I would be able to solve this on the next development phase.  

<br/>   

## **Technology Used**  
### **Main Languages Used**
   * [HTML5](https://en.wikipedia.org/wiki/HTML5)   
   * [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)   
   * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)   
   * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))   

### **Libraries and Frameworks**   
   * [Material Design For Bootstrap](https://mdbootstrap.com/)  
   MDB was used to assist with the UI/UX components, responsiveness, and styling of the website.  
   * [jQuery 3.6.0](https://jquery.com/)  
   jQuery was used as a JavaScript library to help writing less JavaScript code.  
   * [Sharer.js](https://jinja.palletsprojects.com)   
   Sharer.js was used to provide the share to social media functionality.   
   * [Flask](https://flask.palletsprojects.com)   
   Flask was used as Python web application framework.  
   * [PyMongo](https://pypi.org/project/pymongo/)   
   PyMongo was used as a Python distribution containing tools for working with MongoDB.  
   * [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)   
   Flask-PyMongo was used as a bridge to communicate between Flask and PyMongo.   
   * [Flask-Paginate](https://pypi.org/project/flask-paginate/)  
   Flask-Paginate was used to provide pagination functionality.
   * [Jinja](https://jinja.palletsprojects.com)  
   Jinja was used as a templating language for Python to display backend data to HTML.   
   * [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security)  
   Werkzeug was used for password hashing and authentication.   
   * [Google Fonts](https://fonts.google.com)  
   Google fonts was used to import the "Nunito Sans", and “Pacifico” fonts into the html file, and were used on all parts of the site.  
   * [Font Awesome](https://fontawesome.com)  
   Font Awesome was used throughout the website to add icons for aesthetic and UX purposes.   

### **Database Management**   
   * [MongoDB](https://www.mongodb.com)   
   MongoDB was used as an open source database that stores the data/ documents for the application.  

### **Tools and Programs**  
   * [Git](https://git-scm.com)  
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.  
   * [GitHub](https://github.com)  
   GitHub was used to store the projects code after being pushed from Git. 
   * [Heroku](https://www.heroku.com)   
   Heroku was used to deploy the website.   
   * [Figma](https://www.figma.com)  
   Figma was used to create the wireframes and the high fidelity mock up during the design process.  
   * [Autoprefixer CSS](https://autoprefixer.github.io)  
   Autoprefixer CSS was used to add vendor prefixes to the CSS rules, to ensure that they work across all browsers.   
   * [Am I Responsive](ami.responsivedesign.is)  
   Am I Responsive was used to preview the website across a variety of popular devices.   
   * [Photopea](https://www.photopea.com/)   
   Photopea is an online image editor to edit .ai file, and was used to edit the hero image.  
   * [Tiny JPG](https://tinyjpg.com) and [Tiny PNG](https://tinypng.com)    
   Tiny JPG and Tiny PNG were used to reduce the file size of the images.   
   * [Coolors](https://coolors.co)  
   Coolors was used to create a cohesive color scheme for the website.   


   <br/>





  



   







