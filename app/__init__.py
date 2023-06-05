'''
Author: andy
Date: 2023-06-06 00:17:42
LastEditors: andy
LastEditTime: 2023-06-06 01:53:23
Description: 初始化 app
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> "Flask":
    '''創建一個 app 實體'''

    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
