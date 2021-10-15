from flask import request
from app import db, bcrypt
from api.accounts.model import Account
from .validators import AccountReq
from marshmallow import ValidationError, EXCLUDE

def login():
    # request body vars
    body = request.json
    email = body.get('email') 
    password = body.get('password')

    # query for account with matching email
    acc = Account.query.filter_by(email=email).first()

    # validate if there's a match and the match shares the same password
    if acc and bcrypt.check_password_hash(acc.password, password):
        return {'success': True, 'msg': 'sucesffully logged in'}, 200

    return {'success': False, 'msg': 'email and password must match'}, 401


def register_user():    
    body = request.json

    # handling validation errors
    try:
        AccountReq().load(body, unknown=EXCLUDE)
    except ValidationError as err:
        return {'success': False, 'msg': err.messages}, 401

    # request body vars
    email = body.get('email') 
    password = body.get('password')

    # loading user into db
    phash = bcrypt.generate_password_hash(password, 10).decode('utf-8')
    acc = Account(email=email, password=phash)
    db.session.add(acc)
    db.session.commit() 
    
    return {'success': True, 'msg': 'Successfully registered'}, 200