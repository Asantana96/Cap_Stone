from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .fish_api import fish_api_bp
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(fish_api_bp)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# Import your models
from app.models import Fish

# Import your blueprints
from app.blueprints.auth import bp as auth_bp
from app.blueprints.main import bp as main_bp

# Register your blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp) 

# Rest of your code...
