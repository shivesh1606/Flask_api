from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from .config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])

    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Flask-RESTful API
    api = Api(app)
    
    # Register Blueprints or routes
    from .accounts.urls import register_routes
    register_routes(api)

    return app
