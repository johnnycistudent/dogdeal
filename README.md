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

The primary functions are represented in the Navbar links; Dogs for Sale, Dogs Wanted, User Profile, the Shopping Cart, the search function and the Log Out function. 

The Dogs for Sale display page is the home page as it is the main focus of the website and can be accessed by clicking on the site logo "DogDeal" in the top left hand corner of the navbar. Each ad is accessible through a button on the ad table display. The Admin can access the "Add an Ad" feature from this page to add more ads to the database.

In an individual Dog for Sale page, the user can add any number of dogs to their shopping cart. The user can access their cart from the Navbar where they will see the number of "products" currently in their cart beside the cart icon in the Navbar. The user can then purchase their dogs from their cart from the checkout once the cart is accessed.

The Dogs Wanted display page has the same format as the Dogs for sale display table, with a link to each ad linked within the table. The user can also add their own request through the "Request a Dog" button underneath the Dogs Wanted table. This button will bring the user to a form to add their own requests for dogs from the site.

Once a "Request a Dog" ad is submitted, the user's ad is rendered and they or other users can comment on it below the ad. 

The user can access their profile and log out of the site from the Navbar.

#### Surface
*What will the finished product look like?*
*What colours, typography and design elements will be used?*

I have previously used Bootswatch in other projects and find their themes to be very useful so I used their Simplex theme for this project. The mostly white background contrasts well with the red, blue and purple detailing such as on buttons and also allows the black text to stand out. 

The banner/jumbotron image is a nice photo of a Jack Russell terrier's face with it's nose in the foreground and adds character to the site. 

The font used on the logo for the site is Lato from Google fonts and the icons used through the site are from FontAwesome. 


## User Stories

  **1.** As a non-registered user, I would like 
  
  **2.** As a registered or non-registered user, I would like
  
  **3.** 
  
  **8.** As the Administrator of the site, I would like to be able to see the vital statistics of the site in one comprehensive and interactive list. i.e. how many recipes there currently are, how many users, how many deleted recipes etc. 
  
  **9.** As the Administrator of the site, I would like to restore a recipe I deleted previously to the active recipe collection. 

                


## Wireframes

As mentioned in the [Skeleton](#skeleton) above, here are the wireframes created and edited during the production of the site.  

 * [Mobile Wireframes](https://github.com/johnnycistudent/dogdeal/blob/master/static/media/FSF%20Mobile%20wireframes.pdf)
 * [Desktop Wireframes](https://github.com/johnnycistudent/dogdeal/blob/master/static/media/FSF%20Desktop%20wireframes.pdf)



## Features

### Existing Features

  *   **Navbar** - The Navbar offers an easy navigational view through the site for both non-registered and registered users and is always available to act as a reference point for any user not necessarily sure of their whereabouts on the site. 
  *   **Intro Page** - The Intro Page welcomes new Users to the site with a brief explainer and offers three options - Browse Recipes, Log in or Create an Account. 
  *   **Search bar** - The Search bar on the Browse Recipes page is designed to match the text query of the user. The results of the user's queries follow best practices of UX design - the user is reminded of their query and informed of the number of results their query has generated. The search submit button can be triggered by the return or enter key on any device that the site is being viewed through.
  *   **Full Ad Display** - The full ad view is rendered when 
  *   **User Accounts** - Each user has the ability to create their own account which enables them to access a wider array of features on the website such as saving(favouriting), editing, deleting and creating recipes. The User is required to enter a Username, Email Address and Password. Their password is hashed on entry and not stored in plain text thanks to the werkzeug library. The password cannot be seen even when viewing the MongoDB on Atlas. All usernames and email addresses must be unique.    
  *   **User Profiles** - The User Profile is used to view your own recipes as well as other user's recipes. The "My Recipes" link in the navbar allows the user to view the recipes they themselves have added. As mentioned in the Full Recipe Display feature above, if a user wants to view another user's profile, they can follow the link by clicking on the name of the recipe author displayed on the full recipe display. 
  *   **Admin Area** - The Admin Area allows the site Administrator to view a list of information/statistics about each collection in the database. The information includes the total number of documents in each collection, each document and a link to said document as well as the date each document was created. This view also links each user profile as well as offering a path to the deleted recipe display, where the deleted recipe can be restored. 
  *   **Footer** - The footer features links to the social media accounts of myself, the site developer and my Github profile. 

### Features Left to Implement

  * Comments section on recipes
  * User ability to upload their own photos
  * User ability to edit their own profile, change username or email and reset their password

## Technologies Used
* [HTML](https://www.w3schools.com/html/html5_intro.asp) - [CSS](https://www.w3schools.com/css/) - [Javascript](https://www.w3schools.com/js/) - [JQuery](https://jquery.com/) - [FontAwesome](https://fontawesome.com/) - [Google Fonts](https://fonts.googleapis.com/css?family=Muli:400,700i|Poppins:400,400i)

    This site's front end is written using HTML, CSS, Javascript and Jquery. It features iconography from FontAwesome's library and fonts from Google Fonts. 

* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - [Bootswatch](https://bootswatch.com/)

    This website uses Bootstrap 4.1.3 and Bootswatch for its framework and for responsivesness. 

* [AWS Cloud9](https://aws.amazon.com/cloud9/)

    The IDE this website was written on is AWS Cloud9. 

* [GitHub](https://github.com) - [Heroku](https://www.heroku.com/) - [Django](https://www.djangoproject.com/) - [Python](https://www.python.org/)

    This website's Git repository is published on GitHub and is deployed on Heroku. The backend code is written in Python and Django is used as the Python web framework and uses Jinja templates.
    
* [PostgreSQL](https://www.postgresql.org/)   

    PostgreSQL is the NoSQL database used for this site.  

    

## Testing

### Testing User Stories

1. As a non-registered user, I would like to browse 

   **i.** From the opening page 
   **ii.** 
   **iii.** 
  
2. As a registered or non-registered user, I would like 

   **i.** As a non-registered or registered user, 
   **ii.** 
   **iii.** As a registered user,
  
3. As a registered or non-registered 

   **i.** Navigate to
   **ii.** 
   **iii.** 

  
4. As a registered or non-registered user, I would like 

  
   

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
  * User search queries 
  * When making the function that remove
 
  I solved these problems by...

 

### Validation

  * I have validated my html code through [https://validator.w3.org/](https://validator.w3.org/) and my css code through [http://jigsaw.w3.org/css-validator/](http://jigsaw.w3.org/css-validator/) and no errors have occurred.

## Deployment

The app is deployed to Heroku and can be found at the following link: []()

  - Download the repo for my project or clone it using the following method: 
  



## Credits
This website was designed by John O'Connor. Stack Overflow, the Code Institute tutors and the Code Institute Full-Stack Frameworks Milestone Project channel were also extremely helpful during the production of this project.

### Content

### Media 

   - The  

   - The backup photo for recipes without a photo and the Intro page background were taken from a free search of [Pixabay](https://pixabay.com/).  
   
   - The favicon image was found at
   
   - Any other photos uploaded by Users were sourced by them.


## Acknowledgements

  * [Stack Overflow](https://stackoverflow.com/), [W3Schools](https://www.w3schools.com/) and [Slack](https://slack.com/) were very useful when coming up against problems that many other people had also encountered.
  * 

