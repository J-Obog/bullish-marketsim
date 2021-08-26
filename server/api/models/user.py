from api import db

class User(db.Document):
    username = db.StringField()
    email = db.StringField()
    password = db.StringField()
    created_at = db.DateTimeField()