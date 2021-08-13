from flask import Blueprint, render_template

account_bp = Blueprint("account", __name__) 

@account_bp.route("/")
def index(id):
    return render_template("index.html")