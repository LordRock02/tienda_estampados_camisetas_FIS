from flask import Blueprint, redirect, render_template, request, flash, url_for
from .models import *
from .business_logic.store import *
from .business_logic.user import User as CurrentUser
from werkzeug.security import generate_password_hash, check_password_hash
#from passlib.hash import sha256_crypt

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        user = User.query.filter_by(nickname=nickname).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                sesion.setUser(CurrentUser(id =user.user_id, name=user.name, last_name=user.last_name, nickname=user.nickname, email=user.email))
                render_template('home_base.html', isLoggedIn=True)
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
        nickname=request.form.get('nickname')
        email=request.form.get('email')
        password=request.form.get('password')
        password2=request.form.get('password2')

        user = User.query.filter_by(nickname=nickname).first()
        if user:
            flash('Email already exists', category='error')
        elif password!=password2:
            flash('The passwords don\'t match', category='error')
        elif password == '' or password2 == '':
            flash('Please introduce a password', category='error')
        elif nickname == '':
            flash('Please introduce a username', category='error')
        elif email == '':
            flash('Please introduce an E-mail', category='error')
        else:
            new_user = User(nickname=nickname, email = email, password = generate_password_hash(password))
            if(generate_password_hash(password) == generate_password_hash(password)):
                print('las contraseñas son iguales')
            else:
                print('las contraseñas no coinciden')
            db.session.add(new_user)
            db.session.commit()
            new_customer = Customer(user_id=new_user.user_id)
            db.session.add(new_customer)
            db.session.commit()
            print(f'id del usuario: {new_user.user_id}')
            flash('Account created', category='succes')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")