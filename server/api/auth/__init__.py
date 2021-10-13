from flask import Blueprint
from .controller import test

auth_bp = Blueprint("auth", __name__)