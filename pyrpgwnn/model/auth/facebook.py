from pyrpgwnn import app

# Facebook accounts (direct via Facebook)
# This would normally be enabled for everyone but can be disabled
# by setting in pyrpgwnn.config AUTH_ENABLE_FACEBOOK = False

class Auth:
    def __init__(self):
        self.type = 'facebook'

    def __repr__(self):
        return "Type: %r" % self.type

""" Add the facebook Auth class to the config if it's enabled """
    
if 'facebook' in app.config['AUTHS']:
    print("Already imported auth method 'facebook'")
elif ('AUTH_ENABLE_FACEBOOK' in app.config.keys() and
    app.config['AUTH_ENABLE_FACEBOOK'] == True):

    app.config['AUTHS']['facebook'] = {
        'name': 'facebook',
        'class': Auth,
    }
