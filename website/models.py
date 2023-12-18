from . import db 
""" importing db from website package"""
from flask_login import UserMixin
"""flask module that login user info"""

class User(db.Models, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150). unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))