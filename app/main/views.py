'''
Author: andy
Date: 2023-06-06 01:48:42
LastEditors: andy
LastEditTime: 2023-06-06 03:29:39
Description: app 主試圖
'''

from datetime import datetime

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.db_model import Record
from . import main


@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/record", methods=["GET"])
@login_required
def records():
    """顯示所有記帳路由"""

    user = current_user

    records = user.records

    return render_template("main/records.html", records=records)


@main.route("/add_record", methods=["GET", "POST"])
@login_required
def add_record():
    """新增記帳路由"""

    user = current_user

    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        desc = request.form.get("desc")
        date = request.form.get("date")

        date_object = datetime.strptime(date, "%Y-%m-%d").date()

        record = Record(name=name, price=price, desc=desc, date=date_object)

        user.records.append(record)

        db.session.add(record)
        db.session.commit()

        flash("新增成功")
        return redirect(url_for("main.records"))

    return render_template("main/add_record.html")
