import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = "\x99u\xb3\xd8\xe2\\\x95\xf6\x95\x01vv\x04\x88'Ohq\xba_\x00\xb5\x83\x90"

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

# DEBUG = False