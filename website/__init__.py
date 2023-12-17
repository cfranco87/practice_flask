#!/usr/bin/env python3

from flask import Flask


def create_app():
    """function thats creates app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'the yellow pages'
    """secret_key adds security to site"""
    return app