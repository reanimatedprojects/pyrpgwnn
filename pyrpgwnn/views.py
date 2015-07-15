from flask import render_template, redirect, url_for
from pyrpgwnn import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    auth_methods = list(app.config['AUTHS'].keys())
    if len(auth_methods) == 1:
        auth_key = auth_methods.pop(0)
        return redirect(url_for('register_' + auth_key), code=302)

    return render_template('register.html', auths=app.config['AUTHS'])

@app.route('/register/local')
def register_local():
    return render_template('register_local.html')

