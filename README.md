[![Build Status](https://travis-ci.org/johnnycistudent/dogdeal.svg?branch=master)](https://travis-ci.org/johnnycistudent/dogdeal)

# Full-Stack Frameworks Milestone Project

Welcome to my Full-Stack Frameworks Milestone Project which I have entitled "DogDeal". I have chosen to take a different approach then the one suggested in the brief and have built a website in which users can buy man's best friend - Dogs. The purpose of this project is to build an app that allows users to browse, purchase and request a dog or dogs of their choosing.

DogDeal can be accessed here: [https://dog-deal-app.herokuapp.com](https://dog-deal-app.herokuapp.com)

**Disclaimer - I realise dogs are not a commodity that should be traded or purchased like any other product but for the purposes of a college project they make a nice subject matter**

## UX


#### Strategy
*WHY does this site exist? And for who? (Target Audience) Detail goal of creator/user.*  
The idea behind this website is to create a one stop shop for purchasing dogs online. It can also be used to request a breed of dog you can't find anywhere else. Simply place a Request a Dog ad onto the site and the admin can get back to you in the comments below the your ad.

#### Scope
*WHAT are we doing? Outline features and functions that help achieve goals from Strategy.*  


###### Functional requirements
The most basic requirements for this project are to have advertisements that are attractive to the user and easy to read and to have a user registration system that allows users to sign in in order to make purchases or requests.


The site should be responsive and work on all browsers.   

###### Content requirements
The content requirements for the functions proposed above would be as follows:
  - A table to display the advertisements, both sale and wanted
  - A display page for each advertisement
  - Add a Request a Dog form
  - User comments
  - User search query box
  - Registration/Login form
  - User Profile 
  - Log Out button
  - User Password change
  - Shopping Cart
  - Checkout


#### Structure
*HOW - How much content is there, how is it organised, how is it prioritised, interaction design and architecture*  


The information architecture of the...

#### Skeleton
*How is the information structured? How is it logically grouped?*

The information structure is laid out in the wireframes below:

 * [Mobile Wireframes](https://github.com/johnnycistudent/dogdeal/blob/master/static/media/FSF%20Mobile%20wireframes.pdf)
 * [Desktop Wireframes](https://github.com/johnnycistudent/dogdeal/blob/master/static/media/FSF%20Desktop%20wireframes.pdf)

The primary functions are represented in the Navbar links; Dogs for Sale, Request a Dog, User Profile, the Shopping Cart, the search function and the Log Out function. 

The Dogs for Sale display page is the home page as it is the main focus of the website and can be accessed by clicking on the site logo "DogDeal" in the top left hand corner of the navbar. Each ad is accessible through a button on the ad table display. The Admin can access the "Add an Ad" feature from this page to add more ads to the database.

In an individual Dog for Sale page, the user can add any number of dogs to their shopping cart. The user can access their cart from the Navbar where they will see the number of "products" currently in their cart beside the cart icon in the Navbar. The user can then purchase their dogs from their cart from the checkout once the cart is accessed.

The "Request a Dog" display page has the same format as the Dogs for sale display table, with a link to each ad linked within the table. The user can also add their own request through the "Request a Dog" button underneath the Dogs Wanted table. This button will bring the user to a form to add their own requests for dogs from the site.

Once a "Request a Dog" ad is submitted, the user's ad is rendered and they or other users can comment on it below the ad. 

The user can access their profile and log out of the site from the Navbar.

#### Surface
*What will the finished product look like?*
*What colours, typography and design elements will be used?*

I have previously used Bootswatch in other projects and find their themes to be very useful so I used their Simplex theme for this project. The mostly white background contrasts well with the red, blue and purple detailing such as on button links and pagination and also allows the black text to stand out. 

The banner/jumbotron image is a nice photo of a Jack Russell terrier's face with it's nose in the foreground and adds character to the site. 

The font used on the logo for the site is Lato from Google fonts and the icons used through the site are from FontAwesome. 


## User Stories

  **1.** As a registered or non-registered user, I would like to browse/search through the site and see what dogs are available.
  
  **2.** I would like to create a user profile to be able to interact with the site further. 
  
  **3.** I would like to be able to add a dog to the shopping cart and continue browsing the site.
  
  **4.** I would like to be able to safely purchase dogs from the site over a secure connection.
  
  **5.** If I don't see a dog I want on the site, I would like to make a request to the site by using the "Request a Dog" feature.
  
  **6.** I would like the ability to reset my password if I forget it.
  
  **7.** As the Administrator of the site, I would like to be able to easily upload new dogs for sale and edit the ads if there is a typo or change to their sale status.
  
                


## Wireframes

As mentioned in the [Skeleton](#skeleton) above, here are the wireframes created and edited during the production of the site.  

 * [Mobile Wireframes](https://github.com/johnnycistudent/dogdeal/blob/master/static/media/FSF%20Mobile%20wireframes.pdf)
 * [Desktop Wireframes](https://github.com/johnnycistudent/dogdeal/blob/master/static/media/FSF%20Desktop%20wireframes.pdf)



## Features

### Existing Features

  *   **Navbar** - The Navbar offers an easy navigational view through the site for both non-registered and registered users and is always available to act as a reference point for any user not necessarily sure of their whereabouts on the site. It contains a search bar and the user's cart for quick references.
  *   **Advertisement Table view** - The Advertisement table view allows users to view the main relevant ad details. In desktop view the user can see the fields for the Ad title, image, description, breed, location and the "View Ad" button which invites the user to view the ad in its entirety on its own page. In a mobile view, just the most important information is on display to make it easy to read without overcrowding the screen with details; just the Ad title, description and the "View Ad" button.   
  *   **Full Ad Sale Display** - The full ad sale view - "Dogs for Sale" ad - is rendered when the "View Ad" button is followed from the Ad Table view. The Ad information is represented on a card with the photo at the top of the card. If there is no photo, the card starts with the Ad title. The ad lists the following information: Ad title, price, description, breed, colour, location, status, ad views and published date. At the bottom of the ad are the "Add to Cart" button and the quantity field. Below the photo at the top left of the ad are the edit and delete buttons that are only visible to the admin. The heading displayed in the Banner heading is the ad title.    
  *   **Full Ad Wanted Display** - The full ad wanted view - "Request a Dog" ad - is rendered when the "View Ad" button is followed from the Request a Dog Table view. The Ad information is represented on a card like the Full Sale Ad display page but without the photo. The ad lists the following information: Ad title, price, description, breed, colour, location, status, ad views, posted by and published date. The heading displayed in the Banner heading is the requested dog breed. There is a "Add a comment" button below the ad in order for the user/admin to be able to comment on the post.        
  *   **User Comments** - The user comments are used below the "Request a Dog" individual ad pages as way of communicating between the user and admin on the status of the request ads. The comment page itself is just a text field where the user can write their comment and submit. The comments displayed below the ads have the date and the username who posted the comment. When another user comments after the initial comment, it is displayed chronologically from top to bottom so it reads like a regular thread. There is also a delete comment function for the author of the comment at the top right of the comment display.   
  *   **Search bar** - The Search bar is located within the expanded navbar on large screens and also above the Dogs for Sale table display. The results of the user's queries follow best practices of UX design - the user is reminded of their query and informed of the number of results their query has generated. The search submit button can be triggered by the return or enter key on any device that the site is being viewed through.
  *   **Login/Registration forms**  - Each user has the ability to create their own account and they need to do that in order to buy from the site. To register, the user must provide an email address, username and password. The Login form features a reset password link and function (explained fully in [User Stories](#testing-user-stories)). 
  *   **Shopping Cart/Checkout** - The shopping cart is represented in the navbar and allows users to keep adding to it until they are ready to review their order and go to the checkout. The number of items within the cart are represented alongside the cart icon with a number as traditional for ecommerce sites.   
  *   **Footer** - The footer features links to the social media accounts of myself, the site developer and my Github profile.   


## Technologies Used
* [HTML](https://www.w3schools.com/html/html5_intro.asp) - [CSS](https://www.w3schools.com/css/) - [Javascript](https://www.w3schools.com/js/) - [JQuery](https://jquery.com/) - [FontAwesome](https://fontawesome.com/) - [Google Fonts](https://fonts.googleapis.com/css?family=Muli:400,700i|Poppins:400,400i)

    This site's front end is written using HTML, CSS, Javascript and Jquery. It features iconography from FontAwesome's library and fonts from Google Fonts. 

* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - [Bootswatch](https://bootswatch.com/)

    This website uses Bootstrap 4.1.3 and Bootswatch for its framework and for responsivesness. 

* [AWS Cloud9](https://aws.amazon.com/cloud9/)

    The IDE this website was written on is AWS Cloud9. 

* [GitHub](https://github.com) - [Heroku](https://www.heroku.com/) - [Django](https://www.djangoproject.com/) - [Python](https://www.python.org/)

    This website's Git repository is published on GitHub and is deployed on Heroku. The backend code is written in Python and Django is used as the Python web framework.
    
* [PostgreSQL](https://www.postgresql.org/)/[Sqlite3](https://www.sqlite.org/) 

    PostgreSQL is the NoSQL database used for this site and SQLite is used in the development stage.  

    

## Testing

### Testing User Stories

1. As a registered or non-registered user, I would like to browse/search through the site and see what dogs are available.   

   **i.** Go to [the site](https://dog-deal-app.herokuapp.com) and the home page will automatically open on the Dogs for Sale page.  
   **ii.** Scroll and Search through the available dogs by either manually clicking through the pages available or using the search box to find a specific query.   
   **iii.** Click on the "View Ad" button within the advertisement table display or click on the title of the ad to view the full ad.    
  
2. I would like to create a user profile to be able to interact with the site further.   

   **i.** If in mobile view, click on the hamburger menu to reveal the "Register" page link and click it to go through to the Register page. If viewing from a desktop, the "Register" link is simply in the navbar.  
   **ii.** Fill in the form fields - email address, username, password and confirm your password.   
   **iii.** To verify the email field, enter an email address without an "@" symbol and confirm the form does not allow you to continue without a valid email address.  
   **iv.** To verify the password/confirm password fields, enter a password that doesn't match the confirm password. The form should return the "Register" page with a message below the password confirmation field informing the user "Passwords must match".   
   **v.** To verify the username field, enter a name that includes a space (or another invalid character). The form should return the "Register" page with a message below the username field informing the user "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.".  
  
3. I would like to be able to add a dog to the shopping cart and continue browsing the site.

   **i.** Browse through the advertisements and click on "View Ad" to get a full view of the Ad.  
   **ii.** Select the quantity of the product from the selection box beside the "Add to Cart" button and then click the "Add to Cart" button to add the product.    
   **iii.** Verify that the number on the shopping cart icon on the navbar (within the hamburger menu if viewing from a mobile device) corresponds with the quantity you have entered in the previous step.   
   **iv.** Repeat this step on another Dog to verify the correct quantity is added to the cart.   
   **v.** Click into the shopping cart icon to view the order you have so far.    
   **vi.** Change your order by changing the quantity amount on the number field beside one of the products and clicking the amend button or remove it completely by clicking the remove button. Verify the order total changes in accordance with your changes. Stay on this page for the next User story.    

4. I would like to be able to safely purchase dogs from the site over a secure connection.  

   **i.** Following on from the previous step with products in the cart within the shopping cart page, click on the "Checkout" button to go to the checkout page.         
   **ii.** Fill out the personal details fields and then fill out the credit card with Stripe's test number "4242 4242 4242 4242", the security code "111" and the expiration date any date past the current month. Click "Pay Now" button.       
   **iii.**  You should be taken back to the home page with an alert appearing telling you you have successfully paid.    
   **iv.** To test the personal information of the checkout form, leave a field empty, such as "Full Name" and see how the form informs you you are missing an entry.    
   **v.** To test the payment details on the checkout form, enter "4242 4242 4242 4241", replacing the last digit with the number 1 instead of number 2. The form should stop you from submitting and display the error message "Your card number is incorrect." Repeat this step with an erroneous Expiration date and a similar error alert will appear.      


5. If I don't see a dog I want on the site, I would like to make a request to the site by using the "Request a Dog" feature.   

   **i.** After checking the "Dogs for Sale" section, if the user can't find the particular breed of dog they're interested in purchasing they can navigate to the "Request a Dog" page in the Navbar (within the hamburger menu in mobile view).   
   **ii.** Scroll to the bottom of the page and click the "Request a Dog" button.    
   **iii.** Fill out the form with the relevant information and submit it and you will be reverted to the new ad you have created.  
   **iv.**  Review your information in the ad and click the edit symbol in the top right of the advertisement in order to make changes and you will be taken into an edit page.  
   **v.** The Admin and user can converse using the comments underneath the ad and then either can edit the information in the ad to reflect the status of the advertisement.    

6. I would like the ability to reset my password if I forget it.  

   **i.** Make sure you are logged out and follow the "Login" link in the menu navbar.   
   **ii.** Click the "Reset Password" link underneath the Login form and you will be taken to the reset password page.      
   **iii.** You will be prompted to enter your email into a field and click the "Reset Password" button. You will then be taken to a page that tells you that an instructional email has been sent to your email address.     
   **iv.** Check your email inbox for the instructional email or junk email if it's not immediately in your inbox. Follow the link in the email and you will be taken to the password change form on the site.    
   **v.** Enter your new password and submit it and your password has been changed successfully. Follow the link from the page you are reverted to and Log in to ensure the password change has worked.
   **vi.** To test the form for the new password, enter your old password to ensure that the form won't allow you to submit the same password.

7. As the Administrator of the site, I would like to be able to easily upload new dogs for sale and edit the ads if there is a typo or change to their sale status.  

   **i.** To Log in as the Admin, enter the details: Username - admin , Password - thisismypassword .  
   **ii.** Responding to a user request for a new dog from User Story no. 5, go to the "Dogs for Sale" page and scroll to the bottom and click on the "Add an Ad" button.       
   **iii.** Fill out the relevant details on the ad corresponding to the user's request and submit the ad.   
   **iv.** Respond to the user's request in the comments under their request ad.  


  
   

### Responsiveness
  I have tested out the responsivesness of the website on Google Chrome, Microsoft Edge and Mozilla Firefox using Dev tools, as well as testing it on Safari on various iOS devices.  
  
  The banner hero image reduces in size from desktop to smaller devices so it doesn't take up as much space at the top of the screen and the user doesn't need to scroll as much on mobile devices. 
  
  On mobile view and medium devices, the the advertisement tables (both sale and requests) only show the most relevant information - Ad title, description and the action button to go to the full ad view with the aid of a media query. On larger screen views, more info is available to the user such as the ad seller location, image (if available) and breed. 
  The tests took place on the devices below, both in horizontal and vertical view ports. All buttons and links work on all devices.  
   
    * Small devices - iPhone 6s, iPhone X, Samsung J5, Samsung S9. 
    * Medium devices - iPad, Samsung Tablet. 
    * Large/Extra Large devices - Lenovo ideapad 520, Asus Vivobook, Samsung 49-Inch 4K Ultra HD Smart LED TV.  

### Bugs
  Most of the bugs I encountered while developing this site...
  This produced the following bugs when I asked family and friends to test my site:
  * When I switched from the development stage to hosting the app on Heroku, I had an issue with displaying the images from the advertisements that were hosted on AWS S3 on the site. The static files such as the banner image, the css files and js files were working but when I uploaded an image from the front end forms, the images wouldn't be displayed or be stored in S3. When I uploaded from the admin panel, the file would work but that wouldn't work for the purposes of this project. The fact the admin panel worked for uploading the image files made me aware that the connection between S3 and my project wasn't an issue, it must've been something within my forms.   
  I found the answer in a stackoverflow query [here](https://stackoverflow.com/questions/44489956/amazon-s3-storing-image-files-from-django-dont-upstream-uploaded-images-by). The tutorials that I followed (the Code Institute tutorials and tutorials from [here](https://simpleisbetterthancomplex.com)) helped me to set up saving the information entered by the user on the form but I was missing the "request.FILES" when saving the form data  in the views.py file from the products app. I also added " enctype="multipart/form-data" " to the HTML form. I learned more about the process [here](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html) It was a simple fix in the end but one that stumped me.  
  * I had an issue using my own email as the host email as my google account security settings kept preventing my app from being used as the host. I allowed third party application access on my google account security settings but unless I did that every single time google was still blocking my reset password emails. I consulted the Full-Stack Frameworks channel on Stack and saw that a few other users had set up a new gmail account so their security settings for their personal email wouldn't interfere with the app's email hosting. I set up a new email account and allowed third party apps access and because there was no google account linked to it, it worked.

 

### Validation

  * I have validated my html code through [https://validator.w3.org/](https://validator.w3.org/) and my css code through [http://jigsaw.w3.org/css-validator/](http://jigsaw.w3.org/css-validator/) and no errors have occurred.

## Deployment

The app is deployed to Heroku and can be found at the following link: [https://dog-deal-app.herokuapp.com/](https://dog-deal-app.herokuapp.com/)

To deploy this app:
 
 - Download the repo for my project or clone it using the following method: 
 - Open a new workspace and download the git repository with the following CLI commands:
  ```
  https://github.com/johnnycistudent/dogdeal.git
  ```   
  - This method will put everything into a subfolder so cut and paste the project out of the subfolder and delete the subfolder so all the paths are correct.
  - Create a virtual environment and check the requirements.txt for the necessary packages used in this app and install them via the following command in the CLI:
  ```
  pip3 install -r requirements.txt
  ```   
  - Git init, commit and push your repo to github. 
  - Create a new app in Heroku 
  - Link the github repo to Heroku by going to the deploy tab in Heroku and link your github repo in the app connected to GitHub section. 
  - Enable the automatic deployment in the same tab so everytime you make changes and commit and push to github, it automatically pushes to Heroku too. Make sure it is set to the Master branch.
  - In the resources tab in Heroku, add Postgres to add-ons. 
  - In the Heroku settings tab, enter the following enviromental variables in the config vars:
      - "SECRET_KEY" - used to provide cryptographic signing, and should be set to a unique, unpredictable value. 
      - "STRIPE_PUBLISHABLE" - required by Stripe and provided to you when you set up a Stripe account.
      - "STRIPE_SECRET" - required by Stripe and provided to you when you set up a Stripe account.
      - "DATABASE_URL" - address of the PostgreSQL database. 	
      - "AWS_ACCESS_KEY_ID"	- provides access to static and media files stored in AWS S3 bucket.
      - "AWS_SECRET_ACCESS_KEY" -	provides access to static and media files stored in AWS S3 bucket.
      - "EMAIL_USER" - email address of the host email from which the site sends reset password settings email.
      - "EMAIL_PASSWORD" - email password of the above email to give the app access to the email account.
      - set "DISABLE_COLLECTSTATIC" to "1" - prevents media and static files that are stored on S3 being pushed to Heroku. 
  - Create a file in the top folder of your local environment named "env.py" and copy the above security enviromental variables. Make sure to .gitignore this file so it won't show up on your github repo as it contains sensitive information.
  - type in the following to your CLI:  
  ```python3 manage.py createsuperuser```  
    A super user is then created once you enter in the name, email address and password.
  - Enter the following commands to migrate your models to the new DB:
  ```
  python3 manage.py makemigrations
  ```   
  followed by:
  ```
  python3 manage.py migrate
  ```
  

## Credits
This website was designed by John O'Connor. Stack Overflow, the Code Institute tutors and the Code Institute Full-Stack Frameworks Milestone Project channel were also extremely helpful during the production of this project.

### Content

### Media 

   - The jumbotron banner image is taken from [Pixabay](https://pixabay.com/).  
   
   - The favicon image was generated at [https://favicon.io/favicon-generator/](https://favicon.io/favicon-generator/).
   
   - Any other photos uploaded by Users were sourced by them.


## Acknowledgements

  * [Stack Overflow](https://stackoverflow.com/), [W3Schools](https://www.w3schools.com/) and [Slack](https://slack.com/) were very useful when coming up against problems that many other people had also encountered.
  * I took inspiration from the various mini projects in the Code Institute's Full-Stack Frameworks module and used the code used in those lessons as a starting off point to customise my code on top of their examples.
  * [https://simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com) was very helpful providing many tutorials on a lot of different features of Django. I also used [https://docs.djangoproject.com](https://docs.djangoproject.com) for the likes of pagination and comments.
  * The product view was taken and heavily edited from [this bootsnipp code](https://bootsnipp.com/snippets/orOGB).
  * The shopping cart code was taken and edited from [this nicesnippets code](http://nicesnippets.com/snippet/bootstrap-4-shopping-cart-design-example).
  * 

