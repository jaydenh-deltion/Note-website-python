from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views # Import the views blueprint
    from .auth import auth # Import the auth blueprint

    app.register_blueprint(views, url_prefix='/') # Register the views blueprint
    app.register_blueprint(auth, url_prefix='/') # Register the auth blueprint

    return app  
