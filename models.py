from datetime import date

from extensions import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)   # 'income' किंवा 'expense'
    date = db.Column(db.Date, nullable=False, default=date.today)
    note = db.Column(db.String(200))