'''
Author: andy
Date: 2023-06-06 00:17:42
LastEditors: andy
LastEditTime: 2023-06-06 00:48:41
Description: 初始化 app
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app() -> "Flask":
    '''創建一個 app 實體'''

    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)

    @app.route("/")
    def index():
        return "<h1>main</h1>"

    return app
