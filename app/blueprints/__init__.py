from flask import Blueprint


auth_bp = Blueprint('auth', __name__, static_folder="static", template_folder="templates")
main_bp = Blueprint('main', __name__)


from app.blueprints.auth import routes
from app.blueprints.main import routes
