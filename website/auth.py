from flask import Blueprint, render_template
"""render_template will call files named, ex login.html"""
from flask_sqlalchemy import SQLAlchemy
"""Flask_sqlalchemy module that can use databases"""

"""db  instance will be used to interact w database in flask"""
db = SQLAlchemy()
"""variable DB_NAME to store the name of the database file, database.db"""
DB_NAME = "database.db"

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    """POST REQUEST asks for info, email, name, passwordsin form"""
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
    """if POST doesnt meet criteria then it will flash error, using flash module"""
    if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('')

    return render_template("signup.html")