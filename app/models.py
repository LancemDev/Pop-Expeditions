from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    languages_spoken = db.Column(db.String(100), nullable=False)
    currency = db.Column(db.String(100), nullable=False)
    visa_requirements = db.Column(db.String(100), nullable=False)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    photo_main = db.Column(db.String(100), nullable=False)
    photo_profile = db.Column(db.String(100), nullable=False)
    photo_others = db.Column(db.String(100), nullable=False)
    area = db.Column(db.String(100), nullable=False)