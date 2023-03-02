from flask import Flask
import os

application = Flask(__name__)

application.config['SECRET_KEY'] = os.environ['SECRET_KEY']

application.config['SECRET_KEY'] = '80981b81d7c7cdc17815c28b24f29a859f1e1abd62e4b90f'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

