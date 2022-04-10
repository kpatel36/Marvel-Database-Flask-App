from functools import wraps
import secrets
from flask import request, jsonify, json

from app.models import Character, User


def token_required(flask_function):
    @wraps(flask_function)
    def decorate_function(*args,**kwargs):
        token = request.headers.get('x-access-token')
        # if no token provided
        if not token:
            return jsonify ({'Access denied':'No API Token provided - please register an account and request an API token."'}), 401
            # status code of 401 - no token, we dont know who they are
        # token provided but not valid 
        if not User.query.filter_by(api_token=token).first():
            # query database to see if User's token matches the token given
            return jsonify ({'Access denied':'Invalid API tone-please register an account and request an API token'}), 403
        return flask_function(*args,**kwargs)
    return decorate_function