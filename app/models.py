# this models.py file is responsible for everything database
# primarily instantiation of ORM and create of database models (tables/entities)

# import ORM
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin 


# create instance of ORM
# practice to refer to database as db in instantiation
db = SQLAlchemy()

login=LoginManager()

# necarry function for our login manager
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id) 


from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4


# create database model 
class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    displayname = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    data_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, username, email, displayname, password):
        self.username = username
        self.email = email.lower()
        self.displayname = displayname.lower()
        self.password = generate_password_hash(password)
        self.id = str(uuid4())

# new DB model for Marvel Characters
# @ start - only name, description, comics # and ID not nullable, rest can have constraints added later
class Character(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    comics_number = db.Column(db.Integer(), nullable=False)
    superpower = db.Column(db.String(100))
    alias = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # user submitting a POST request to create a new character will be sending a python dictionary that you'll use to make your object
    def __init__(self,dict):
        """
        expected dict structure:
        {
            'name': <str>,
            'description':<str>
            'comics_number':<int>
            'superpower':<str>
            'alias':<str>,
            'datecreated':<str>
        }
        """
        self.name = dict['name']
        self.description = dict['description']
        self.comics_number = dict['comics_number']
        self.superpower = dict.get('superpower')
        self.alias = dict.get('alias')
        self.id = str(uuid4())


    def to_dict(self):
        # translate object into dictionary
        # take self and return a dictionary containing K'V pair for each attribute
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'comics_number':self.comics_number,
            'superpower' : self.superpower,
            'alias': self.alias 
        }