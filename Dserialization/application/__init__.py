from flask import Flask, render_template, flash, redirect, url_for
import secrets


app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(24)
# for csrf

from application import routes
