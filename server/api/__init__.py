from flask import Blueprint
from .auth import auth_bp

main_bp = Blueprint("api", __name__)

main_bp.register_blueprint(auth_bp, url_prefix="/auth")