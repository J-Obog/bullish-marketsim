from flask import request
from app import db, bcrypt
from api.accounts.model import Account
from .validators import AccountReq
from marshmallow import ValidationError, EXCLUDE
from flask_jwt_extended import create_access_token, create_refresh_token

def logout():
    pass


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
        return {'access_token': access_token, 'refresh_token': refresh_token}, 200

    return {'success': False, 'msg': 'email and password must match'}, 401


""" Sign user up """
def register_user():    
    # handling validation errors
    try:
        AccountReq().load(request.json, unknown=EXCLUDE)
    except ValidationError as err:
        return {'success': False, 'msg': err.messages}, 401

    # request body vars
    email = request.json.get('email') 
    password = request.json.get('password')

    # loading user into db
    phash = bcrypt.generate_password_hash(password, 10).decode('utf-8')
    acc = Account(email=email, password=phash)
    db.session.add(acc)
    db.session.commit() 
    
    return {'success': True, 'msg': 'Successfully registered'}, 200