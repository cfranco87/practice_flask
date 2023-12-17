from flask import Blueprint, render_template
"""Blueprint focuses on routes"""
views = Blueprint('views', __name__)


@views.route('/')
def home():
    """takes us to home page"""
    return render_template("home.html")