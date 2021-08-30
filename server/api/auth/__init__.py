from flask import Blueprint
from . import controllers as auth_controller

router = Blueprint("auth", __name__)

router.add_url_rule("/signup", view_func=auth_controller.signup, methods=["POST"])
