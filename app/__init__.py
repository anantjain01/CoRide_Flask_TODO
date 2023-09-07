from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from app.resources import UserResource, UserListResource

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo:27017/mydatabase'  # Update with your MongoDB URI
mongo = PyMongo(app)
api = Api(app)

api.add_resource(UserResource, '/users/<string:id>')
api.add_resource(UserListResource, '/users')

from app import routes
