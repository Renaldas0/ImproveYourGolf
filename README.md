# Improve Your Golf

### [Improve Your Golf](https://www.example.com) is a full stack website developed to be a website that takes bookings for golf lessons. The user must create an account to be able to make bookings for classes, then they are able to change or delete their placed bookings.

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
  - Once the user scrolls for better user experience, the navbar is set to always be visible and a background colour appears
  - For extra functionality there is a button which if clicked simply scrolls down to the About Us section
  - Clicking on sections in the navbar scrolls the page down to that desired section
  - Clicking on the heading will also scroll the page back up to the top
  
## Main section
![main-screenshot](https://user-images.githubusercontent.com/97538312/201192933-98a6b956-1bc9-43e9-84d8-8ba22933ffd2.jpg)


- **Classes**
  - The classes section is designed to look different for authenticated users and those who are not logged in
  - If a user is not logged in then a message at the bottom of the class description appears to inform a user they must first login
  - When a user logs in this message disappears and the 'Book Now' button appears
  - The responsive features set the columns to align from 3 across to a 2,1 layout and then in a row formation for mobile devices
  - Each class has a different image to indicate the type of lesson to expect

## Classes when not logged in 
![classes_notauth](https://user-images.githubusercontent.com/97538312/201193183-2252d2ed-a915-4d1d-b734-fa61ae8fb172.jpg)

## Classes to logged in viewers 
![classes_auth](https://user-images.githubusercontent.com/97538312/201193253-d616c879-8851-4726-9fb6-ada64418b095.jpg)


- **Coaches**
  - The coaches section consists of 2 images that show the coaches and a brief description
  - The responsive feature also changes the layout for these 2 divs, making them fall one under the other for smaller devices
![coach-screenshot](https://user-images.githubusercontent.com/97538312/202302482-35e26dd9-6f8f-4402-9230-0fded587fbc0.jpg)



- **Register & Login Forms**
  - When the register or login option is selected by the user, they are redirected to the form page.
  - These forms are of very simplistic design for easy and satisfying user experience.
  - Both forms are designed to look the same and contain the same navbar and footer elements as on the main page.

## Register form
![signup](https://user-images.githubusercontent.com/97538312/204099776-1019a34c-b1ba-4175-a117-291956594794.jpg)

## Sign in form
![sign-in-screenshot](https://user-images.githubusercontent.com/97538312/202302531-b3fa0508-89ad-47df-8140-16c6126b0bef.jpg)

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
   
   ![manage_booking](https://user-images.githubusercontent.com/97538312/204099619-976b5c43-e4fb-4e79-9861-e1c8e164e79a.jpg)

  ![cancel_modal](https://user-images.githubusercontent.com/97538312/204099563-3ec26c06-4a16-43ef-93df-1a145cf7d53b.jpg)


## Bugs encountered
  - Backports.zoneinfo was shown as an error when deploying to Heroku
  - I fixed this by specifying an older python version in a runtime.txt file
  - My csrf token was getting rejected so I addressed this by specifying a trusted url in my settings.py file
  - In manage bookings, the class name does not show up, however it does display in delete bookings.
  
## Unfixed Bugs 
  - If a user makes a booking and their username or email don't match their signup details, the booking is recorded in the database but won't show up for the user in manage bookings.
  - Currently in the manage bookings page, the class name is not showing up. This works in delete booking
  
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
  - I deployed the project to heroku which is a cloud based hosting platform https://www.heroku.com/
  - The database is deployed using ElephantSQL 
  - This is done by creating a new instance on ElephantSQL 
  - Select Table quries in BROWSER and select an option that looks familiar
  - The DATABASE URL is then pasted into heroku config vars and into my env.py file 
  - The code is deployed and pushed to Github which is linked to heroku

## Credits
  - I traced back to the I think therefore I blog project to set up my python files correctly
  - Errors during the build process were fixed with the help of slack community and stackoverflow
  - These helped me find a solution to my backports.zoneinfo issues and csrf token issues.
  
