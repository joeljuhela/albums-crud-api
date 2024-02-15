from functools import wraps
import jwt

from flask import request
from flask import current_app

from .models import User


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        token = None
        if auth_header:
            token = auth_header.split(" ")[1]
        
        if token:
            try:
                payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
                username = payload['sub'] 
            except jwt.InvalidTokenError:
                return {'message': 'Unauthorized'}, 401
            except jwt.ExpiredSignatureError:
                return {'message': 'Token expired'}, 401 
                
            return f(*args, **kwargs)
        
        return {'message': 'Unauthorized'}, 401

    return decorated