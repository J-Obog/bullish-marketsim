from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = MongoAlchemy()
cors = CORS()
jwt = JWTManager()

def create_app():
  app = Flask(__name__)
  app.config.from_pyfile("config.cfg")
  db.init_app(app)
  cors.init_app(app)
  jwt.init_app(app)
  
  return app