from flask import render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
from . import bp
from app import db
from .timer import PomodoroTimer, timer_bp
import random

fish_library = {
    '1': {'name': 'Rainbow Trout', 'color': 'Rainbow', 'type': 'Freshwater'},
    '2': {'name': 'Blue Tang', 'color': 'Blue', 'type': 'Saltwater'},
    '3': {'name': 'Betta Fish', 'color': 'Various', 'type': 'Freshwater'},
    '4': {'name': 'Clownfish', 'color': 'Orange', 'type': 'Saltwater'},
    '5': {'name': 'Guppy', 'color': 'Various', 'type': 'Freshwater'},
    '6': {'name': 'Angelfish', 'color': 'Silver', 'type': 'Freshwater'},
    '7': {'name': 'Swordtail', 'color': 'Red', 'type': 'Freshwater'},
    '8': {'name': 'Mandarinfish', 'color': 'Colorful', 'type': 'Saltwater'},
    '9': {'name': 'Catfish', 'color': 'Various', 'type': 'Freshwater'},
    '10': {'name': 'Piranha', 'color': 'Silver', 'type': 'Freshwater'},
}

@bp.route('/fish', methods=['GET'])
def get_fish_info():
    fish_id = random.choice(list(fish_library.keys()))  # Randomly select a fish ID
    fish_info = fish_library.get(fish_id)  # Get the fish information from the library

    if fish_info:
        return jsonify(fish_info)
    else:
        return jsonify({'error': 'Fish not found'})

bp.register_blueprint(timer_bp)

@bp.route('/')
def home():
    return render_template('index.jinja')

@bp.route('/pond', methods=['GET', 'POST'])
def pond():
    return render_template('pond.jinja')

@bp.route('/fish_tank')
def fish_tank():
    return render_template('fish_tank.jinja')

@bp.route('/api/fish', methods=['GET'])
def get_random_fish():
    fish_id = random.choice(list(fish_library.keys()))  # Randomly select a fish ID
    fish_info = fish_library.get(fish_id)  # Get the fish information from the library

    if fish_info:
        return jsonify(fish_info)
    else:
        return jsonify({'error': 'Fish not found'})
