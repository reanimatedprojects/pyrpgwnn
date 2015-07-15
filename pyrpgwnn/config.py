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
