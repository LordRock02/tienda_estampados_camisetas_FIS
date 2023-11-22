from flask import Blueprint, redirect, render_template, request, flash, url_for
from .models import *
from .logic.store import *
from .logic.user import User as CurrentUser
from werkzeug.security import generate_password_hash, check_password_hash
#from passlib.hash import sha256_crypt

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname=request.form.get('nickname')
        password=request.form.get('password')
        succes=login_usr(request.form.get('nickname'), password)
        if succes:
            flash('Logged in successfully!', category='success')
            return render_template('home_base.html', isLoggedIn=True)
        else:
            flash('The password or the user doesn\'t match', category='error')
    return render_template("sign_in.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method=='POST':
        message=create_usr(request.form.get('nickname'), request.form.get('email'), request.form.get('password'), request.form.get('password2'))
        if message!='':
            flash(message, category='error')
        else:
            flash('Account created', category='succes')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")