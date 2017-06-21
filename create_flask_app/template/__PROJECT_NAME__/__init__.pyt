import os
import importlib
from flask import Flask
from flask_script import Manager
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


__author__ = "luavis"
__copyright__ = "Copyright 2017, luavis"
__credits__ = ["luavis", ]
__license__ = "MIT"
__version__ = "0.1.0"
__status__ = "Development"

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if os.environ.get('FLASK_CONFIG') is not None:
    app.config.from_object('${{ PROJECT_NAME }}.config.%s' % os.environ['FLASK_CONFIG'])
else:
    app.config.from_object('${{ PROJECT_NAME }}.config.DevelopmentConfig')
migrate = Migrate(app, importlib.import_module('${{ PROJECT_NAME }}.database').db)
__import__('${{ PROJECT_NAME }}.router')


def main(app):
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', Server(host='0.0.0.0', port=8080))

    manager.run()
