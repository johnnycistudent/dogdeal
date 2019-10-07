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
  *   **Advertisement Table view** - 
  *   **Full Ad Display** - The full ad view is rendered when 
  *   **User Comments**
  *   **Search bar** - The Search bar is located within the expanded navbar on large screens and also above the Dogs for Sale table display. The results of the user's queries follow best practices of UX design - the user is reminded of their query and informed of the number of results their query has generated. The search submit button can be triggered by the return or enter key on any device that the site is being viewed through.
  *   **User Accounts** - Each user has the ability to ... 
  *   **Login/Registration forms** 
  *   **User Profiles** - The User Profile is used to 
  *   **Shopping Cart/Checkout** - 
  *   **Admin Functions** - ...
  *   **Footer** - The footer features links to the social media accounts of myself, the site developer and my Github profile. 

### Features Left to Implement


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

   **i.** To Log in as the Admin, enter the details: Username - admin , Password - newpassword .
   **ii.** Responding to a user request for a new dog from User Story no. 5, go to the "Dogs for Sale" page and scroll to the bottom and click on the "Add an Ad" button.       
   **iii.** Fill out the relevant details on the ad corresponding to the user's request and submit the ad.   
   **iv.** Respond to the user's request in the comments under their request ad.  


  
   

### Responsiveness
  I have tested out the responsivesness of the website on Google Chrome, Microsoft Edge and Mozilla Firefox using Dev tools, as well as testing it on Safari on various iOS devices.  
  The Recipe cards were designed to help the responsiveness of the site. On mobile view, the screen displays one recipe per column, on medium devices two cards are displayed and then three cards are displayed on anything larger. Bootstrap's grid system was very useful in this regard and meant the only media query I needed for the whole site was for the Admin Area info table.
  The tests took place on the devices below, both in horizontal and vertical view ports. All buttons and links work on all devices.  
   
    * Small devices - iPhone 6s, Samsung J5, Samsung S9. 
    * Medium devices - iPad, Samsung Tablet. 
    * Large/Extra Large devices - Lenovo ideapad 520, Asus Vivobook.  

### Bugs
  Most of the bugs I encountered while developing this site...
  This produced the following bugs when I asked family and friends to test my site:
  * Connecting S3 
  * Password email settings
 
  I solved these problems by...

 

### Validation

  * I have validated my html code through [https://validator.w3.org/](https://validator.w3.org/) and my css code through [http://jigsaw.w3.org/css-validator/](http://jigsaw.w3.org/css-validator/) and no errors have occurred.

## Deployment

The app is deployed to Heroku and can be found at the following link: [https://dog-deal-app.herokuapp.com/](https://dog-deal-app.herokuapp.com/)

  - Download the repo for my project or clone it using the following method: 
  



## Credits
This website was designed by John O'Connor. Stack Overflow, the Code Institute tutors and the Code Institute Full-Stack Frameworks Milestone Project channel were also extremely helpful during the production of this project.

### Content

### Media 

   - The jumbotron banner image is taken from [Pixabay](https://pixabay.com/).  
   
   - The favicon image was generated at [https://favicon.io/favicon-generator/](https://favicon.io/favicon-generator/).
   
   - Any other photos uploaded by Users were sourced by them.


## Acknowledgements

  * [Stack Overflow](https://stackoverflow.com/), [W3Schools](https://www.w3schools.com/) and [Slack](https://slack.com/) were very useful when coming up against problems that many other people had also encountered.
  * [https://simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com) was very helpful providing many tutorials on a lot of different features of Django. I also used [https://docs.djangoproject.com](https://docs.djangoproject.com) for the likes of pagination and comments.
  * The product view was taken and heavily edited from [this bootsnipp code](https://bootsnipp.com/snippets/orOGB).
  * The shopping cart code was taken and edited from [this nicesnippets code](http://nicesnippets.com/snippet/bootstrap-4-shopping-cart-design-example).
  * 

