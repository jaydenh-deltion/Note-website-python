from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login') # Define the login route
def login():
    return "<h1>Login Page</h1>"

@auth.route('/logout')# Define the logout route
def logout():
    return "<p>Logout Page</p>"

@auth.route('/sign-up') # Define the sign-up route
def sign_up():
    return "<p>Sign Up</p>"