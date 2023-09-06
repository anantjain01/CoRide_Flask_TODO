from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo:27017/mydatabase'  # Update with your MongoDB URI
mongo = PyMongo(app)

from app import routes
