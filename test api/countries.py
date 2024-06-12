from flask import Blueprint, request, jsonify

countries_bp = Blueprint('countries', __name__)

countries_db = {}
country_id_counter = 1

@countries_bp.route('/', methods=['POST'])
def create_country():
    global country_id_counter
    data = request.get_json()
    data['id'] = country_id_counter
    countries_db[country_id_counter] = data
    country_id_counter += 1
    return jsonify(data), 201

@countries_bp.route('/', methods=['GET'])
def get_countries():
    return jsonify(list(countries_db.values())), 200

@countries_bp.route('/<int:country_id>', methods=['GET'])
def get_country(country_id):
    country = countries_db.get(country_id)
    if not country:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(country), 200

@countries_bp.route('/<int:country_id>', methods=['PUT'])
def update_country(country_id):
    if country_id not in countries_db:
        return jsonify({"error": "Country not found"}), 404
    data = request.get_json()
    data['id'] = country_id
    countries_db[country_id] = data
    return jsonify(data), 200

@countries_bp.route('/<int:country_id>', methods=['DELETE'])
def delete_country(country_id):
    if country_id not in countries_db:
        return jsonify({"error": "Country not found"}), 404
    del countries_db[country_id]
    return '', 204
