from api.users.models import User
import re 

def validate_username(value, min):
    if not isinstance(value, str):
        return {"username": "Username must be of type string"}
    if not value:
        return {"username": "Username cannot be empty"}
    if ' ' in value:
        return {"username": "Username cannot contain whitespace"}
    if len(value) < min:
        return {"username": f"Username must be at least {min} characters long"}
    if User.query.filter_by(username=value).first():
        return {"username": "Username already taken"}
    
def validate_password(value, min):
    if not isinstance(value, str):
        return {"password": "Password must be of type string"}
    if not value:
        return {"password": "Password cannot be empty"}
    if ' ' in value:
        return {"password": "Password cannot contain whitespace"}
    if len(value) < min:
        return {"password": f"Password must be at least {min} characters long"}

def validate_email(value, regex):
    pattern = re.compile(regex)
    if not isinstance(value, str):
        return {"email": "Email must be of type string"}
    if not value:
        return {"email": "Email cannot be empty"}
    if ' ' in value:
        return {"email": "Email cannot contain whitespace"}
    if not pattern.match(value):
        return {"email": f"Email must be valid"}
    if User.query.filter_by(email=value).first():
        return {"email": "Username already taken"}