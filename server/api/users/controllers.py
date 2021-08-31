from flask_jwt_extended import jwt_required

@jwt_required()
def protected():
    return "Some protected route"