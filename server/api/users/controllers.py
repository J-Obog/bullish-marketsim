from flask import request, abort, jsonify
from functools import wraps

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 1 == 1:
            abort(401)
        return f(*args, **kwargs)
    return wrapper

def signup():
    pass