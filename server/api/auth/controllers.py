from flask import request, abort, jsonify
#from functools import wraps
from . import validators
from api.users.models import User
from flask_jwt_extended import create_access_token
from api import bcrypt

def validate():
    return ""

def signup():
    body = request.json
    username = body.get("username")
    password = body.get("password")
    email = body.get("email")
    #validation
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
    user.password = bcrypt.generate_password_hash(password, 10).decode("utf-8")
    user.save()   

    #create jwt token
    access_token = create_access_token(identity={
        "username": user.username,
        "user_id": str(user.mongo_id)
    })

    return jsonify(access_token=access_token), 200