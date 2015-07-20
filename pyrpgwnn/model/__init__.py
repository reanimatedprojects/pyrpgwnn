from pyrpgwnn import db

# Eventually these classes will need to be split out into
# separate files for each one

class Account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    max_characters = db.Column(db.Integer, nullable=False, default=3)
    characters = db.relationship('Character', backref='account', lazy='dynamic')
    account_auths = db.relationship('AccountAuth', backref='account', lazy='dynamic')

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return (self.account_id is not None)

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return '<Account %r (%d)>' % ( self.email, self.account_id )

class AccountAuth(db.Model):
    __tablename__ = 'account_auth'
    account_auth_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    auth_type = db.Column(db.String(10), nullable=False)

class AccountAuthLocal(db.Model):
    __tablename__ = 'account_auth_local'
    id = db.Column(db.Integer, primary_key=True)
    account_auth_id = db.Column(db.Integer, db.ForeignKey('account_auth.account_auth_id'))
    # Extra parameters required specifically for this auth method
    # Encrypted password
    password = db.Column(db.String(255), nullable=False)

class Character(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    name = db.Column(db.String(64), index=True, unique=True)
    xp = db.Column(db.Integer, nullable=False, default=0)
    disabled = db.Column(db.String(10))
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    z = db.Column(db.Integer, nullable=False)
    world = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Character %r (%d)>' % ( self.name, self.character_id )

class Map(db.Model):
    map_id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    z = db.Column(db.Integer, nullable=False)
    world = db.Column(db.Integer, nullable=False)
    tile_id = db.Column(db.Integer, db.ForeignKey('tile.tile_id'), nullable=False)
    name = db.Column(db.String(32))
    css_class = db.Column(db.String(32))

    def __repr__(self):
        return '<Map %r (%d)>' % ( self.name, self.map_id )

class Tile(db.Model):
    tile_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    description = db.Column(db.String(255))
    background_image = db.Column(db.String(32))
    background_colour = db.Column(db.String(7))
    css_class = db.Column(db.String(32))

    def __repr__(self):
        return '<Tile %r (%d)>' % ( self.name, self.tile_id )
