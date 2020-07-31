# -*- coding: utf-8 -*-

from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    u_id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(20), unique = True, nullable=False)
    u_password = db.Column(db.String(20), nullable=False)
    
    def __init__(self, u_id, u_name, u_password):
        self.u_id = u_id
        self.u_name = u_name
        self.u_password = u_password
        
    def serialize(self):
        return {
            'id': self.u_id,
            'name': self.u_name,
            'password': self.u_password
        }
        
class UserSchema(ma.Schema):
    u_id = fields.Integer(required=True)
    u_name = fields.String(required=True)
    u_password = fields.String(required=True)
    
    
class Car(db.Model):
    __tablename__ = 'car'
    
    c_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    mpg = db.Column(db.Numeric)
    cylinder = db.Column(db.Integer)
    displacement= db.Column(db.Numeric)
    horsepower = db.Column(db.Integer)
    weight = db.Column(db.Numeric)
    acceleration = db.Column(db.Numeric)
    u_id = db.Column(db.Integer, db.ForeignKey('user.u_id',
                                               ondelete = 'SET NULL',
                                               onupdate = 'CASCADE'))
    
    def __init__(self, c_id, name, mpg, cylinder, displacement, horsepower,
                 weight, acceleration, u_id):
        self.c_id = c_id
        self.acceleration = acceleration
        self.cylinder = cylinder
        self.displacement = displacement
        self.horsepower = horsepower
        self.mpg = mpg
        self.name = name
        self.u_id = u_id
        self.weight = weight
        
    
class CarSchema(ma.Schema):
    c_id = fields.Integer()
    name = fields.String()
    acceleration = fields.Float()
    cylinder = fields.Integer()
    displacement = fields.Float()
    horsepower = fields.Integer()
    mpg = fields.Float()
    u_id = fields.Integer()
    weight = fields.Float()