from flask import request, jsonify
from app import app
from app.models import User, users_collection

@app.route('/users', methods=['GET'])
def get_users():
    users = [User.from_dict(user) for user in users_collection.find()]
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify(User.from_dict(user).to_dict())
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(None, data['name'], data['email'], data['password'])
    result = users_collection.insert_one(new_user.to_dict())
    return jsonify({'message': 'User created', 'id': str(result.inserted_id)}), 201

@app.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    updated_user = User(id, data['name'], data['email'], data['password'])
    users_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_user.to_dict()})
    return jsonify({'message': 'User updated'})

@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    result = users_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404
