'''
Author: andy
Date: 2023-06-06 01:48:42
LastEditors: andy
LastEditTime: 2023-06-06 02:09:00
Description: app 主試圖
'''


from flask import render_template

from . import main


@main.route("/")
def index():
    return render_template("main/index.html")
