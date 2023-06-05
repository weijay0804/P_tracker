'''
Author: andy
Date: 2023-06-06 00:26:39
LastEditors: andy
LastEditTime: 2023-06-06 06:17:20
Description: database ORM model
'''

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from . import db, login_manager


class User(db.Model, UserMixin):
    '''user table'''

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    # 建立與 record table 一對多關係
    records = db.relationship(
        'Record', back_populates="user", lazy="joined", cascade="delete, delete-orphan"
    )

    # 建立與 record_type table 一對多關係
    record_types = db.relationship(
        'RecordType', back_populates="user", lazy="joined", cascade="delete, delete-orphan"
    )

    # 建立與 project 一對多關係
    projects = db.relationship(
        'Project', back_populates="user", lazy="joined", cascade="delete, delete-orphan"
    )

    @property
    def password(self):
        '''讓外部無法讀取 pssword 屬性'''
        raise AttributeError('Password is not a readablb attribute.')

    @password.setter
    def password(self, password: str):
        '''將密碼雜湊後儲存至資料庫'''

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        '''檢查使用者密碼是否正確'''

        return check_password_hash(self.password_hash, password)


class Record(db.Model):
    """record table"""

    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('record_type.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    name = db.Column(db.String(30), index=True)
    price = db.Column(db.Float)
    desc = db.Column(db.Text)
    date = db.Column(db.Date)

    user = db.relationship('User', back_populates="records")
    type = db.relationship('RecordType', back_populates="records")
    project = db.relationship('Project', back_populates="records")


class RecordType(db.Model):
    """record_type table"""

    __tablename__ = "record_type"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(30), index=True)
    desc = db.Column(db.Text)

    user = db.relationship('User', back_populates="record_types")

    # 建立與 record table 一對多關係
    records = db.relationship(
        'Record', back_populates="type", lazy="joined", cascade="delete, delete-orphan"
    )


class Project(db.Model):
    """project table"""

    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(30), index=True)
    desc = db.Column(db.Text)
    price = db.Column(db.Float)
    current_price = db.Column(db.Float)
    date = db.Column(db.Date)

    user = db.relationship('User', back_populates="project")

    # 建立與 record table 一對多關係
    records = db.relationship('Record', back_populates="project", lazy="joined")


@login_manager.user_loader
def load_user(user_id):
    '''載入使用者'''
    return User.query.get(int(user_id))
