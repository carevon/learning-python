import os

from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.environ.get("DATABASE_URL",  "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    @app.before_request
    def create_tables():
        if not hasattr(app, 'tables_created'):
            with app.app_context():
                db.create_all()
            app.tables_created = True

    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)
    return app
