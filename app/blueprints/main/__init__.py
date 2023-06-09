from flask import Blueprint


bp = Blueprint('main',__name__)

from app.blueprints.main.timer import timer_bp
