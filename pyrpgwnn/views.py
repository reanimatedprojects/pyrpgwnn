from flask import render_template, redirect, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from pyrpgwnn import app, db, login_manager, flask_bcrypt
from pyrpgwnn.model import Account
from .forms import *

# https://flask-login.readthedocs.org/en/latest/

@login_manager.user_loader
def user_loader(userid):
    # Returns None if the account is not valid. userid is the email address
    # This doesn't do the actual authentication
    return Account.query.filter_by(email=userid).one()

@app.before_request
def before_request():
    g.account = current_user

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

@app.route('/register/local', methods=['GET', 'POST'])
def register_local():

    if request.method == 'GET':
        return render_template('register_local.html')

# 1 Check password is ok (at least 3 characters?)
# 2 Check email is ok (rfc822? format)
# 3 If both ok,
#   3.1 create the account using the email address
#   3.2 If it works,
#       3.2.1 register an authentication method for the account
#             (type=local, password=$password
#       3.2.2 If that works,
#           3.2.2.1 great - log them in
#           3.2.2.2 and redirect to the account page
#       3.2.3 If it fails,
#           3.2.3.1 delete the account that was created
#           3.2.3.2 setup error
#           3.2.3.3 redirect back to registration form with error
#   3.3 If it fails,
#       3.3.1 setup error
#       3.3.2 redirect back to registration form with error
# 4 If one or both fail,
#   4.1 setup error with bad email address error if applicable
#   4.2 setup error with bad password error if applicable
#   4.3 redirect back to registration form with error(s)

    vars = { }

# The email is stored in the accounts table, the password
# field is in the account_auths_local table

    # FIXME: Fill in the code for the above logic

    return render_template('register_local.html', vars = vars)

@app.route('/login')
def login():
    auth_methods = list(app.config['AUTHS'].keys())
    if len(auth_methods) == 1:
        auth_key = auth_methods.pop(0)
        return redirect(url_for('login_' + auth_key), code=302)

    return render_template('login.html', auths=app.config['AUTHS'])


@app.route('/login/local', methods=['GET', 'POST'])
def login_local():
    if g.account is not None and g.account.is_authenticated():
        print("Already logged in as " + g.account.email)
        return redirect(url_for('account'))

    # FIXME: Fill in code to check login

    form = LoginLocalForm()

    print(form.email.data)

    if form.is_submitted():
        print("submitted")

    if form.validate():
        print("validated")

    if form.validate_on_submit():
        account = Account.query.filter_by(email = form.email.data).first()
        print(account)
        # if account and flask_bcrypt.check_password_hash(account.password, form.password.data):
        if account and flask_bcrypt.check_password_hash('$2a$12$NmPLLbCTttv74jLV.5KojusYErzFwCyz6Iqi5Q3f19ZHrSJqfSwRe', form.password.data):
            print("authenticated")
            account.authenticated = True
            # this saves the account object in the db.. eg for 'last login' timestamps.

            #db.session.add(account)
            #db.session.commit()
            login_user(account, remember=True)
            return redirect(url_for('account'))

    # return flask.render_template('login_local.html', form=form)
    return render_template('login_local.html', form=form)


@app.route('/account')
@login_required
def account():
    return render_template('account.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
