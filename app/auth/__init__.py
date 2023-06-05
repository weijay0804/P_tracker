'''
Author: andy
Date: 2023-06-06 01:05:59
LastEditors: andy
LastEditTime: 2023-06-06 01:07:36
Description: 使用者認證相關視圖藍圖
'''

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
