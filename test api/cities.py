from flask import Blueprint, request, jsonify

cities_bp = Blueprint('cities', __name__)

cities_db = {}
city_id_counter = 1

@cities_bp.route('/', methods=['POST'])
def create_city():
    global city_id_counter
    data = request.get_json()
    data['id'] = city_id_counter
    cities_db[city_id_counter] = data
    city_id_counter += 1
    return jsonify(data), 201

@cities_bp.route('/', methods=['GET'])
def get_cities():
    return jsonify(list(cities_db.values())), 200

@cities_bp.route('/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = cities_db.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    return jsonify(city), 200

@cities_bp.route('/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    if city_id not in cities_db:
        return jsonify({"error": "City not found"}), 404
    data = request.get_json()
    data['id'] = city_id
    cities_db[city_id] = data
    return jsonify(data), 200

@cities_bp.route('/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    if city_id not in cities_db:
        return jsonify({"error": "City not found"}), 404
    del cities_db[city_id]
    return '', 204
