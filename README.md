# xdata
A Django web application to manage and display a list of users, along with their TTS enabled status. The application allows for adding new users, editing, deleting, and adding CSV data for existing users.

Features
User Registration: Register new users with a unique username and specify if TTS is enabled.
User Management: Edit, delete, or add CSV data for registered users.
Responsive UI: Clean and simple user interface that works on both desktop and mobile devices.

Prerequisites
Python 3.x
Django (Specify the version you used, e.g., Django 3.2)

Setup and Installation
# git clone git@github.com:tmetreveli/xdata.git
# cd xdata

# python -m venv venv
# source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# pip install -r requirements.txt

# python manage.py migrate

# python manage.py runserver

# Now, open your browser and go to http://127.0.0.1:8000/ to access the application.

Usage
To register a new user, fill in the "Username" field and check the "TTS Enabled" box if required, then click "Register".
To edit, delete, or add CSV data for a user, click the corresponding button in the "Actions" column of the user list.

