from flask import Blueprint
from .controller import register_user, login, logout, verify, private_route

auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule('/register', view_func=register_user, methods=['POST'])
auth_bp.add_url_rule('/login', view_func=login, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=private_route(logout, refresh_required=True), methods=['DELETE'])
auth_bp.add_url_rule('/verify', view_func=private_route(verify, refresh_required=True), methods=['GET'])