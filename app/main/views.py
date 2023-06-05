'''
Author: andy
Date: 2023-06-06 01:48:42
LastEditors: andy
LastEditTime: 2023-06-06 05:34:38
Description: app 主試圖
'''

from datetime import datetime

from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from app import db
from app.db_model import Record, RecordType
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
        type_id = request.form.get("select_type")

        date_object = datetime.strptime(date, "%Y-%m-%d").date()

        record = Record(name=name, price=price, desc=desc, date=date_object)

        user.records.append(record)

        db.session.add(record)
        db.session.commit()

        record_type = RecordType.query.get_or_404(type_id)
        record_type.records.append(record)
        db.session.commit()

        flash("新增成功")
        return redirect(url_for("main.records"))

    r_types = user.record_types

    return render_template("main/add_record.html", r_types=r_types)


@main.route("/edit_record/<id>", methods=["GET", "POST"])
@login_required
def edit_record(id):
    """編輯記帳紀錄路由"""

    user = current_user
    record = Record.query.get_or_404(id)

    if record.user != user:
        abort(403)

    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        desc = request.form.get("desc")
        date = request.form.get("date")

        date_object = datetime.strptime(date, "%Y-%m-%d").date()

        record.name = name
        record.price = price
        record.desc = desc
        record.date = date_object

        db.session.commit()

        flash("更新成功")

        return redirect(url_for("main.records"))

    return render_template("main/edit_record.html", record=record)


@main.route("/delete_record/<id>")
@login_required
def delete_record(id):
    """刪除記帳紀錄路由"""

    user = current_user
    record = Record.query.get_or_404(id)

    if record.user != user:
        abort(403)

    user.records.remove(record)

    db.session.commit()

    flash("刪除成功")

    return redirect(url_for("main.records"))


@main.route("/record_types")
@login_required
def record_types():
    """所有記帳種類路由"""

    user = current_user

    types = user.record_types

    return render_template("main/record_types.html", types=types)


@main.route("/add_record_type", methods=["GET", "POST"])
@login_required
def add_record_type():
    """新增記帳種類路由"""

    user = current_user

    if request.method == "POST":
        name = request.form.get("name")
        desc = request.form.get("desc")

        r_type = RecordType(name=name, desc=desc)

        user.record_types.append(r_type)

        db.session.add(r_type)
        db.session.commit()

        flash("新增成功")

        return redirect(url_for("main.record_types"))

    return render_template("main/add_record_type.html")


@main.route("/edit_record_type/<id>", methods=["GET", "POST"])
@login_required
def edit_record_type(id):
    """編輯記帳種類路由"""

    user = current_user
    r_type = RecordType.query.get_or_404(id)

    if r_type.user != user:
        abort(403)

    if request.method == "POST":
        name = request.form.get("name")
        desc = request.form.get("desc")

        r_type.name = name
        r_type.desc = desc

        db.session.commit()

        flash("更新成功")

        return redirect(url_for("main.record_types"))

    return render_template("main/edit_record_type.html", r_type=r_type)


@main.route("/delete_record_type/<id>")
@login_required
def delete_record_type(id):
    """刪除記帳種類"""

    user = current_user
    r_type = RecordType.query.get_or_404(id)

    if r_type.user != user:
        abort(403)

    user.record_types.remove(r_type)
    db.session.commit()

    flash("刪除成功")

    return redirect(url_for("main.record_types"))
