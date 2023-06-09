from flask import render_template, request, redirect, url_for, jsonify
from . import bp
from app import db


@bp.route('/')
def home():
    return render_template('index.jinja')


@bp.route('/pond', methods=['GET', 'POST'])
def pond():
    return render_template('pond.jinja')


@bp.route('/fish_tank')
def fish_tank():
    # fishes = Fish.query.all()
    return render_template('fish_tank.jinja')  # add this about inside the parentheses , fishes=fishes


@bp.route('/api/fish', methods=['GET'])
def get_random_fish():
    return jsonify({'status': 'success'})
