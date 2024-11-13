from flask import Flask, render_template, flash, redirect, url_for, request, jsonify, make_response
from application.forms import LoginForm
from application import app
import phpserialize
import base64

#login_manager = LoginManager(app)




def dserialize(encoded_data):

    try:

        decoded_data = (base64.b64decode(encoded_data))
        user_data = phpserialize.loads(decoded_data)

        username = user_data.get(b'name')
        is_admin = user_data.get(b'isAdmin')
        password = user_data[b'password']


        print(username, is_admin, password)
        print(type(password))

        use = username.decode()


        try:
            #password is a string
            pas = password.decode()
            if use == 'administrator' and is_admin:
                if pas == 'a_strog_admin_password_here':
                    return 'admin_valid'
            else:
                return f'Your fake flag is {{{username.decode('utf-8')}:{password.decode('utf-8')}}}'
        except:
            #password is an integer
            if use == 'administrator':
                if password == 0:
                    return 'admin_valid'
            else:
                return f'Your fake flag is {{{username.decode('utf-8')}:{password.decode('utf-8')}}}'



    except Exception as e:
        print(e)
        return 'Error :('



@app.route("/logic.php")
def file():
    return render_template('logic.php')




@app.after_request
def remove_server_header(response):
    # This will remove the 'Server' header from the response
    if 'Server' in response.headers:
        del response.headers['Server']
    return response



@app.route("/")
def home():
    return render_template('home.html')


@app.route("/flag")
def flag():
    encoded_data = request.cookies.get('UserSession')

    if encoded_data :
        x = dserialize(encoded_data)

        if x == 'admin_valid' :
            flash(f'<flag_here>')
        else:
            flash(x)
    else :
        flash(f'Can not get your flag')   

    return render_template('home.html')     



@app.route("/login", methods=['GET', 'POST'])
def login():
    form =  LoginForm()

    if request.method == 'POST' and form.validate_on_submit():

        username = str(form.username.data)
        password = str(form.password.data)

        user_creds = {
            'name': username,
            'password': password,
            'isAdmin': False
        }


        # Serialize and base64 encode the data
        serialized_data = phpserialize.dumps(user_creds)

        encoded_data = base64.b64encode(serialized_data).decode('utf-8')

        response = make_response(redirect(url_for('flag')))
        response.set_cookie('UserSession', encoded_data)
        return response 

    return render_template('login.html', form=form)        




