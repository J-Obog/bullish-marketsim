from flask import Blueprint
from flask.templating import render_template

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/")
def index():
    return render_template("accounts.html", accounts=[{}])