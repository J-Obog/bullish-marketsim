from flask import Blueprint, render_template

accounts_router = Blueprint("accounts", __name__, template_folder="templates")

@accounts_router.route("/")
def index():
    return render_template("index.html")    
