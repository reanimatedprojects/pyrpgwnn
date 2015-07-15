import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

AUTHS = {
# Local accounts (username/password)
# This would normally be enabled for everyone
    'local': {
        'name': 'Local',
    },
}

# This should usually be left as utf-8
CHARSET = 'utf-8'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'rpgwnn.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
