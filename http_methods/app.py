from flask import Flask, render_template, send_file, request, flash, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import secrets

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(24)


admin_password = []

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=10)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AdminForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=10)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Spider-Hub')

@app.route("/tiuwvefisytofisyt", methods=['GET', 'POST', 'PUT'])
def login():
    form = LoginForm()
    if form.validate_on_submit() :
        if (form.username.data).lower() == 'spider' and request.method == 'PUT':
            admin_password.append(form.password.data.lower())
            flash(f"The admin password is changed successfully")
        elif (form.username.data).lower() == 'spider' and request.method != 'PUT':
            flash(f"Spider is an admin")    
        else:
            flash(f"No such user {form.username.data}")    

    return render_template('login.html', title='Spider-Hub', form=form)

@app.route("/robots.txt")
def robots():
    return send_file('robots.txt', as_attachment=False)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    admin_form = AdminForm()
    if admin_form.validate_on_submit():
        if (admin_form.username.data).lower() == 'spider' and (admin_form.password.data).lower() == admin_password[0]:
            flash(f"Here is your flag: logon{{7ricky_h77p_m37h0d5}}")
            admin_password.clear()
        else:
            flash(f"You are not an admin. It will be reported :(")               
    return render_template('login.html', form=admin_form, title='Admin Pannel')




if '__name__' ==  '__main__':
    app.run(debug=False)    

