from flask import Flask,redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('pyrpgwnn.config')

db = SQLAlchemy(app)

# This next line is needed at the end to avoid circular imports
from pyrpgwnn import views, model
