from . import db
from sqlalchemy.sql import func
#modelos de las tablas de la base de datos
#many to many tables

class Wallet(db.Model):
    user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'))
    payment_method_id=db.Column(db.Integer, db.ForeignKey('payment_method.payment_method_id'), primary_key=True)
class Tshirt_detail(db.Model):
    tshirt_id=db.Column(db.Integer, db.ForeignKey('tshirt.tshirt_id'), primary_key=True)
    print_id=db.Column(db.Integer, db.ForeignKey('print.print_id'), primary_key=True)
class Print_detail(db.Model):
    print_id=db.Column(db.Integer, db.ForeignKey('print.print_id'), primary_key=True) 
    category_id=db.Column(db.Integer, db.ForeignKey('category.category_id'), primary_key=True)
class Purchase_detail(db.Model):
    tshirt_id=db.Column(db.Integer, db.ForeignKey('tshirt.tshirt_id'), primary_key=True)
    purchase_id=db.Column(db.Integer, db.ForeignKey('purchase.purchase_id'), primary_key=True)
    quantity=db.Column(db.Integer)
    subTotal=db.Column(db.Integer)
class Warehouse(db.Model):
    tshirt_id=db.Column(db.Integer, db.ForeignKey('tshirt.tshirt_id'), primary_key=True)
    size_id=db.Column(db.Integer, db.ForeignKey('size.size_id'), primary_key=True)
    stock=db.Column(db.Integer)
#entity tables
class User(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nickname=db.Column(db.String(50), nullable=False)
    name=db.Column(db.String(50), nullable=True)
    last_name=db.Column(db.String(50), nullable=True)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    customer=db.relationship("Customer", uselist=False, backref='user')
    artist=db.relationship("Artist", uselist=False, backref='user')
    admin=db.relationship("Admin", uselist=False, backref='user')
    wallet=db.relationship("Payment_method", secondary=Wallet.__table__, backref="payment_methods")
class Customer(db.Model):
    customer_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True, nullable=False)
    description=db.Column(db.String(50), nullable=True)
    purchase=db.relationship('purchase')
class Artist(db.Model):
    artist_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True, nullable=False)
    artist_info=db.Column(db.String(200))
    prints=db.relationship('Print')
class Admin(db.Model):
    admin_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True, nullable=False)
    description=db.Column(db.String(50))
class Payment_method(db.Model):
    payment_method_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    payment_name=db.Column(db.String(50), nullable=False)
class purchase(db.Model):
    purchase_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    customer_id=db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    Purchase_detail=db.relationship('Tshirt', secondary=Purchase_detail.__table__, backref='tshirts')
    date= db.Column(db.DateTime(timezone=True), default=func.now())
    total=db.Column(db.Integer, nullable=False)
class Tshirt(db.Model):
    tshirt_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    image=db.Column(db.String(100), nullable=False)
    cost=db.Column(db.Integer, nullable=False)
    name=db.Column(db.String(50))
    description=db.Column(db.String(100))
    show=db.Column(db.Boolean)
    tshirt_detail=db.relationship('Print', secondary=Tshirt_detail.__table__, backref='details')
    Warehouse=db.relationship('Size', secondary=Warehouse.__table__, backref='sizes')
class Print(db.Model):
    print_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    image=db.Column(db.String(100), nullable=False)
    cost=db.Column(db.Integer, nullable=False)
    print_name=db.Column(db.String(100))
    artist_id=db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    print_detail=db.relationship('Category', secondary=Print_detail.__table__, backref='categories')
    date= db.Column(db.DateTime(timezone=True), default=func.now())
class Category(db.Model):
    category_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    category_name=db.Column(db.String(20), nullable=False)
class Size(db.Model):
    size_id=db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name=db.Column(db.String(10), nullable=False)

 