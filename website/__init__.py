from flask import Flask


def create_app():
    """function thats creates app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'the yellow pages'
    """secret_key adds security to site"""
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    """app.config is telling where the database is located"""
    db.init_app(app)
    """enables you ti use SQL within Flask app to work with databases"""

    """registering view, auth"""
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app