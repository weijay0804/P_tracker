'''
Author: andy
Date: 2023-06-06 01:07:08
LastEditors: andy
LastEditTime: 2023-06-06 01:09:12
Description: 使用者認證試圖
'''

from . import auth


@auth.route("/register")
def register():
    return "<h1>Register</h1>"
