from flask import Blueprint
from .accounts import acc_bp
from .auth import auth_bp
from .stocks import stock_bp

main_bp = Blueprint('api', __name__)
main_bp.register_blueprint(auth_bp, url_prefix='/auth')
main_bp.register_blueprint(acc_bp, url_prefix='/account')
main_bp.register_blueprint(stock_bp, url_prefix='/stock')