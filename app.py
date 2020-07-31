# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.User import UserResource
from resources.Car import CarResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(UserResource, '/User')
api.add_resource(CarResource, '/Car')