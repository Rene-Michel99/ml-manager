from flask import Flask
from flask_cors import CORS
from flask_api.routes import blueprint


def create_app(config) -> Flask:
    app = Flask(__name__)

    app.register_blueprint(blueprint, url_prefix='/')
    app.config.from_object(config)

    CORS(app)

    return app
