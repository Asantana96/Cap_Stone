from flask import render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
from . import bp
from app.models import Fish

timer_running = False

@bp.route('/')
def home():
    return render_template('index.jinja')

@bp.route('/pond', methods=['GET', 'POST'])
def pond():
    global timer_running
    timer_value = 0

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'start_timer':
            start_time = datetime.now()
            end_time = start_time + timedelta(minutes=25)
            timer_running = True
            timer_value = (end_time - start_time).total_seconds() * 1000

        elif action == 'stop_timer':
            timer_running = False

    return render_template('pond.jinja', timer_value=timer_value)

@bp.route('/fish_tank')
def fish_tank():
    fishes = Fish.query.all()
    return render_template('fish_tank.jinja', fishes=fishes)

@bp.route('/api/fish', methods=['GET'])
def get_random_fish():
    # Logic to generate a random fish or fetch from an external API
    # Create a new Fish object and add it to the database
    fish = Fish(type='Random Fish', size='Small', color='Red')
    db.session.add(fish)
    db.session.commit()

    return jsonify({'status': 'success'})
