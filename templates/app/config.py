from os import path

class Config(object):
    DEBUG = False
    TESTING = False
    ROOT_DIR = path.abspath(
        path.dirname(path.join(__file__ + '..'))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/test.db' % (ROOT_DIR)
    SECRET_KEY=${{ SECRET_KEY }}

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/foo'
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_NATIVE_UNICODE = True
