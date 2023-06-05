'''
Author: andy
Date: 2023-06-06 01:48:42
LastEditors: andy
LastEditTime: 2023-06-06 02:28:18
Description: app 主試圖
'''


from flask import render_template, request

from . import main


@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/record", methods=["GET", "POST"])
def record():
    """記帳路由"""

    if request.method == "POST":
        pass

    record = [{"name": "test1", "price": 120, "date": "2022-01-01", "desc": "this is a test"}]
    return render_template("main/record.html", record=record)
