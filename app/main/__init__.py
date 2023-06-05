'''
Author: andy
Date: 2023-06-06 01:05:59
LastEditors: andy
LastEditTime: 2023-06-06 01:48:36
Description: app 主功能視圖藍圖
'''

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
