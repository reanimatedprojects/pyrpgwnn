from flask import Flask,redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('pyrpgwnn.config')

db = SQLAlchemy(app)

flask_bcrypt = Bcrypt(app)

# Session management using Flask-Login extension
login_manager = LoginManager()
login_manager.init_app(app)

# if login is required, redirect to the login view (/login)
login_manager.login_view = "login"

# This next line is needed at the end to avoid circular imports
from pyrpgwnn import views, model
