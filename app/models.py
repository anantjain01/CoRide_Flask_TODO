from app import mongo
from bson import ObjectId

class User:
    def __init__(self, id, name, email, password):
        self._id = id
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def from_dict(data):
        return User(data.get('_id'), data.get('name'), data.get('email'), data.get('password'))

    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
        }
# users_collection = mongo.db.users
