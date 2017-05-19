import os
from flask import Flask
from flask_script import Manager
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


__author__ = "${{ AUTHOR }}"
__copyright__ = "Copyright ${{ YEAR }}, ${{ AUTHOR }}"
__credits__ = ["${{ AUTHOR }}", ]
__license__ = "${{ LICENSE }}"
__version__ = "${{ VERSION }}"
__status__ = "Development"

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def main():
    from ${{ PROJECT_NAME }}.database import db
    if os.environ.get('FLASK_CONFIG') is not None:
        app.config.from_object('${{ PROJECT_NAME }}.config.%s' % os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('${{ PROJECT_NAME }}.config.DevelopmentConfig')
    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', Server(host='0.0.0.0', port=8080))

    __import__('${{ PROJECT_NAME }}.router')
    manager.run()
