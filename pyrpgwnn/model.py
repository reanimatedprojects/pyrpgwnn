from pyrpgwnn import db

# Eventually these classes will need to be split out into
# separate files for each one

class Account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    max_characters = db.Column(db.Integer)
    characters = db.relationship('Character', backref='account', lazy='dynamic')

    def __repr__(self):
        return '<Account %r (%d)>' % ( self.email, self.account_id )

class Character(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    name = db.Column(db.String(64), index=True, unique=True)
    xp = db.Column(db.Integer)
    disabled = db.Column(db.String(10))
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    z = db.Column(db.Integer)
    world = db.Column(db.Integer)

    def __repr__(self):
        return '<Character %r (%d)>' % ( self.name, self.character_id )

class Map(db.Model):
    map_id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    z = db.Column(db.Integer)
    world = db.Column(db.Integer)
    tile_id = db.Column(db.Integer, db.ForeignKey('tile.tile_id'))
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
