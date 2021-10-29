from flask import request, g
from app import db, bcrypt, cache, jwt
from flask_migrate import current
from .validators import AccountValidator
from marshmallow import ValidationError
from api.accounts.model import Account
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, current_user

@jwt.token_in_blocklist_loader
def check_token_in_blacklist(jwt_header, jwt_payload):
    return cache.get(jwt_payload['sub']) is not None

@jwt.user_lookup_loader
def user_lookup(jwt_header, jwt_payload):
    return Account.query.filter_by(id=jwt_payload['sub']).one_or_none()

""" Log a user out"""
@jwt_required()
def logout():
    cache.set(current_user.id, '', ex=3600)
    return {'message': 'Logout successful'}, 200

""" Log a user in """
def login():
    # request body vars
    email = request.json.get('email') 
    password = request.json.get('password')

    # query for account with matching email
    acc = Account.query.filter_by(email=email).first()
    
    # validate if there's a match and the match shares the same password
    if acc and bcrypt.check_password_hash(acc.password, password):
        access_token = create_access_token(identity=acc.id)
        refresh_token = create_refresh_token(identity=acc.id)
        return {'access_token': access_token, 'refresh_token': refresh_token, 'message': 'Login successful'}, 200

    return {'message': 'Email and password must match'}, 401


""" Sign user up """
def register_user():    
    # request body vars
    email = request.json.get('email') 
    password = request.json.get('password')

    # handling validation errors
    try:
        AccountValidator().load(request.json)
    except ValidationError as e:
        return {'message': e.messages}, 401

    if Account.query.filter_by(email=email).first():
        return {'message': {'email': ['Account with email already exists']}}, 401

    # loading user into db
    acc = Account(email=email, password=bcrypt.generate_password_hash(password, 10).decode('utf-8'))
    db.session.add(acc)
    db.session.commit() 
    
    return {'message': 'Registration successful'}, 200