from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func # func is just used to get current date and time

# Flask-login requires a User model with the following properties:

# has an is_authenticated() method that returns True if the user has provided valid credentials
# has an is_active() method that returns True if the user’s account is active
# has an is_anonymous() method that returns True if the current user is an anonymous user
# has a get_id() method which, given a User instance, returns the unique ID for that object

# UserMixin class provides the implementation of this properties. 
# Its the reason you can call for example is_authenticated to check if login credentials provide is correct or not instead of having to write a method to do that yourself.

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # add the note to all the notes under a user

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # one to many relationship: one user can have many notes

