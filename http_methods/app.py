from flask import Flask, render_template, send_file, request, flash, session, url_for
import secrets

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(24)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='SquidGame')


@app.route("/flag", methods=["GET", "PUT"])
def flag():
    method = request.method
    if method == 'PUT':
        flash('flag{H77p_m3th0d5_m4tt3r5_3b4873b}')
    return render_template('base.html', title='Flag')
    else:
        flash("Oops!! something went wrong :(")





if '__name__' ==  '__main__':
    app.run(debug=False)    

