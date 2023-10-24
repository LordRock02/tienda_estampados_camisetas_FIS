from flask import Blueprint, render_template, request, flash
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods=['GET', 'POST'])
def login():
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
        if password!=password2:
            flash('The passwords don\'t match', category='error')
        elif password == '' or password2 == '':
            flash('Please introduce a password', category='error')
        elif userName == '':
            flash('Please introduce a username', category='error')
        elif email == '':
            flash('Please introduce an E-mail', category='error')
        else:
            new_user = User(userName = userName, email = email, password = password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='succes')
    
    return render_template("sign_up.html")