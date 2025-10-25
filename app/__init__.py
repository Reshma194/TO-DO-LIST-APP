from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()  # SQLAlchemy instance

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "mykey"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db_path = os.path.abspath('todo.db')
    print(f"SQLite database path: {db_path}")  # corrected typo

    # Connect database to app
    db.init_app(app)  # better than db.__init__(app)

    # Import blueprints
    from app.routes.auth import auth_bp
    from app.routes.task import tasks_bp  # corrected import

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app
