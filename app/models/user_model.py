from werkzeug.security import generate_password_hash,check_password_hash
from app.database import db
from flask_login import UserMixin
import json


class User(db.Model,UserMixin):
    __tablename__="users"


    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50), nullable=False)
    password_hash=db.Column(db.String(50),nullable=False)
    phone=db.Column(db.String(50),nullable=False)
    roles=db.Column(db.String(50),nullable=False)


    def __init__(self,name,email,password,phone,roles=["customer"]):
        self.username=name
        self.email=email
        self.password_hash=generate_password_hash(password)
        self.phone=phone
        self.roles=json.dumps(roles)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def has_role(self,role):
        return self.role==role


    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()