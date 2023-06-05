'''
Author: andy
Date: 2023-06-06 01:48:42
LastEditors: andy
LastEditTime: 2023-06-06 03:00:02
Description: app 主試圖
'''


from flask import render_template, request
from flask_login import login_required, current_user

from . import main


@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/record", methods=["GET"])
@login_required
def records():
    """顯示所有記帳路由"""

    record = [{"name": "test1", "price": 120, "date": "2022-01-01", "desc": "this is a test"}]
    return render_template("main/records.html", record=record)
