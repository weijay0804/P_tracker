'''
Author: andy
Date: 2023-06-06 01:48:42
LastEditors: andy
LastEditTime: 2023-06-06 07:22:43
Description: app 主試圖
'''

from datetime import datetime

from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from app import db
from app.db_model import Record, RecordType, Project
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
        project_id = request.form.get("select_project")

        date_object = datetime.strptime(date, "%Y-%m-%d").date()

        record = Record(name=name, price=price, desc=desc, date=date_object)

        user.records.append(record)

        if int(project_id) != 0:
            project = Project.query.get_or_404(project_id)

            project.current_price = project.current_price + float(price)
            project.records.append(record)

        db.session.add(record)
        db.session.commit()

        record_type = RecordType.query.get_or_404(type_id)
        record_type.records.append(record)
        db.session.commit()

        flash("新增成功")
        return redirect(url_for("main.records"))

    r_types = user.record_types
    u_projects = user.projects

    return render_template("main/add_record.html", r_types=r_types, projects=u_projects)


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


@main.route("/record_type/<id>")
@login_required
def record_type(id):
    """單一記帳種類路由"""

    user = current_user

    r_type = RecordType.query.get_or_404(id)

    if r_type.user != user:
        abort(403)

    records = r_type.records

    return render_template("main/record_type.html", r_type=r_type, records=records)


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


@main.route("/projects")
@login_required
def projects():
    """所有專案路由"""

    user = current_user

    projects = user.projects

    return render_template("main/projects.html", projects=projects)


@main.route("/project/<id>")
@login_required
def project(id):
    """單一專案路由"""

    user = current_user
    u_project = Project.query.get_or_404(id)

    if u_project.user != user:
        abort(403)

    records = u_project.records

    return render_template("main/project.html", project=u_project, records=records)


@main.route("/add_project", methods=["GET", "POST"])
@login_required
def add_project():
    """新增專案路由"""

    user = current_user

    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        desc = request.form.get("desc")
        date = request.form.get("date")

        date_object = datetime.strptime(date, "%Y-%m-%d").date()

        project = Project(name=name, price=price, current_price=price, desc=desc, date=date_object)

        user.projects.append(project)

        db.session.add(project)
        db.session.commit()

        flash("新增成功")
        return redirect(url_for("main.projects"))

    return render_template("main/add_project.html")


@main.route("/edit_project/<id>", methods=["GET", "POST"])
@login_required
def edit_project(id):
    """編輯專案路由"""

    user = current_user
    project = Project.query.get(id)

    if project.user != user:
        abort(403)

    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        desc = request.form.get("desc")
        date = request.form.get("date")

        date_object = datetime.strptime(date, "%Y-%m-%d").date()

        tmp_price = project.price - project.current_price

        project.name = name
        project.price = price
        project.current_price = float(price) - tmp_price
        project.desc = desc
        project.date = date_object

        db.session.commit()

        flash("更新完成")

        return redirect(url_for("main.projects"))

    return render_template("main/edit_project.html", project=project)


@main.route("/delete_projcet/<id>")
@login_required
def delete_project(id):
    """刪除專案路由"""

    user = current_user
    project = Project.query.get(id)

    if project.user != user:
        abort(403)

    user.projects.remove(project)
    db.session.commit()

    flash("刪除成功")

    return redirect(url_for("main.projects"))
