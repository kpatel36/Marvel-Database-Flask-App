from flask import Flask
from config import Config

from .auth.authroutes import auth

app=Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(auth)

from . import routes