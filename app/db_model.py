'''
Author: andy
Date: 2023-06-06 00:26:39
LastEditors: andy
LastEditTime: 2023-06-06 01:02:28
Description: database ORM model
'''

from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model):
    '''user table'''

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        '''讓外部無法讀取 pssword 屬性'''
        raise AttributeError('Password is not a readablb attribute.')

    @password.setter
    def password(self, password: str):
        '''將密碼雜湊後儲存至資料庫'''

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        '''檢查使用者密碼是否正確'''

        return check_password_hash(self.password_hash, password)