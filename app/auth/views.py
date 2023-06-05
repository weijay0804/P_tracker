'''
Author: andy
Date: 2023-06-06 01:07:08
LastEditors: andy
LastEditTime: 2023-06-06 04:34:15
Description: 使用者認證試圖
'''

from flask import request, flash, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user

from app import db
from app.db_model import User, RecordType
from . import auth


@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''使用者註冊路由'''

    # 處理表單
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 如果 email 存在資料庫，就發出錯誤訊息
        if User.query.filter_by(email=email).first():
            flash('Email 已經被使用')
            return render_template('auth/register.html', email=email, username=username)

        # 如果 username 存在資料庫，就發出錯誤訊息
        if User.query.filter_by(username=username).first():
            flash('使用者名稱已存在')
            return render_template('auth/register.html', email=email)

        # 如果密碼不相同，就發出錯誤訊息
        if password1 != password2:
            flash('密碼必須相同')
            return render_template('auth/register.html', email=email, username=username)

        u = User(email=email, username=username, password=password1)
        db.session.add(u)
        db.session.commit()

        # 先新增幾種預設的種類
        type1 = RecordType(name="食物", desc="食物類別")
        type2 = RecordType(name="交通", desc="交通類別")
        type3 = RecordType(name="娛樂", desc="娛樂類別")

        u.record_types.append(type1)
        u.record_types.append(type2)
        u.record_types.append(type3)

        db.session.add_all([type1, type2, type3])

        db.session.commit()

        flash('註冊成功')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''使用者登入路由'''

    # 處理表單
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        u = User.query.filter_by(email=email).first()

        if not u or not u.verify_password(password):
            flash('帳號或密碼錯誤')

            return redirect(url_for('auth.login'))
        login_user(u)
        return redirect(url_for('main.index'))

    return render_template('auth/login.html')


@auth.route('/logout')
@login_required
def logout():
    '''使用者登出路由'''

    # 更新使用者登入時間
    logout_user()
    flash('你已經登出')
    return redirect(url_for('main.index'))
