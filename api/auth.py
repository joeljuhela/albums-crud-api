import jwt
from datetime import datetime, timedelta

from flask import Blueprint, request, current_app

from .models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return {"message": "Unauthorized"}, 401
    
    user = User.query.filter(User.username==auth.username).first()
    
    if user.check_password(auth.password):
        token = jwt.encode({'sub': user.username, 'exp': datetime.utcnow() + timedelta(hours=3)}, current_app.config['SECRET_KEY'], 'HS256')
        return {'token': token}
    else:
        return {"message": "Unauthorized"}, 401
