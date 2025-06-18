from flask import Flask, render_template, send_file, request, flash, session, url_for, abort, Response
import secrets

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(24)


@app.route("/")
@app.route("/home")
def home():
    file_url = url_for('content', file='squid_game_plot')
    return render_template('home.html', title='SquidGame', file_url=file_url)

@app.route('/content')
def content():
    file = request.args.get('file', '')
    if file == "../../../../../flag.txt":
        try:
            with open("static/flag.txt", 'r') as fl:
                content = fl.read()
            return Response(content, mimetype='text/plain')
        except FileNotFoundError:
            abort(404)           
    elif file == "squid_game_plot":
        try:
            with open("static/squid_game_plot", 'r') as f:
                content = f.read()
            return Response(content, mimetype='text/plain')
        except FileNotFoundError:
            abort(404)        

    elif ("flag.txt" in file) and (file != "../../../../../flag.txt"):

        err = 'Unable to open any file with name "flag.txt"'
        return Response(err, status=404, mimetype='text/plain')

    return render_template('base.html', title='Flag')

if '__name__' ==  '__main__':
    app.run(debug=False)    

