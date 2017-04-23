#!/usr/bin/env python
import os
from app import app
from flask_script import Manager
from app.config import DevelopmentConfig
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


def main():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    app.config.from_object('app.config.DevelopmentConfig')
    migrate = Migrate(app, __import__('database').db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', Server(host='0.0.0.0', port=8080))

    __import__('app.router')
    manager.run()

if __name__ == "__main__":
    main()
