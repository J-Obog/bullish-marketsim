from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

# application plugins
db = MongoAlchemy()
cors = CORS()
jwt = JWTManager()
bcrypt = Bcrypt()
ma = Marshmallow()

def create_app():
  # configuring app
  app = Flask(__name__)
  app.config.from_pyfile("config.py")
  app.url_map.strict_slashes = False
  
  # binding plugins
  db.init_app(app)
  cors.init_app(app)
  jwt.init_app(app)
  bcrypt.init_app(app)
  ma.init_app(app)
  
  # routing
  from api.routes import router as api_router
  app.register_blueprint(api_router, url_prefix="/api")
  
  return app