from . import db
#from flask_login import UserMixin
from sqlalchemy.sql import func
#modelos de las tablas de la base de datos

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=func.now)
    UserType = db.Column(db.Integer, db.ForeignKey('UserType.id'))
class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
"""class T_Shirt(db.Model):
    pass
class Stamp(db.Model):
    pass
class CustomTShirt(db.Model):
    pass
class Invoice(db.Model):
    pass
class Purchase(db.Model):
    pass
class OrderDetails(db.Model):
    pass"""