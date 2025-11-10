from flask_login import UserMixin
from sqlalchemy import func
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    _from = db.Column(db.String(150), nullable=False)
    _for = db.Column(db.String(150), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    payment_type = db.Column(db.String(10), nullable=False)

    def __init__(self, date, _from, _for, amount, payment_type):
        self.date = date
        self._from = _from
        self._for = _for
        self.amount = amount
        self.payment_type = payment_type
