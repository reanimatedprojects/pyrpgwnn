#!/usr/bin/env python
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from pyrpgwnn import app, db

app.config.from_object('pyrpgwnn.config')

migrate = Migrate(app, db)
manager = Manager(app, with_default_commands=False)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
