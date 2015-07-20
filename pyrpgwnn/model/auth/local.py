from pyrpgwnn import app

# Local accounts (email/password)
# This would normally be enabled for everyone but can be disabled
# by setting in pyrpgwnn.config AUTH_ENABLE_LOCAL = False

class Auth:

    def __init__(self):
        self.type = 'local'

    def __repr__(self):
        return "Type: %r" % self.type

""" Add the local Auth class to the config if it's enabled """

if 'local' in app.config['AUTHS']:
    print("Already imported auth method 'local'")
elif ('AUTH_ENABLE_LOCAL' in app.config.keys() and
    app.config['AUTH_ENABLE_LOCAL'] == True):

    app.config['AUTHS']['local'] = {
        'name': 'local',
        'class': Auth,
    }

