# Cookle - Testing  

[Back to the main README.md file](https://github.com/dissyulina/cookle-cookbook#cookle)  

[Back to the Testing section in main README.md file](https://github.com/dissyulina/cookle-cookbook#4-testing)  

[View live website here](https://cookle-cookbook.herokuapp.com/)   

<br/>  

**Table of Contents** 
1. [User Stories Testing]()  
2. [Manual Testing]()  
   a. [Responsiveness Testing]()  
   b. [Links Testing]()  
   c. [Game Play Testing]()   
   d. [Form Testing]()  
3. [Autoprefixer CSS]()  
4. [W3C Validator Testing]()  
5. [JSHint Testing]()   
6. [Lighthouse Testing]()  
7. [CI Peer Code Review on Slack]()
8. [Further Testing]()  

<br/>  

## **1. User Stories Testing**  
### **Unregistered User Goals**   
As a new/ unregistered user, I want to:
1. Be able to search a recipe easily
   * On the landing page in the middle of the screen, users can immediately see a search recipes input box where they can type a keyword to search the recipe.  
   * On the top right of the screen, a navigation link named "Explore Recipes" provides another way to search the recipes by navigating first to that page.  
   ![Search box on landing page](static/images/readme/testing/user-stories/search-box.jpg "Search box on landing page")
   ![Explore Recipes navigation link](static/images/readme/testing/user-stories/explore-recipes-navlink.jpg "Explore Recipes navigation link")   


2. See the popular recipes of the site  
   * On the Home Page (index.html), below the hero-image, users can find eight most popular recipes in the site. These are the recipes that have the most number of likes. 
   * The recipes are organized in a carousel of recipe cards, with an autoslide feature. The user can also flick the cards on touch screen devices, or click the right arrow (next) or left arrow (previous) to navigate between cards.
   ![Popular Recipes carousel](static/images/readme/testing/user-stories/popular-recipes.jpg "Popular Recipes carousel")   

3. Explore all recipes that listed in the site  
   * Right below the popular recipes carousel, there's a link to "See more recipes". This link will direct the user to the Explore Recipes page (recipes.html).  
   * On the navigation bar, the user can navigate to the Explore Recipes page by clicking the Explore Recipes navigation link.  
   * Below are the screenshot of the Explore Recipes page on tablet device.  
   ![Explore Recipes page](static/images/readme/testing/user-stories/explore-recipes.jpg "Explore Recipes page")  

4. Be able to view a full recipe that I'm interested in   
   * By clicking a recipe card, the user can view the full recipe even if they aren't registered/ logged-in yet.  
   * Below are the screenshot of the Individual Recipe page (single-recipe.html).  
   ![Individual Recipe page](static/images/readme/testing/user-stories/individual-recipe.jpg "Individual Recipe page")  

5. Navigate intuitively and can spot the Sign Up button right away  
   * For unregistered users, the links on Navbar that are available to navigate are: Homepage, Explore Recipes page, Sign Up, and Log In.
   * On the landing page, the users can see the Sign Up and Log In button right away, located on the top right of the screen.  
   ![Navbar](static/images/readme/testing/user-stories/navbar-unregistered-user.jpg "Navbar")  
   * The Navbar are dissapering on scroll down, but will be re-appearing again on a bit of scroll up. This way the users have easy access to the Navbar, and at the same time it also save spaces, allowing the content to have a full screen display. 
   * The footer, which is available at the very bottom of every page, also provides same the navigation links as Navbar.  
   ![Footer](static/images/readme/testing/user-stories/footer-unregistered-user.jpg "Footer")  

6. Understand what the site is about and how it works  
   * On the Home page, inside the hero-image, a title and tagline for the website is placed to give a user an introduction to the website in a very short statement.  
   ![Title and tagline](static/images/readme/testing/user-stories/home-title.jpg "Title and tagline")  
   * If the user decided to scroll down to investigate more and read further about the website, the user will find a little section that explains how it works, which ends with the invitation to sign up.  
   ![How it works section](static/images/readme/testing/user-stories/how-it-works.jpg "How it works section")  


### **Registered User Goals**   
As a returning/ registered user, I want to:  
1. Immediately be able to spot the Log In button  
   * The Log In button is can be seen right away at the top right of the page.  
   ![Log In button](static/images/readme/testing/user-stories/login.jpg "Log In button")  

2. See the newest added recipes on the site  
   * On the Home Page, below the popular recipes carousel, users can find eight newest added recipes in the database.  
   * The recipes are organized in a carousel of recipe cards, with an autoslide feature. The user can also flick the cards on touch screen devices, or click the right arrow (next) or left arrow (previous) to navigate between cards.  
   ![Newest Recipes carousel](static/images/readme/testing/user-stories/newest-recipes.jpg "Newest Recipes carousel")  

3. Once logged in, easily navigate  to my account settings, my cookbook, and other pages available to me.  
   * Once the user logged-in or signed-up, the links on Navbar that are available to navigate are: Homepage, Explore Recipes page, My Cookbook page, A Dropdown profile picture which has navigation items: Create Recipe, View Profile, and Log Out.  
   ![Navbar for logged-in user](static/images/readme/testing/user-stories/navbar-logged-in-user.jpg "Navbar for logged-in user")  

4. Be able to Edit or Delete my profile
   * Once the user logged-in or signed-up, they will be directed to the Profile page. The first section of the Profile page is "My Profile", where user can see their account information. User can manage their account by clicking the "Manage Account" dropdown button on the top right corner, with options to : Edit Profile (change Username, change Email, change About Me, and change/upload a profile image), Change Password, and Delete Account.  
   ![Manage Account](static/images/readme/testing/user-stories/manage-account.jpg "Manage Account")  
   * When the user click "Edit Profile", the user will be directed to the Edit Profile page (edit-profile.html), with buttons to Cancel and to Submit the edited profile.
   ![Edit Profile](static/images/readme/testing/user-stories/edit-profile.jpg "Edit Profile")  
   * The user can also delete their profile by clicking "Delete Profile" button. A modal will pop up to confirm the deletion, as a barrier in case the user accidentaly clicked the button. The modal comes with buttons to Cancel and to Delete the profile.  
   ![Modal confirmation before deleting an account](static/images/readme/testing/user-stories/modal-delete-account.jpg "Modal confirmation before deleting an account")  

5. Be able to Create a recipe and share it to the site, and to Edit or Delete it afterwards as needed  
   * There are various ways users can create a recipe, to ensure easy navigation, by clicking :
     - Call to Action button on the Profile page, or  
     ![CTA create recipe on profile page](static/images/readme/testing/user-stories/cta-profile-create-recipe.jpg "CTA create recipe on profile page")  
     - The profile picture dropdown button on the Navbar and choose Create Recipe, or  
     ![Navigation link create recipe](static/images/readme/testing/user-stories/navbar-create-recipe.jpg "Navigation link create recipe")  
     - Call to action button on the bottom of My Cookbook page, or  
     ![CTA create recipe on my cookbook page](static/images/readme/testing/user-stories/cta-cookbook-create-recipe.jpg "CTA create recipe on my cookbook page")  
     - Navigation link to Create Recipe on the footer 
   * Once the user clicked the Create Recipe link/ button, they will be directed to the Create Recipe page (see here)
   * There are various was to Edit or Delete a recipe: 
     - After user created a recipe, the user will be directed to the newly created recipe page. On the top right of the recipe page, the user wil be able to locate an Edit button and a Delete button.  
     ![Edit and Delete Recipe on Recipe page](static/images/readme/testing/user-stories/edit-delete-recipe.jpg "Edit and Delete Recipe on Recipe page")  
     - The user can also manage all their created recipes from the Profile page by clicking the "Uploaded Recipes" collapse button, and navigate to the ellipsis button to find the option to Edit and Delete.  
     ![Edit and Delete Recipe on Profile page](static/images/readme/testing/user-stories/profile-uploaded-recipes.jpg "Edit and Delete Recipe on Profile page")  
   * Once the user clicked the Edit Recipe button, they will be directed to the Edit Recipe page (see here).  
   * Once the user clicked the Delete Recipe button, a modal will pop up to confirm the deletion, as a barrier in case the user accidentaly clicked the button. The modal comes with buttons to Cancel and to Delete the recipe.  
     ![Modal confirmatin before deleting recipe](static/images/readme/testing/user-stories/modal-delete-recipe.jpg "Modal confirmatin before deleting recipe")   

6. Be able to Save a recipe that I like to my cookbook, and to remove it from my cookbook as needed.  
   * Ways to save a recipe to user's cookbook:
     - By clicking the plus button on a recipe card. When a recipe is already saved to the cookbook, the plus button becomes disabled and displays a check icon.  
     ![A Recipe Card](static/images/readme/testing/user-stories/recipe-card.jpg "A Recipe Card") 
     ![An already saved Recipe Card](static/images/readme/testing/user-stories/recipe-card-saved.jpg "An already saved Recipe Card")  
     - By clicking the "Save to cookbook" button on a recipe page. When a recipe is already saved to the cookbook, the button will displays "Saved to Cookbook" with a checked icon.  
     ![Save Recipe on Recipe page](static/images/readme/testing/user-stories/save-recipe.jpg "Save Recipe on Recipe page") 
     ![Saved Recipe on Recipe page](static/images/readme/testing/user-stories/saved-recipe.jpg "Saved Recipe on Recipe page")   

   * Ways to remove a recipe from user's cookbook:  
     - By clicking again the Saved to Cookbook button on the Recipe page (see images from previous point). A modal to confirm the remove will show up.
     - By managing it from the Profile page, where the usec can click on the "See All My Saved Recipes" collapse button, then click the trash icon located on the right side of the recipe's name that the user wants to remove.  
     ![Remove recipes from cookbook on profile page](static/images/readme/testing/user-stories/profile-saved-recipes.jpg "Remove recipes from cookbook on profile page")  
     - A modal will pop up to confirm the remove, as a barrier in case the user accidentaly clicked the button. The modal comes with buttons to Cancel and to Remove.  
     ![Modal confirmation before removing recipe from cookbook](static/images/readme/testing/user-stories/modal-remove-recipe.jpg "Modal confirmation before removing recipe from cookbook")  

7. Be able to give a like to a recipe, and also unlike it as needed.  
   * To like a recipe, simply click the "Like this recipe" button on the Recipe page. The button will then turn to "Liked", and the number of likes will increase by one. To unlike a recipe, clicked the "Liked" button again, and it will turn back to "Like this recipe", and the number of likes will decrease by one as well.  
   ![Like this recipe](static/images/readme/testing/user-stories/like-recipe.jpg "Like this recipe") 
   ![A liked recipe](static/images/readme/testing/user-stories/liked-recipe.jpg "A liked recipe")   

8. Be able to write a review on a recipe page, and to edit or delete my review  
   * To write a review, click the "Write A Review" button on a Recipe page. A text-area form will show up with a Cancel and Submit Review buttons.  
   ![Write review](static/images/readme/testing/user-stories/write-review.jpg "Write review")  
   * To edit a review, click on the elipsis button on the right side of the review that the user wants to edit. It will show the options to edit or to delete review. After choosing the Edit button, a text-area with the review text inside will show up.  
   ![Edit and delete review buttons](static/images/readme/testing/user-stories/edit-delete-review.jpg "Edit and delete review buttons")  
   ![Edit review](static/images/readme/testing/user-stories/edit-review.jpg "Edit review")   
   * To delete a review, click again on the elipsis button on the right side of the review that the user wants to delete, and choose the delete option. A modal confirmation will pop up.  
   ![Modal confirmation before deleting a review](static/images/readme/testing/user-stories/modal-delete-review.jpg "Modal confirmation before deleting a review")  

9. Be able to share a recipe on social media easily  
   * A dropdown share button is located on the top right of the Recipe page. When clicked, it provides the options to share the recipe page to: Whatsapp, Facebook, Twitter, and Pinterest.  
   ![Share a recipe page to social media](static/images/readme/testing/user-stories/share.jpg "Share a recipe page to social media")   

10. Be able to print a recipe easily
   * A print button is located on the top right of the Recipe page. When clicked, it connects right away to the print feature of the users' computer.  
   ![Print a recipe page](static/images/readme/testing/user-stories/print.jpg "Print a recipe page")  
   
11. Find a contact page for my inquiries  
   * To contact the admin or site owners, users can navigate to the footer and click on the "Contact Form" button. Another option to contact would be to send an email or to find the social media page. When the contact form button is clicked, a contact form modal will show up.  
   ![Contact form](static/images/readme/testing/user-stories/contact-form.jpg "Contact form")  


### **Administrative Account**   
As an Administrative Account holder, I want to:
1. Be able to do all the functionalities as a registered user can
   * All functionalities as a general user are available for the admin.  

2. Add, Edit, or Delete a category of recipes  
   * Once the Admin logged-in, a "Manage Categories" navigation link can be found inside the profile picture dropdown button. This navigation link will direct the Admin to the Manage Categories page (categories.html).    
   ![Manage Categories navigation link](static/images/readme/testing/user-stories/manage-categories-navlink.jpg "Manage Categories navigation link")   
   * Inside the Manage Categories page, Admin can add a new category, and edit or delete a category.  
   ![Manage Categories](static/images/readme/testing/user-stories/manage-categories.jpg "Manage Categories")   
   * A modal will show up when the Delete button is clicked, confirming the deletion.  
   ![Modal confirmation before deleting a category](static/images/readme/testing/user-stories/modal-delete-category.jpg "Modal confirmation before deleting a category")   

3. Be able to edit any recipes listed on the site as needed.  
   * The Edit Recipe button on each of the recipe page is available for admin to access, even though the recipe was created by another user. This functionality is added for Admin in order to keep the database clean.
  
4. Be able to delete any recipes listed on the site as needed.  
   * The Delete Recipe button on each of the recipe page is available for admin to access, even though the recipe was created by another user. This functionality is added for Admin in order to keep the database clean.  

5. Be able to delete offensive reviews on the site as needed.  
   * The Delete review button inside the ellipsis dropdown button is available for admin to access. Admin can only delete a review, not edit it.  

<br/>  


## **2. Auto Prefixer CSS**   
Autoprefixer CSS was used to add CSS vendor prefixes to the CSS rules after the developing process was done, to ensure that the they work across all browsers. 

<br/>  

## **3. Manual Testing by the developer**  
### **Browsers Compatibility**  
The website was tested through the following browsers: Google Chrome, Microsoft Edge, Opera, Mozilla Firefox, and Safari (iOS) browsers.  

### **Devices**
The website was also views on the following devices: 
- Windows Desktop 
- Windows Laptop  
- Tablets: iPad Mini 2 and iPad 2018
- Mobile: iPhone7, iPhone 8, iPhone 12 Mini, Asus Zenfone Max Pro M2, and LG G5  
- Friends and family members were asked to review the site on their devices and to point out any bugs and/or user experience issues.  

### **Responsiveness**
To check the responsiveness of the website across all devices, the developer tools are used regularly during the developing process.  
[Responsiveness Checker](https://www.websiteplanet.com/webtools/responsive-checker/?url=https%3A%2F%2Fcookle-cookbook.herokuapp.com%2F) to test the responsiveness. Below are a few examples.
- [Responsiveness check on Samsung Galaxy tab 7, Kindle Fire](static/images/readme/testing/responsiveness/galaxytab7-kindle.jpg)  
- [Responsiveness check on Samsung S9](static/images/readme/testing/responsiveness/samsungS9.jpg)  
- [Responsiveness check on 13 inch notebook](static/images/readme/testing/responsiveness/13notebook.jpg)    

### **Links**  
The links were tested to ensure that:  
- All navigation links are linking correctly.  
- All buttons on the forms are working (to cancel or to submit the form).  
- The social media buttons are working and opening in a new tab.  

All of the above are working properly.  

### **Forms**
The form was also tested to ensure that:  
- The ```required``` attributes are working.  
- The regex patterns for username and password are working.
- There's a validation message that explains the correct format if user filled in the wrong format.  

For Contact Form (using email js), the test was performed to ensure that:
- When a valid Contact form is submitted, a modal will show up for 2 seconds with text "Message sent" as a response to the user.  
- The Contact Form is reset (all fields are empty again).
- The developer gets the notification message in their inbox.  
- The sender gets a thank you message in their inbox.  

For Invitation email (also using email js), the test was performed to ensure that:
- When a valid email address is submitted, the button will turn to "Sent" for 2 seconds as a response to the user.  
- The input area is blank again.
- A message is sent to the email address, to invite the receiver to sign up to Cookle.  

All of the above are working properly.  

### **Defensive Testing**
The defensive testing was done to make sure certain actions can only be performed by authorized user/admin. The test was done such as: 
- Typing the url to try to access other user's edit recipe page : ```https://cookle-cookbook.herokuapp.com/edit_recipe/<recipe_id>``` 
- Typing the url to try to access other user's profile page : ```https://cookle-cookbook.herokuapp.com/profile/<username>```   
- Typing the url to try to access other user's cookbook page : ```https://cookle-cookbook.herokuapp.com/cookbook/<username>```   
- Typing the url to try to access manage categories page without logging in as Admin : ```https://cookle-cookbook.herokuapp.com/manage_categories``` 
- etc.

When a user tries to perform unauthorized action such above, a flash message with red text "You are not authorized to view that page" will be showed.  

<br/>   

## **4. W3C Validator Testing**  
The [W3C Markup Validator](https://validator.w3.org) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) were used to validate the website to ensure there were no syntax errors in the project. The results are below:  

### **HTML**  
These are the summary of warning/ errors that I got on the first test. 
Error/ Warnings | Actions  
 --- | ---
Element div not allowed as child of element ul in this context. (Suppressing further errors from this subtree.) | Change the ```<div>``` to ```<li>``` element   
An img element must have an alt attribute, except under certain conditions. | Add an ```alt``` attribute   
The value of the for attribute of the label element must be the ID of a non-hidden form control. | Add an id to the ```input``` element   
Duplicate IDs | Change the repeated id   

The duplicate IDs error is existed on almost all pages. This happened because for element inside a loop, for example a review inside a for loop template that has an id attribute. Because the number of the reviews that generated were more than 1, the id repeated and therefore gave an error. The solution for this was to put ```review._id``` inside the id, so that it will become unique.  
All warnings and erros were fixed and I put the Html file back to the test. In the end, no warnings or errors were found on all pages.  
* [Homepage (index.html)](static/images/readme/testing/html-css-validator/index.jpg)  
* [Explore Recipes Page (explore-recipes.html)](static/images/readme/testing/html-css-validator/explore-recipes.jpg)  
* [Sign Up Page (register.html)](static/images/readme/testing/html-css-validator/register.jpg)  
* [Log In Page (login.html)](static/images/readme/testing/html-css-validator/login.jpg)  
* [Profile Page (profile.html)](static/images/readme/testing/html-css-validator/profile.jpg)  
* [Edit Profile Page (edit-profile.html)](static/images/readme/testing/html-css-validator/edit-profile.jpg)  
* [Change Password Page (change-password.html)](static/images/readme/testing/html-css-validator/change-password.jpg)  
* [Create Recipe Page (add-recipe.html)](static/images/readme/testing/html-css-validator/add-recipe.jpg)  
* [Individual Recipe Page (single-recipe.html)](static/images/readme/testing/html-css-validator/single-recipe.jpg)  
* [Edit Recipe Page (edit-recipe.html)](static/images/readme/testing/html-css-validator/edit-recipe.jpg)  
* [My Cookbook Page (add-recipe.html)](static/images/readme/testing/html-css-validator/cookbook.jpg)  
* [Manage Categories Page (categories.html)](static/images/readme/testing/html-css-validator/categories.jpg)  
* [Edit Category Page (edit-category.html)](static/images/readme/testing/html-css-validator/edit-category.jpg)  
* [Add Category Page (add-category.html)](static/images/readme/testing/html-css-validator/add-category.jpg)  


### **CSS**
No errors were found, but there are 15 warnings and they are all concerning the vendor prefixes added by Autoprefixer CSS. I decided to ignore the warnings because the vendor prefixes are important to ensure that the styling works across different browsers. 
* [No Errors found](static/images/readme/testing/html-css-validator/css-no-error.jpg) 
* [15 Warnings](static/images/readme/testing/html-css-validator/css-warnings.jpg)   

<br/>  


## **5. JavaScript Testing**  
I ran the javascript code through [JSHint](https://jshint.com/), and there were some warnings. 
Warnings | Actions  
--- | ---   
Missing semicolons | Semicolons is added
Unused variables | Remove the unused variables
Undefined variables | Define the variables 

All of the warnings have been fixed, except for one warning which shows ```emailjs``` as an undefined variable. However, ```emailjs``` is an external variable from a service that allows sending email from JavaScript, so it's not defined inside the js file. [See here the screen capture of the testing result](static/images/readme/testing/js-hint.jpg).  

<br/>  

## **6. Python Testing**  
I ran the python code through [Pep8 Online](http://pep8online.com/) and it returned no errors. [See here the screen capture of the testing result](static/images/readme/testing/pep8-test.jpg).   

<br/>  

## **7. Lighthouse Testing**  
The Chrome Lighthouse testing was used to audit the performance, accessibility, best practices, and SEO. Below are the result.   

Page Name | Performance | Accessbility | Best Practices | SEO | See link   
--- | --- | --- | ---  | --- | ---    
index.html |  94 | 97 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/index-desktop.jpg)   
explore-recipes.html | 94 | 94 | 100 | 90 | [see here](static/images/readme/testing/lighthouse/explore-recipes-desktop.jpg)   
register.html | 95 | 92 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/register-desktop.jpg)   
login.html | 97 | 99 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/login-desktop.jpg)  
profile.html | 91 | 98 | 100 | 90 | [see here](static/images/readme/testing/lighthouse/profile-desktop.jpg)  
edit-profile.html | 86 | 99 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/edit-profile-desktop.jpg)   
change-password.html | 96 | 99 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/change-password-desktop.jpg)  
add-recipe.html | 88 | 97 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/add-recipe-desktop.jpg)  
single-recipe.html | 94 | 91 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/single-recipe-desktop.jpg)  
edit-recipe.html | 96 | 97 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/edit-recipe-desktop.jpg)  
cookbook.html | 86 | 94 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/cookbook-desktop.jpg)  
categories.html | 96 | 98 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/categories-desktop.jpg)  
edit-category.html | 97 | 97 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/edit-category-desktop.jpg)  
add-category.html | 94 | 97 | 100 | 100 | [see here](static/images/readme/testing/lighthouse/add-category-desktop.jpg)  







