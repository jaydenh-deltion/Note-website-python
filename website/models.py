from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) ## Unique identifier for each note
    data = db.Clumn(db.String(10000)) ## Content of the note
    date = db.Column(db.DateTime(timezone=True), default=func.now()) ## Timestamp of when the note was created
    user_id = db.Column(db.Integer, db. ForeinKey('user.id')) ## Foreign key to link the note to a specific user


class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) ## Unique identifier for each user
    email = db.Column(db.String(150), unique=True) ## User's email address
    password = db.Column (db.String(150)) ## User's password
    first_name = db.Column(db.String(150)) ## User's first name
    notes = db.relationship('Note') ## Relationship to link user to their notes
