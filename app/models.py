__author__ = 'Leo'
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    num_picture = db.Column(db.Integer, primary_key = True)
    text_answer = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

def __repr__(self):
    return '<Answer %r>' % (self.text_answer)
