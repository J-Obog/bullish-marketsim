from flask import Blueprint
from .controller import get_user_account, get_user_history

acc_bp = Blueprint('accounts', __name__)
acc_bp.add_url_rule('/', view_func=get_user_account, methods=['GET'])
acc_bp.add_url_rule('/data', view_func=get_user_history, methods=['GET'])