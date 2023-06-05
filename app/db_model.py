'''
Author: andy
Date: 2023-06-06 00:26:39
LastEditors: andy
LastEditTime: 2023-06-06 00:54:49
Description: database ORM model
'''

from . import db


class User(db.Model):
    '''user table'''

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
