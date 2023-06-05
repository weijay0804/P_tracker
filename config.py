'''
Author: andy
Date: 2023-06-06 00:19:25
LastEditors: andy
LastEditTime: 2023-06-06 01:26:14
Description: app 設定檔
'''


import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "This is test token"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "database.db")

    @staticmethod
    def init_app(app):
        pass
