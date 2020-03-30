from flask import Blueprint, Flask
from flask_restx import Api, Resource, fields

from learn_docker_app.api import api


def create_app(test_config=None) -> Flask:
    """
    Creates the app and inserts the given configuration into it.

    Returns
    -------
    Flask
                An instance of the `Flask` app
    """
    api_bp = Blueprint('api', __name__)
    app = Flask(__name__)

    app.register_blueprint(api_bp)
    api.init_app(app)
    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000, debug=True)
