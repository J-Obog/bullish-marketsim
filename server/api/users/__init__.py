from flask import Blueprint
from . import controllers as user_controller

router = Blueprint("users", __name__)

router.add_url_rule("/protected", view_func=user_controller.protected, methods=["GET"])