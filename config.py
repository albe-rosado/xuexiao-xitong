import os
basedir = os.path.abspath(os.path.dirname(__file__))



SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
MAIL_SERVER = 'debugmail.io'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'alberosado7@icloud.com'
MAIL_PASSWORD = '24c07b60-a72d-11e6-a47c-974f7f2487db'
FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

