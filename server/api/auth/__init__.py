from flask import Blueprint
from .controller import register_user

auth_bp = Blueprint("auth", __name__)

auth_bp.add_url_rule("/register", view_func=register_user, methods=["POST"])