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