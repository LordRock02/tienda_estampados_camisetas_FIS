from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/prints')
def prints():
    return render_template("prints.html")

@views.route('/tshirts')
def tshirts():
    return render_template("t-shirts.html")

