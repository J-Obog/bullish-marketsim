from flask import request
from app import db, bcrypt
from api.accounts.model import Account
from .validators import AccountReq
from marshmallow import ValidationError, EXCLUDE

def register_user():    
    body = request.json

    # handling validation errors
    try:
        AccountReq().load(body, unknown=EXCLUDE)
    except ValidationError as err:
        return {'success': False, 'errors': err.messages}, 401

    # body variables
    email = body.get('email') 
    password = body.get('password')

    # loading user into db
    phash = bcrypt.generate_password_hash(password, 10).decode('utf-8')
    a = Account(email=email, password=phash)
    db.session.add(a)
    db.session.commit() 
    
    return {'email': a.email, 'password': a.password}, 200