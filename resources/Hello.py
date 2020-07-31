# -*- coding: utf-8 -*-

from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}