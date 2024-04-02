# Basic Flask Note-Taking Web App

## Introduction

This project is a simple Flask web application that provides a platform for users to sign up, log in, create notes, and delete them. The application utilises Flask blueprints to structure the views and authentication processes, and integrates SQLAlchemy for database interactions.

## Application Structure

### `__init__.py`

- Initialises the Flask app and configures key components such as the database (SQLite), the login manager, and the application secret key.
- Registers blueprints for different sections of the application (authentication and views).
- Defines the `create_database` function which conditionally creates a new database file.

### `auth.py`

- Contains routes for user authentication, including sign-up and login functionalities, using Werkzeug for password hashing and verification.
- Uses Flask-Login for handling user session management after authentication.

### `models.py`

- Defines the database models `User` and `Note`, with `User` being integrated with Flask-Login through the `UserMixin`.
- `User` model includes email, password, and a relation to the `Note` model, representing the user's notes.
- `Note` model contains a text field, a timestamp, and a foreign key to the `User` model.

### `views.py`

- Handles routes for the main application views, requiring login to access.
- Includes a route for the homepage where notes can be created and deleted.
- Implements the creation of new notes and deletion of existing notes with SQLAlchemy ORM.

## Technologies Used

- **Flask**: Micro web framework for Python.
- **SQLAlchemy**: SQL toolkit and ORM for Python.
- **SQLite**: Lightweight disk-based database.
- **Flask-Login**: Flask extension for managing user sessions.
- **Werkzeug**: Comprehensive WSGI web application library.

## Running the Application

1. Install all the required Python packages by running:
pip install -r requirements.txt
2. To start the server, run:
flask run
3. Access the application in your web browser at `localhost:5000`.

## Learning Outcomes

- Learnt how to set up a Flask application with modular architecture using blueprints.
- Understood user authentication using Flask-Login and password hashing with Werkzeug.
- Managed database schemas and interactions with SQLAlchemy ORM.
- Utilised Flask templates to render the frontend while sending and receiving data from the backend.
- Gained experience in managing user sessions and protecting routes with login requirements.

## Final Thoughts

This project was an excellent introduction to full-stack web development with a focus on the backend. Building this application has solidified my understanding of web frameworks, ORM, and user authentication.
