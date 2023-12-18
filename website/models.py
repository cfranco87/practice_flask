from . import db 
""" importing db from website package"""
from flask_login import UserMixin
"""flask module that login user info"""
from sqlalchemy.sql import func
"""By importing func, you gain access to a collection of SQL
functions that you can use when constructing queries with SQLAlchemy."""

class Note(db.Model):
    """class for notes, datetime will automatically give current time,
    comment 10000 char max, id is integer and primary key for note"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.column(db.String(10000))
    date= db.Column(db.Datetime(timezone=True), default=func.now())
    """creating relationship between note and user using foreign key"""
    user_id = db.column(db.Integer, db.ForeignKey=('user.id'))


class User(db.Models, UserMixin):
    """class for User that inherits from db.Model and UserMixin"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150). unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    """these go into database, so its always db.Column, 
    db.String(150), this is max char, and id being the primary key
    while email we give it a unique attr, so no one else has the email"""