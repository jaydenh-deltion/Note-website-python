from flask import Blueprint,render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # Define the login route
def login():
    return render_template("login.html", boolean=True)


@auth.route('/logout')# Define the logout route
def logout():
    return "<p>Logout Page</p>"

@auth.route('/sign-up', methods=['GET', 'POST']) # Define the sign-up route
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # add user to database
            pass

    return render_template("sign_up.html")