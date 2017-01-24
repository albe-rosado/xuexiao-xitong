import os
basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
MAIL_SERVER = 'debugmail.io'
MAIL_PORT = 9025
MAIL_USE_TLS = True
MAIL_USERNAME = 'alberosado7@icloud.com'
MAIL_PASSWORD = '24c07b60-a72d-11e6-a47c-974f7f2487db'
APP_MAIL_SUBJECT_PREFIX = '[APP]'
APP_MAIL_SENDER = 'Admin <admin@site.com>'
APP_ADMIN = 'ADMIN'


# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        # 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# temporary db URI (Dev)
SQLALCHEMY_DATABASE_URI = 'postgres://uvofwqzb:NzHObsMLOy-yfEnLs2WLaTYcU57FwjlD@elmer.db.elephantsql.com:5432/uvofwqzb'


# Storage Config
STORAGE_PROVIDER = "LOCAL"
STORAGE_CONTAINER = os.path.join(basedir,'app/files/')
STORAGE_KEY = ""
STORAGE_SECRET = ""
STORAGE_SERVER = True
UPLOAD_FOLDER = "app/files/uploads/"