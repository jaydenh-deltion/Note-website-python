from flask import Blueprint, render_template 
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') # Define the home route
@login_required # Ensure the user is logged in to access this route
def home():
    return render_template("home.html")