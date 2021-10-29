from flask import Blueprint
from api.auth.controller import private_route


acc_bp = Blueprint('accounts', __name__)