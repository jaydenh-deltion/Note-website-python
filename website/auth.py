from flask import Blueprint,render_template

auth = Blueprint('auth', __name__)

@auth.route('/login') # Define the login route
def login():
    return render_template("login.html")

@auth.route('/logout')# Define the logout route
def logout():
    return "<p>Logout Page</p>"

@auth.route('/sign-up') # Define the sign-up route
def sign_up():
    return render_template("sign_up.html")