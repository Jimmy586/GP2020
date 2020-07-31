# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:38:43 2020

@author: ASus
"""

from flask import request
from flask_restful import Resource
from Model import db, Car, CarSchema, User

cars_schema = CarSchema(many = True)
car_schema = CarSchema()

class CarResource(Resource):
    def get(self):
        args_data = request.args

        if not args_data:
            return {'message': 'No input data provided'}, 400
        
        car_id = args_data['c_id']
        user_id = args_data['u_id']
        
        user = User.query.filter_by(u_id = user_id).first()
        
        if not user:
            return {'message': 'User does not exist'}, 400
        
        data = Car.query.filter_by(c_id = car_id, u_id = user_id).first()
        
        if not data:
            return {'message': 'Car does not exist'}, 400
        
        car = car_schema.dump(data).data
        return {'status': 'success', 'data': car}, 200
    
    def post(self):
        args_data = request.args
        if not args_data:
            return {'message': 'No input data provided'}, 400
        
        cars = Car.query.all()
        
        car = Car(
                c_id =  len(cars) + 1,
                name = args_data['name'],
                mpg = args_data['mpg'],
                cylinder = args_data['cylinder'],
                displacement = args_data['displacement'],
                horsepower = args_data['horsepower'],
                weight = args_data['weight'],
                acceleration = args_data['acceleration'],
                u_id = args_data['u_id']
        )
        
        db.session.add(car)
        db.session.commit()
    
        result = car_schema.dump(car).data
    
        return { "status": 'success', 'data': result }, 201
    
    def put(self):
        args_data = request.args
       
        if not args_data:
            return {'message': 'No input data provided'}, 400
       
        data = Car.query.filter_by(c_id = args_data['c_id']).first()
        
        #check car exist
        if not data:
            return {'message': 'Car does not exist'}, 400
        
        
        data.name = args_data['new_name']
        data.mpg = args_data['new_mpg']
        data.cylinder = args_data['new_cylinder']
        data.displacement = args_data['new_displacement']
        data.horsepower = args_data['new_horsepower']
        data.weight = args_data['new_weight']
        data.acceleration = args_data['new_acceleration']
        
        db.session.commit()
        
        result = car_schema.dump(data).data
    
        return { "status": 'success', 'data': result }, 204
    
    def delete(self):
        args_data = request.args
        
        if not args_data:
            return {'message': 'No input data provided'}, 400
        
        
        data = Car.query.filter_by(c_id = args_data['c_id']).first()
        
        if not data:
            return {'message': 'Car does not exist'}, 400
        
        data = Car.query.filter_by(c_id = args_data['c_id']).delete()
        
        db.session.commit()
        
        result = car_schema.dump(data).data
        
        return {"status": 'success', 'data': result}, 204