from flask import Blueprint, render_template

bp = Blueprint("account", __name__) 

@bp.route("/")
def index():
    return render_template("accounts.html")

@bp.route("/account/<int:id>")
def home(id):
    return render_template("index.html")