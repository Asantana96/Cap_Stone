from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.fish_api import fish_api_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(fish_api_bp)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.sign_in'

# Import your models after initializing SQLAlchemy
from app.models import User

# Import your blueprints
from app.blueprints.auth import bp as auth_bp
from app.blueprints.main import bp as main_bp

# Register your blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

# Rest of your code...
