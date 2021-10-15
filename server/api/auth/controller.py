from flask import request
from app import db 
from api.accounts.model import Account
from .validators import AccountReq
from marshmallow import ValidationError, EXCLUDE

def register_user():    
    body = request.json

    try:
        AccountReq().load(body, unknown=EXCLUDE)
    except ValidationError as err:
        return {'success': False, 'errors': err.messages}, 401

    email = body.get('email') 
    password = body.get('password')

    a = Account(email=email, password=password)
    db.session.add(a)
    db.session.commit() 
    return {'email': email, 'password': password}, 200