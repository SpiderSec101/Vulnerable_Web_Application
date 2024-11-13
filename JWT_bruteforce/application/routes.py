from flask import Flask, render_template, flash, redirect, url_for, request, jsonify, make_response
from application.forms import RegistrationForm, LoginForm
from application import app, db
from application.models import User 
import string 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user

import jwt
from datetime import datetime, timedelta


SECRET = "2c89956d186a75693f2be77a79874107ed7fc7e2f860f0156abe8e2c20e5b12d"

# this secret can be brute force using hashcat and the jwt_secret wordlist can be found from github

def generate_jwt_token(username, remember_me=False):
    """Generate JWT token with optional expiration."""
    payload = {
        'username': username
    }
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return token



banned_characters = list(string.punctuation)
banned_characters.append('admin')
banned_characters.append('administrator')
#print(banned_characters)

b = Bcrypt()

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    # we use get function to get the user id

@app.after_request
def remove_server_header(response):
    # This will remove the 'Server' header from the response
    if 'Server' in response.headers:
        del response.headers['Server']
    return response


def check_jwt_token(token_check):
    try:
        form = LoginForm()
        data = jwt.decode(token_check, SECRET, algorithms=['HS256'])
        user_check = data.get('username')
        user = User.query.filter_by(username=user_check).first()
        # checking if the user exists and if the secret is correct
        if user :
            return 'bgmi'
        elif user_check == 'admin':
            return user_check
        else:
            flash(f'Error  :  User  does  not  exists')


    except Exception as e:
        flash(f'ZG8gbm90IHdhc3RlIHlvdXIgdGltZSA6KQ==')
            


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')



@app.route("/admin", methods=['GET', 'POST'])
def admin():
    token = request.cookies.get('jwt_token')
    if not token:
        flash('Please login as admin')
        return redirect(url_for('login'))

    elif token:
        try:
            data = jwt.decode(token, SECRET, algorithms=['HS256'])
            username = data.get('username')
            if username != 'admin':
                flash(f'You  are  {username}  not  admin')

            else:
                # If the username is 'admin', display the flag
                flash(f'your_flag_here')

        except Exception as e:
            flash(f'ZG8gbm90IHdhc3RlIHlvdXIgdGltZSA6KQ==')

    return render_template('home.html', title='Admin Panel')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit() :
        for i in banned_characters:
            if i in (form.username.data).lower():
                flash(f'Warning : Account is not created. Suspicious activity detected')
                return redirect(url_for('register'))
                
        hashed_password = b.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created for {form.username.data}')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)





@app.route("/login", methods=['GET', 'POST'])
def login():
    token_check = request.cookies.get('jwt_token')
    form =  LoginForm()
    if token_check:
        x = check_jwt_token(token_check)

        if x == 'bgmi':
            response = make_response(redirect(url_for('home')))
            response.set_cookie('jwt_token', token_check, httponly=True) 
            flash(f'Welcome {form.username.data}')
            return response

        elif x == 'admin':
            flash(f'Admin  must  know  his  path')

    else:
        if form.validate_on_submit() :
            user = User.query.filter_by(username=form.username.data).first()

            if user and b.check_password_hash(user.password, form.password.data):  

                token = generate_jwt_token(user.username, form.remember_me.data)
                response = make_response(redirect(url_for('home')))
                response.set_cookie('jwt_token', token, httponly=True) 
                #login_user(user)
                flash(f'Welcome {form.username.data}')
                return response

            else:
                flash(f'Please check your username or password')         
    
    return render_template('login.html', title='Login', form=form)        




@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('home')))
    response.set_cookie('jwt_token', '', expires=0)  # Clear the JWT token
    flash(f'You have been logged out. Bye <0j0>')
    #logout_user()
    return response 

    return render_template('login.html', form=form)    




