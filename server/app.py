#!/usr/bin/env python3
import os
from flask import Flask, request, session, jsonify
from flask_restful import Resource
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from models import db, User

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

db.init_app(app)


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

