from app.extentions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False) 
    email = db.Column(db.String, unique=True, nullable=False)