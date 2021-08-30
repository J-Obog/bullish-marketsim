from flask import request, abort, jsonify
from functools import wraps
from . import validators
from api.users.models import User
from api import bcrypt

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 1 == 1:
            abort(401)
        return f(*args, **kwargs)
    return wrapper

def signup():
    body = request.json
    username = body.get("username")
    password = body.get("password")
    email = body.get("email")
    #errors
    username_error = validators.validate_username(username, min=8)
    password_error = validators.validate_password(password, min=8)
    email_error = validators.validate_email(email, regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")

    if username_error:
        return jsonify(success=False, error=username_error), 403
    if password_error:
        return jsonify(success=False, error=password_error), 403
    if email_error:
        return jsonify(success=False, error=email_error), 403

    #save user info
    user = User(username=username, password=password, email=email)
    hashed = bcrypt.generate_password_hash(password, 10).decode("utf-8")
    user.password = hashed
    user.save()  
    
    #o = bcrypt.check_password_hash(user.password.encode("utf-8"), "joshua2001")
    #print(o)

    return ""