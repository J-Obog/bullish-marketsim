from flask import request, g
from app import db, bcrypt, cache
from api.accounts.model import Account
from .validators import AccountReq
from marshmallow import ValidationError, EXCLUDE
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from functools import wraps

def decode_auth_token(token):
    try:
        return decode_token(token)
    except Exception as err:
        print(err)
        return None
        
""" Private route decorator"""
def private_route(fn):
    @wraps(fn)
    def wrap(*args, **kwargs):
        token = request.headers.get('authorization')
        token_decoded = decode_auth_token(token) 

        # check if token is present in header
        if not token:
            return {'message': 'Authentication credentials were not provided'}, 401

        # check if token is in blacklist    
        if cache.get(token) or not token_decoded:
            return {'message': 'Invalid Authorization header'}, 401

        g.jwt_identity = {'sig': token, 'exp': token_decoded['exp'], 'id': token_decoded['sub']}
        return fn(*args, **kwargs)
    return wrap

    
""" Log a user out"""
def logout():
    # add token to black list
    cache.set(g.get('jwt_identity')['sig'], 1, ex=3600)
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
    # handling validation errors
    try:
        AccountReq().load(request.json, unknown=EXCLUDE)
    except ValidationError as err:
        return {'message': err.messages}, 401

    # request body vars
    email = request.json.get('email') 
    password = request.json.get('password')

    # loading user into db
    acc = Account(email=email, password=bcrypt.generate_password_hash(password, 10).decode('utf-8'))
    db.session.add(acc)
    db.session.commit() 
    
    return {'message': 'Registration successful'}, 200