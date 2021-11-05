from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis
from flask_marshmallow import Marshmallow

# application plugins
cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
cache = FlaskRedis()
ma = Marshmallow()

def create_app():
  # configuring app
  app = Flask(__name__)
  app.config.from_pyfile("config.py")
  app.url_map.strict_slashes = False
  
  # binding plugins
  cors.init_app(app)
  db.init_app(app)
  migrate.init_app(app, db)
  bcrypt.init_app(app)
  jwt.init_app(app)
  cache.init_app(app)
  ma.init_app(app)

  #registering blueprints
  from api import main_bp
  app.register_blueprint(main_bp, url_prefix="/api")

  return app