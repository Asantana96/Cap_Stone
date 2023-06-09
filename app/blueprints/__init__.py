from flask import Blueprint

# Create the blueprint objects
auth_bp = Blueprint('auth', __name__, static_folder="static", template_folder="templates")
main_bp = Blueprint('main', __name__)

# Import the routes after creating the blueprint objects
from app.blueprints.auth import routes
from app.blueprints.main import routes
