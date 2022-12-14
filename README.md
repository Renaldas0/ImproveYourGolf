# Improve Your Golf

### [Improve Your Golf](https://improve-your-golf.herokuapp.com/) is a full stack website developed to be a website that takes bookings for golf lessons. The user must create an account to be able to make bookings for classes, then they are able to change or delete their placed bookings.

![responsive](https://user-images.githubusercontent.com/97538312/203823455-a1f9d1d8-3687-4b54-a6a1-2b5d1a8e8026.jpg)
  
##  **Purpose**
  - The purpose of this website is to provide information about our studio and encourage golfers of all age groups to try out our lessons that will improve their golf.

## Agile Methodology
  - Use of Github Issues and User Stories
  ![user_stories](https://user-images.githubusercontent.com/97538312/204099265-eb4c50b9-ed7d-4d70-b27c-5a2d807fd17e.jpg)


## User Stories

### User Stories that have been achieved for this deadline in this project:

| id  |  Content | How was it satisfied
| ------ | ------ | ------ |
|  [#1](https://github.com/Renaldas0/ImproveYourGolf/issues/1) | As a site user I can view the layout of the website so that everything is easy to find on the page and I know what it is about. | Webpage |
|  [#2](https://github.com/Renaldas0/ImproveYourGolf/issues/2) | As a site user I can use the navbar so that I can easily navigate through the website with the navbar. | Webpage |
|  [#3](https://github.com/Renaldas0/ImproveYourGolf/issues/3) | As a site user I can see the footer clearly so that I can see any social media links clearly incase I wish to follow up there. | Webpage |
|  [#4](https://github.com/Renaldas0/ImproveYourGolf/issues/4) | As a site user I can read about classes so that I can get information about each class offered. | Class Information |
|  [#5](https://github.com/Renaldas0/ImproveYourGolf/issues/5)| As a site user I can read about the scheduled classes so that I know which class is the best to book according to my schedule. | Class Information |
|  [#6](https://github.com/Renaldas0/ImproveYourGolf/issues/6) | As a site user I can check the availability of classes so that I know if the class i'm interested in is available. | Booking |
|  [#7](https://github.com/Renaldas0/ImproveYourGolf/issues/7) | As a site user I can book a class to my schedule so that I can get a reserved place for a lesson. | Booking |
|  [#8](https://github.com/Renaldas0/ImproveYourGolf/issues/8)| As a site user I can cancel my booking so that my place is not reserved in case I can't make it to the class. | Manage Booking |
|  [#9](https://github.com/Renaldas0/ImproveYourGolf/issues/9) |As a site user I can login to my account so that my details are saved and I can place a booking faster. |  Login/SignUp |
|  [#11](https://github.com/Renaldas0/ImproveYourGolf/issues/11) | As a site user I can contact a teacher so that I can ask questions regarding these lessons. |  Webpage |
|  [#12](https://github.com/Renaldas0/ImproveYourGolf/issues/12) | As a site admin I can add social media platforms so that students can follow us on other platforms to better understand our goals. | Webpage |
|  [#13](https://github.com/Renaldas0/ImproveYourGolf/issues/13) | As a site admin I can edit classes so that I can adjust bookings personally if requested by a user. |  Admin |
|  [#14](https://github.com/Renaldas0/ImproveYourGolf/issues/14) | As a site user I can block off bookings so that the class isn't overbooked | Admin |
|  [#15](https://github.com/Renaldas0/ImproveYourGolf/issues/15)| As a site admin I can approve a booking so that I can control how many people book for the class and see who places the booking. | Admin |
|  [#17](https://github.com/Renaldas0/ImproveYourGolf/issues/15)| Develop the website to be responsive and look aesthetic on all devices. | Webpage |

### User stories that are planned for next deployment

| id  |  Content | 
| ------ | ------ |
|  [#10](https://github.com/Renaldas0/ImproveYourGolf/issues/10) | As a site admin I can have past students post their review so that any upcoming students can see if this class is effective. |
|  [#18](https://github.com/Renaldas0/ImproveYourGolf/issues/18) | As a user I can change my password incase I have forgotten my password or feel it has been discovered by someone else|
|  [#19](https://github.com/Renaldas0/ImproveYourGolf/issues/19) | Style the error pages such as the 404, 403, 500 pages so they look a little more appealing to cancel out the inconvenience a touch.|

---
## **Features**

- **User Features** 
  - Fully functioning front end website for users to get information on about the lessons
  - Ability to register an account and login/logout.
  - Ability for users to place bookings for their desired class
  - Ability for users to change or cancel their bookings
  - The layout of certain sections changes, dpending if a user is logged in or not.
  - Fully responsive design using bootstrap and media queries for user on all devices.

- **Admin Features**
  - As an admin only I have the ability to login to the admin panel
  - Admin is able to see all placed reservations and control them
  - Admin is able to see all customer input details
  - Admin can see who placed the reservations by their login details
  - Most importantly the admin can update or delete all reservations

- **Site Features**
  - The site is developed to be a single scroll page except for the register and login forms
  - The main section loads up with an image displaying the theme of the website (golf) and the title clearly visible to users
  - The navbar is compact into a hamburger menu icon and is transparent if the page is at the complete top
  - Once the user scrolls for better user experience, the navbar is set to always be visible and a background colour appears using JavaScript
  - For extra functionality there is a button which if clicked simply scrolls down to the About Us section
  - Clicking on sections in the navbar scrolls the page down to that desired section
  - Clicking on the heading will also scroll the page back up to the top
  
## Main section
![main-screenshot](https://user-images.githubusercontent.com/97538312/201192933-98a6b956-1bc9-43e9-84d8-8ba22933ffd2.jpg)
  - The landing page is designed to immediately inform a user that they are on a golf website
  - Provide an easy UI and UX with it's easy to read design
  - The button in the middle takes the user down to the next section

## Navbar to not logged in users 
  - Log in and register options are available
  - Manage bookings does not show up 
  - Log out option is not shown
  
![nav_not_logged_in](https://user-images.githubusercontent.com/97538312/204134958-fe247587-a0fe-441e-afae-74adcf072acd.jpg)

## Navbar to logged in users
  - Option to make a booking
  - Option to manage bookings
  - Login and Register are now hidden
  - Logout option is visible
  
![logged_in_nav](https://user-images.githubusercontent.com/97538312/204134974-443be7a9-cb17-4560-91aa-b48721dd5ceb.jpg)

## About Us
![about-us](https://user-images.githubusercontent.com/97538312/204131322-e8051a0d-a255-43f4-950d-f753532350f2.jpg)
  - In this section a user is informed about the mission of the ImproveYourGolf company


- **Classes**
  - The classes section is designed to look different for authenticated users and those who are not logged in
  - If a user is not logged in then a message at the bottom of the class description appears to inform a user they must first login
  - When a user logs in this message disappears and the 'Book Now' button appears
  - The responsive features set the columns to align from 3 across to a 2,1 layout and then in a row formation for mobile devices
  - Each class has a different image to indicate the type of lesson to expect

## Classes when not logged in 
![classes_notauth](https://user-images.githubusercontent.com/97538312/201193183-2252d2ed-a915-4d1d-b734-fa61ae8fb172.jpg)

## Classes to logged in viewers 
  - The book now button is shown
  
![classes_auth](https://user-images.githubusercontent.com/97538312/201193253-d616c879-8851-4726-9fb6-ada64418b095.jpg)


- **Coaches**
  - The coaches section consists of 2 images that show the coaches and a brief description
  - The responsive feature also changes the layout for these 2 divs, making them fall one under the other for smaller devices
![coach-screenshot](https://user-images.githubusercontent.com/97538312/202302482-35e26dd9-6f8f-4402-9230-0fded587fbc0.jpg)

  - Responsive layout
  
![coaches-responsive](https://user-images.githubusercontent.com/97538312/204131454-abd62b24-d1ee-4b00-9c17-4d1206b0a69a.jpg)

- **Register & Login Forms**
  - When the register or login option is selected by the user, they are redirected to the form page.
  - These forms are of very simplistic design for easy and satisfying user experience.
  - Both forms are designed to look the same and contain the same navbar and footer elements as on the main page.

## Register form
![signup](https://user-images.githubusercontent.com/97538312/204099776-1019a34c-b1ba-4175-a117-291956594794.jpg)

## Sign in form
![sign-in-screenshot](https://user-images.githubusercontent.com/97538312/202302531-b3fa0508-89ad-47df-8140-16c6126b0bef.jpg)

## Sign out
![sign_out](https://user-images.githubusercontent.com/97538312/204134892-8879b46d-5a4c-4626-bde8-5c34179e3c11.jpg)


## Booking
  - The booking system required a database to store in formation. For this 3 models were created. They store, Customer, Classes and the Booking details.
  - The booking page consists of a form which is made using crispy forms
  - The user must input their name, email, requested class and requested date
  - Once this is done if the fields are correct the form is recorded in the database
  - When booking, a user must enter the exact same username and email they used for signup or the booking may fail
![booking-page](https://user-images.githubusercontent.com/97538312/203824345-9ed984e1-9236-43f5-b7b9-35d97e2bd7ae.jpg)
  - The use of a calendar with the help of Jquery is in place for easy date selection 
  ![calendar](https://user-images.githubusercontent.com/97538312/204099599-90ea3c12-3f52-48d8-8dac-d4f8b5a07831.jpg)


## Manage Bookings
  - Users can see their made bookings in the manage bookings section
  - If no bookings are reorded by the user, they are redirected to the booking page
  - When a user wants to delete their booking an extra modal pops up to confirm this 
  - The bookings are displayed in Rows and 2 bookings show up per row
  ![booking_display](https://user-images.githubusercontent.com/97538312/204134931-d87036da-f066-44c6-823b-433af0dd653f.jpg)

  
### Manage booking layout
   ![manage_booking](https://user-images.githubusercontent.com/97538312/204099619-976b5c43-e4fb-4e79-9861-e1c8e164e79a.jpg)
### Edit booking layout 
![edit_booking](https://user-images.githubusercontent.com/97538312/204131567-1cabfcbb-4d2d-473e-9b91-c6df465f3ae7.jpg)

### Cancel Booking layout
![cancel-booking](https://user-images.githubusercontent.com/97538312/204131623-129f9ac8-a66d-4e89-b6b6-00edefb75b58.jpg)
### Cancellation modal to confirm
  ![cancel_modal](https://user-images.githubusercontent.com/97538312/204099563-3ec26c06-4a16-43ef-93df-1a145cf7d53b.jpg)


## Bugs encountered
  - Backports.zoneinfo wouldn't build wheels and was shown as an error when deploying to Heroku and therefore the deployment would fail
  - I fixed this by specifying an older python version in a runtime.txt file which was suggested by heroku
  
  - My csrf token was getting rejected so I addressed this by specifying a trusted url in my settings.py file
  - In manage bookings, the class name does not show up, however it does display in delete bookings.

  - Static files would not load on heroku but everything was fine on my live server.
  - This issue was fixed by adding Cloudinary details separately instead of a Cloudinary url even though that is far more practical.
  - The final fix attempted was to set debug to False and this instantly loaded up all static files.
  
## Unfixed Bugs 
  - If a user makes a booking and their username or email don't match their signup details, the booking is recorded in the database but won't show up for the user in manage bookings.
  - Currently in the manage bookings page, the class name is not showing up. This works however in delete booking
  ![booking-error](https://user-images.githubusercontent.com/97538312/204110421-f770f5b9-f1c4-4eab-8b38-67b2b545c4fa.jpg)
  
  - I am also getting an error in the console in developer tools for alert.js JavaScript. This does not seem to cause any issues in the website.
  
  ![javascript_error](https://user-images.githubusercontent.com/97538312/204158459-8bc63104-7e62-4f8f-bb34-ccd9bcbae83f.jpg)


  
## Testing 
- For the testing process I used print statements and kept running the code after a new function was added which was noticeable when run
- I wrote code for the urls, models and views in tests.py
- Verified the HTML using the W3C HTML validator and all tests passed : https://validator.w3.org/
- Verified CSS using the Jigsaw w3 css validator to confirm all css is valid : https://jigsaw.w3.org/css-validator/
- Tested the python code by running it through PEP8 online :  http://pep8online.com/
- JsHint was used to check JavaScript code : https://jshint.com/
- The only errors were to indicate that the line is too long
- I manually tested that errors in the form fields show up
- Tested that messages get displayed when Logging in, making a booking, editing bookings, deleting bookings and signing out.

## Message Testing
![messages](https://user-images.githubusercontent.com/97538312/204099520-05e868bd-7f8e-4866-92cc-5303c27568e2.jpg)
![cancelled-message](https://user-images.githubusercontent.com/97538312/204099539-12e19193-ee4f-47c0-b3a4-81b10b902ab0.jpg)

### Date in the past
![booking_past_date](https://user-images.githubusercontent.com/97538312/204134911-5242cde1-407d-416c-808e-b3649726f0f8.jpg)

## Email field testing 
![email_field_test](https://user-images.githubusercontent.com/97538312/204099630-8446fcaa-fc3a-42c9-a040-fe2ebcc00e19.jpg)

## Lighthouse test 
![lighthouse](https://user-images.githubusercontent.com/97538312/204099655-1f7ccfd5-edce-49d2-9a56-dc051040ef09.jpg)

## Design
 **The website was designed using Photoshop**
 - Please note that the final product does differ from the early stage mockups
 
 ## Main page
![main-design](https://user-images.githubusercontent.com/97538312/204100537-e8084126-d4db-4596-a682-8e4e0f2b0353.jpg)
## About us
![goal-design](https://user-images.githubusercontent.com/97538312/204100539-42e5f141-5d0a-4a2f-b98d-0fac17ed2b0a.jpg)
## Classes
![classes-deisign](https://user-images.githubusercontent.com/97538312/204100541-4dde3d78-0f31-40eb-ab3c-727c529fd0c7.jpg)
## Register form
![register-design](https://user-images.githubusercontent.com/97538312/204100548-2a37501b-e9dd-4029-bce5-3f114536f84b.jpg)



## Deployment 
  ### Heroku 
  - I deployed the project to heroku which is a cloud based hosting platform https://www.heroku.com/
    - Log in to Heroku
    - Select `New` and create a new app
    - Create an app name (as similar to repo name as possible)
    - Select a Region (Europe for me)
    - Click on `Create app`
  - Heroku took care of the config variables such as : DATABASE_URL, SECRET_KEY and CLOUDINARY_URL
  ### Elephant SQL
  - The database is deployed using ElephantSQL : https://www.elephantsql.com/
    - This is done by creating a new instance on ElephantSQL 
    - Select Table quries in BROWSER and select an option that looks familiar
    - The DATABASE URL is then pasted into heroku config vars and into my env.py file 
  ### Github & Gitpod
  - The code institute full template is used for setting up this project on gitpod
  - When making a new repository
    -  Click `No Template` button
    -  Select the desired template
    -  Add a repository name
    -   To create a Gitpod workspace you then need to click `Gitpod`
    -   This will then start to build a workspace
  - The code is deployed and pushed to a Github branch which is then linked to heroku and set to automatically deploy with every push
  ### Cloudinary
  - Static files and images are hosted on Cloudinary : https://cloudinary.com/
  - This is done by adding all images to cloudinary and linking my Cloud name, API key and API secret to heroku and env.py file

## Credits
  - I traced back to the "I think therefore I blog" project to set up my python and Django files correctly
  - This also helped a lot when building my models and views
  - Errors during the build process were fixed with the help of slack community, Tutor support and stackoverflow
  - Stackoverflow suggested the use of runtime.txt and that helped me find a solution to my backports.zoneinfo issues.
  - The csrf token issue was also solved with the help of stackoverflow.
  - Tutor support helped me discover why my static files were not loading
  
