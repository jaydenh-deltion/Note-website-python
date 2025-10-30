from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>Login Page</h1>"

@auth.route('/logout')
def logout():
    return "<p>Logout Page</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"