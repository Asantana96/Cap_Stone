from flask import render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
from . import bp
from app import db
from .timer import PomodoroTimer, timer_bp

bp.register_blueprint(timer_bp)

@bp.route('/')
def home():
    return render_template('index.jinja')

@bp.route('/pond', methods=['GET', 'POST'])
def pond():
    

    return render_template('pond.jinja')

@bp.route('/fish_tank')
def fish_tank():
    # fishes = Fish.query.all()
    return render_template('fish_tank.jinja')#add this about inside the paratheises ,fishes=fishes

@bp.route('/api/fish', methods=['GET'])
def get_random_fish():
#     # Logic to generate a random fish or fetch from an external API
#     # Create a new Fish object and add it to the database
#     fish = Fish(type='Random Fish', size='Small', color='Red')
#     db.session.add(fish)
#     db.session.commit()

    return jsonify({'status': 'success'})
