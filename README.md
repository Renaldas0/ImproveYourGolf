# Improve Your Golf

### [Improve Your Golf](https://www.example.com) is a full stack website developed to be a website that takes bookings for golf lessons. The user must create an account to be able to make bookings for classes, then be able to change or delete their placed booking.

![responsive](https://user-images.githubusercontent.com/97538312/203823455-a1f9d1d8-3687-4b54-a6a1-2b5d1a8e8026.jpg)


## **Features**

- **User Features** 
  - Fully functioning front end website for users to get information on about the lessons
  - Ability to register an account and login/logout.
  - Ability for users to place bookings for their desired class
  - Ability for users to change or cancel their bookings
  - The layout of certain sections changes, dpending if a user is logged in or not.

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
## Sign in form
![sign-in-screenshot](https://user-images.githubusercontent.com/97538312/202302531-b3fa0508-89ad-47df-8140-16c6126b0bef.jpg)

## Booking
  - The booking page consists of a form which is made using crispy forms
  - The user must input their name, email, requested class and requested date
  - Once this is done if the fields are correct the form is recorded in the database
![booking-page](https://user-images.githubusercontent.com/97538312/203824345-9ed984e1-9236-43f5-b7b9-35d97e2bd7ae.jpg)

## Manage Bookings
  - Users can see their made bookings in the manage bookings section
  - If no bookings are reorded by the user, they are redirected to the booking page

## Bugs encountered
  - I encountered a bug with the bookings when selecting a date
  - The date selected on a calendar was coming up as an invalid date and when debugging it was shown as an incorrect format
  - The format was coming up as 'yyyy-mm-dd' even though I specified to record it as '%d-%m-%Y' in my views.py file
  - Backports.zoneinfo was shown as an error when deploying to Heroku
  - I fixed this by specifying an older python version in a runtime.txt file
  - My csrf token was getting rejected so I addressed this by specifying a trusted url in my settings.py file

## Unfixed Bugs 
  -
  
## Testing 
- For the testing process I used print statements and kept running the code after a new function was added which was noticeable when run
- I wrote code for the urls, models and views in tests.py
- Verified the HTML using the W3C HTML validator and all tests passed
- Verified CSS using the Jigsaw w3 css validator to confirm all css is valid
- Tested the python code by running it through PEP8 online :  http://pep8online.com/
- The only errors were to indicate that the line is too long
- I manually tested that errors in the form fields show up
- Tested that messages get displayed when Logging in, making a booking, editing bookings, deleting bookings and signing out.

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
  
