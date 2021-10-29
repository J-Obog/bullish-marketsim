from flask import Blueprint
from .controller import register_user, login, logout

auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule('/register', view_func=register_user, methods=['POST'])
auth_bp.add_url_rule('/login', view_func=login, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=logout, methods=['DELETE'])