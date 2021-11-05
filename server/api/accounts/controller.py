from .model import AccountData, AccountDataSchema
from flask_jwt_extended import jwt_required, current_user
from flask import jsonify

""" Get account info """
@jwt_required()
def get_account():
    return jsonify(
        id=current_user.id, 
        email=current_user.email,
        equity_prev_close=current_user.equity_prev_close,
        portfolio_equity=current_user.portfolio_equity,
        buying_power=current_user.buying_power,
        created_at=current_user.created_at
    )


""" Get account historical trading data """
@jwt_required()
def get_account_trading_data():
    data = AccountData.query.filter_by(account_id=current_user.id)
    res = AccountDataSchema(many=True).dump(data)
    return jsonify(data=res)