from flask import Blueprint, jsonify
import random
fish_api_bp = Blueprint('fish_api', __name__)

@fish_api_bp.route('/fish', methods=['GET'])
def get_fish_info():
    fish_library = {
        '1': {'type': 'Salmon', 'color': 'Pink', 'description': 'Salmon are famous for their incredible journeys.'},
        '2': {'type': 'Tuna', 'color': 'Silver', 'description': 'Tuna are known for their speed and strength.'},
        '3': {'type': 'Bass', 'color': 'Green', 'description': 'Bass are popular game fish.'},
    }
    fish_id = random.choice(list(fish_library.keys()))  
    fish_info = fish_library.get(fish_id) 
  
    if fish_info:
        return jsonify(fish_info)
    else:
        return jsonify({'error': 'Fish not found'})
   

  


