from flask import Flask
from .config import DevelopmentConfig
from flask_migrate import Migrate
from .database import db  # Import db instance


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # import and register blueprints
    from .views import home, login, register
    app.register_blueprint(home.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(register.bp)

    db.init_app(app)  # Initialize db with app
    migrate = Migrate(app, db)  # Initialize migrate with app and db

    with app.app_context():
        db.create_all()  # Create tables

    return app
