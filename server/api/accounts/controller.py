from .model import AccountData, AccountSchema, AccountDataSchema
from flask import jsonify
from flask_jwt_extended import jwt_required, current_user

""" Get user account info """
@jwt_required()
def get_user_account():
    res = AccountSchema().dump(current_user)
    return jsonify(account=res), 200


""" Get user historical trading data """
@jwt_required()
def get_user_history():
    data = AccountData.query.filter_by(account_id=current_user.id)
    res = AccountDataSchema(many=True).dump(data)
    return jsonify(data=res), 200