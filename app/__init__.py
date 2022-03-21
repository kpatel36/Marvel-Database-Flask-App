from flask import Flask
from config import Config

from .auth.authroutes import auth

from .characterapi.charroutes import api

from .models import db, login
from flask_migrate import Migrate

app=Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(auth)
app.register_blueprint(api)


db.init_app(app) 
migrate = Migrate(app,db)

login.init_app(app)
login.login_view='auth.signin'
login.login_message = 'Please sign in to see this page'


from . import routes
from . import models