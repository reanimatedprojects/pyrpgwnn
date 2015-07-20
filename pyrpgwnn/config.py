import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# This is for encrypting the sessions, please change it!
SECRET_KEY = 'something really secret'

AUTHS = { }

AUTH_ENABLE_LOCAL = True
AUTH_ENABLE_FACEBOOK = False

# This should usually be left as utf-8
CHARSET = 'utf-8'

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'a random string'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'rpgwnn.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
