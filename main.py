'''
Author: andy
Date: 2023-06-06 00:22:26
LastEditors: andy
LastEditTime: 2023-06-06 00:58:27
Description: app 運行主程式
'''

from flask_migrate import Migrate

from app import create_app, db

app = create_app()

migrate = Migrate(app, db)
