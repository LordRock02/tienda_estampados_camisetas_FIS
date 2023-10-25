from flask import Blueprint, redirect, render_template, request, flash, url_for
from .models import User, User_type, db
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import sha256_crypt

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')
        user = User.query.filter_by(username=userName).first()
        if user:
            if password == user.password:
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('User does not exist.', category='error')
    return render_template("sign_in.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method=='POST':
        userName=request.form.get('userName')
        email=request.form.get('email')
        password=request.form.get('password')
        password2=request.form.get('password2')

        user = User.query.filter_by(username=userName).first()
        if user:
            flash('Email already exists', category='error')
        elif password!=password2:
            flash('The passwords don\'t match', category='error')
        elif password == '' or password2 == '':
            flash('Please introduce a password', category='error')
        elif userName == '':
            flash('Please introduce a username', category='error')
        elif email == '':
            flash('Please introduce an E-mail', category='error')
        else:
            new_user = User(username = userName, email = email, password = password, userType =1)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='succes')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")