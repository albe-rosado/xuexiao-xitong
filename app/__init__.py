from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_turbolinks import turbolinks

app = Flask(__name__)
# Loads the config 
app.config.from_object('config')

bootstrap = Bootstrap(app)
mail = Mail(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
turbolinks(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

with app.app_context():
    db.create_all()