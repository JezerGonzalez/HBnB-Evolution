from flask import Blueprint, request, jsonify

users_bp = Blueprint('users', __name__)

users_db = {}
id_counter = 1

@users_bp.route('/', methods=['POST'])
def create_user():
    global id_counter
    data = request.get_json()
    if 'email' in data and data['email'] in (u['email'] for u in users_db.values()):
        return jsonify({"error": "Email already registered"}), 400
    data['id'] = id_counter
    users_db[id_counter] = data
    id_counter += 1
    return jsonify(data), 201

@users_bp.route('/', methods=['GET'])
def get_users():
    return jsonify(list(users_db.values())), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users_db:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    data['id'] = user_id
    users_db[user_id] = data
    return jsonify(data), 200

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users_db:
        return jsonify({"error": "User not found"}), 404
    del users_db[user_id]
    return '', 204
