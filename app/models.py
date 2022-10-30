from . import db

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    status = db.Column(db.String(20))
    unit = db.Column(db.String(20))
    comment = db.Column(db.String(20))
