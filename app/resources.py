from flask_restful import Resource, reqparse
from app.models import User, users_collection
from bson import ObjectId

class UserResource(Resource):
    def get(self, id):
        user = users_collection.find_one({'_id': ObjectId(id)})
        if user:
            return User.from_dict(user).to_dict()
        return {'error': 'User not found'}, 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        data = parser.parse_args()

        updated_user = User(id, data['name'], data['email'], data['password'])
        users_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_user.to_dict()})
        return {'message': 'User updated'}

    def delete(self, id):
        result = users_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 1:
            return {'message': 'User deleted'}
        return {'error': 'User not found'}, 404

class UserListResource(Resource):
    def get(self):
        users = [User.from_dict(user) for user in users_collection.find()]
        return [user.to_dict() for user in users]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        data = parser.parse_args()

        new_user = User(None, data['name'], data['email'], data['password'])
        result = users_collection.insert_one(new_user.to_dict())
        return {'message': 'User created', 'id': str(result.inserted_id)}, 201
