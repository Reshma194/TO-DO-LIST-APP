from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()  # SQLAlchemy instance

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "mykey"

    # Absolute path to ensure database is in the same folder as __init__.py
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Import blueprints
    from app.routes.auth import auth_bp
    from app.routes.task import tasks_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app
