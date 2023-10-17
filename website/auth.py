from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/sign-in')
def login():
    return render_template("sign_in.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")