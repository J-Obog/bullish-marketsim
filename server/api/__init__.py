from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import api.services as services

# application plugins
db = MongoAlchemy()
cors = CORS()
jwt = JWTManager()

def create_app():
  # configuring app
  app = Flask(__name__)
  app.config.from_pyfile("config.py")
  
  # binding plugins
  db.init_app(app)
  cors.init_app(app)
  jwt.init_app(app)

  # routing
  app.register_blueprint(services.router, url_prefix="/api")
  
  return app