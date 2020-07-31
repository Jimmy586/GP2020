# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource
from Model import db, User, UserSchema

users_schema = UserSchema(many = True)
user_schema = UserSchema()

class UserResource(Resource):    
    def get(self):
        args_data = request.args
        if not args_data:
            return {'message': 'No input data provided'}, 400
        
        name = args_data['name']
        password = args_data['password']
        data = User.query.filter_by(u_name = name,
                                    u_password = password).first()
        if not data:
            return {'message': 'User does not exist'}, 400
        else:
            user = User.serialize(data)
            return {'status': 'success', 'data': user}, 200    
    
    def post(self):
        args_data = request.args
        if not args_data:
            return {'message': 'No input data provided'}, 400
        
        user = User.query.filter_by(u_name = args_data['name']).first()
        if user:
            return {'message': 'User already exists'}, 400
        user = User(
                u_id =  args_data['id'],
                u_name = args_data['name'],
                u_password = args_data['password']
        )
        
        db.session.add(user)
        db.session.commit()
    
        result = user_schema.dump(user).data
    
        return { "status": 'success', 'data': result }, 201
    
    def put(self):
        args_data = request.args
       
        if not args_data:
            return {'message': 'No input data provided'}, 400
       
        data = User.query.filter_by(u_name = args_data['name']).first()
        
        #check user exist
        if not data:
            return {'message': 'User does not exist'}, 400
        
        #check new name exist
        data_new = User.query.filter_by(u_name = args_data['new_name']).first()
        if data_new:
            return {'message': 'User already exists'}, 400
        
        data.u_name = args_data['new_name']
        data.u_password = args_data['new_password']
        
        db.session.commit()
        
        result = user_schema.dump(data).data
    
        return { "status": 'success', 'data': result }, 204
    
    def delete(self):
        args_data = request.args
        
        if not args_data:
            return {'message': 'No input data provided'}, 400
        
        
        data = User.query.filter_by(u_name = args_data['name']).first()
        
        if not data:
            return {'message': 'User does not exist'}, 400
        
        data = User.query.filter_by(u_name = args_data['name']).delete()
        
        db.session.commit()
        
        result = user_schema.dump(data).data
        
        return {"status": 'success', 'data': result}, 204