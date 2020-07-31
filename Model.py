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
        
    def __repr__(self):
        return '<id {}>'.format(self.u_id)
        
    def serialize(self):
        return {
            'id': self.u_id,
            'name': self.u_name,
            'password': self.u_password
        }
        
class UserSchema(ma.Schema):
    u_id = fields.Integer()
    u_name = fields.String(required=True)
    u_password = fields.String(required=True)