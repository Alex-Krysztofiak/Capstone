from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                #flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.player'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        sid = request.form.get('sid')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already tied to an account', category='error', )
        elif len(email) < 1:
            flash('Please enter your email', category='error', )
        elif len(firstname) < 1:
            flash('Please enter your name', category='error', )
        elif password1 != password2:
            flash('Passwords don\'t match', category='error', )
        elif len(password1) < 7:
            flash('Passwords have to be atleast 7 characters', category='error', email=email, firstname=firstname, sid=sid)
        else:
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(password1, method='sha256'), sid=sid)
            #new_user = User(email=email, firstname=firstname, password=password1, sid=sid)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.player'))
            

    return render_template("sign_up.html", user=current_user)

@auth.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
