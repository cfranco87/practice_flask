from flask import Flask


def create_app():
    """function thats creates app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'the yellow pages'
    """secret_key adds security to site"""

    """registering view, auth"""
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app