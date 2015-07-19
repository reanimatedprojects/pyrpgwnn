from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import Required, Email

class LoginLocalForm(Form):
    email = StringField('email') # , validators=[Required(), Email()])
    password = PasswordField('password') # , validators=[Required()])

class RegisterLocalForm(Form):
    email = StringField('email', validators=[Required(), Email()])
    password = PasswordField('password', validators=[Required()])
