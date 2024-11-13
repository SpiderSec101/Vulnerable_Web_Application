from flask import Flask, render_template, flash, redirect, url_for
import secrets
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 


db = SQLAlchemy(app)


from application import routes
from application.models import User

