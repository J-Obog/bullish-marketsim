from flask import Blueprint
from .controller import get_account, get_account_trading_data

acc_bp = Blueprint('account', __name__)
acc_bp.add_url_rule('/', view_func=get_account, methods=['GET'])
acc_bp.add_url_rule('/data', view_func=get_account_trading_data, methods=['GET'])