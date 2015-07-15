from flask import Flask,redirect

app = Flask(__name__)
app.config.from_object('pyrpgwnn.config')

from pyrpgwnn import views
