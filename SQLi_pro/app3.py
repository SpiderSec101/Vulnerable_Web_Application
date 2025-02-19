from flask import Flask, render_template, request
import sqlite3

msg = "Nice try, Try again"


app = Flask(__name__)

# Define your routes and other Flask application code here


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/', methods=['POST'])

def authenticate():
    username = request.form['username']
    password = request.form['password']

    filter = ['or', "'or", 'true', 'true--', '|', '>', '<', '/', '*', '#', 'not', 'is', 'false', 'false--', 'delete', 'update', 'insert', ';', 'and', "'and"]
        

    query = "SELECT * FROM accounts WHERE user='spider" + username + "'AND password='" + password + "';"

    j = 0
    k = 0
    m = 0
    z = 0


    username_new = username.strip()
    password_new = password.strip()


    if username_new.lower() == 'admin' and password_new == 'a_strong_password_goes_here':
        return 'your_flag_goes_here'

    else:

        for i in password_new.split(" "):
            if i.lower() in filter:
                j += 1

        for i in password:
            if i.lower() in filter:
                m += 1

        for i in username_new.split(" "):
            if i.lower() in filter:
                k += 1

        for i in username:
            if i.lower() in filter:
                m += 1
                
                
                
        for i in filter:
            if (i in password or i in username) and 'password' not in username: z += 1 
            if i.upper() in password or i.upper() in username: z += 1 
            if i.title() in password or i.title() in username: z += 1 
                
                

        if j != 0 or k != 0 or m != 0 or z != 0:
            return query
                
        else:

            
            try:
                
                if 'union'.lower() in username_new or 'union'.upper() in username_new or 'union'.title() in username_new: 
                    ind = username_new.lower().index('union')
                    x = int(ind) + 5
                    username_new = (username_new.lower())[x:]
                    
                conn = sqlite3.connect('db.sqlite')
                c = conn.cursor()
                c.execute(username_new)
                user = c.fetchone()
                conn.close()
                if user : return f"Password: {str(user)}"
                else: return msg
            except Exception as e:
                return f"{msg} and also you have a {str(e)}"



if __name__ == '__main__':
    app.run(debug=True)

