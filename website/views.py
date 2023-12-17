from flask import Blueprint
"""Blueprint focuses on routes"""
views = Blueprint('views', __name__)


@views.route('/')
def home():
    """takes us to home page"""
    return "<h1>Test</h1>"