# NetworkEZ

NetworkEZ is a communication platform built for students. During remote classes and lecture halls with hundreds of people, students often struggle with finding buddies to study with, partners to work with, and finding friends with similar interests. NetworkEZ matches students with their fellow classmates to bring together entire class sections and achieve the superior goal of learning. It allows students to see other students in their classes or have the same hobbies, and provides their social media for further exchanges to be made. 

# Technical Architecture

NetworkEZ uses a HTML frontend and uses CSS for styling, Django backend with Python, as well as a SQLite database instance.

Django handles the data posted from the HTML frontend as it handles form requests that are created upon registration, including names, classes, hobbies, etc. Matching is also done based upon the passed on data in the backend using string similarity sorting and matching. The Django backend interacts with the SQLite database and passed that data into the HTML front end as list to be displayed. User data includes registration data like usernames, passwords, emails alongside individual majors and hobbies, while student data includes other students' majors, hobbies, interests. We used Pylint as the linter for code style and Pytest to write unit tests. 

# Components

## Login and User Registration

To begin, the login and user registration pages are at the forefront of the web app. Here users can input their username, password, and email to register. The user’s username, passwords, and emails are stored in a SQLLite database.

## Navigation Bar

The navigation bar uses the django.urls that were initliazed in the backend to navigate throughout different pages. The pages include a list of student profiles, your own profiles, students that share a hobby and classes with you.

## Data Display Pages

The user can see a list of student profiles, your own profiles, students that share a hobby and classes with you with information such as people’s name, major, social media, and more. 




## Diagram




# Group Members

Jalen Xing created the backend for the project that allows the user to enter their information and store it into the database, match the student’s based on their hobbies and shared classes, created the navigation bar that allows website navigation between the various pages, and created the front-end. 

Aditya Matiwala primarily worked on the front-end of the project, initially creating different components in React to display matches between users, pivoting to pure HTML and CSS instead.

# Installation 

Git clone https://github.com/CS222-UIUC/course-project-group-7.git

python3 -m pip install django

python3 manage.py runserver

Go to link http://127.0.0.1:8000/login/

# Acknowledgements

Thanks a lot to our mentor Vansh for helping us throughout the project and giving us great feedback. 
