from flask import Flask, request

from .config import app_config
from .models import db
from .settings import ENV_NAME

def create_app(env_name):
    """Creates app"""
    
    # app initialization
    app = Flask(__name__)
    app.config.from_object(app_config[ENV_NAME])
    
    db.init_app(app)

    db.create_all()

    @app.route('/', methods=['GET'])
    def index():
        return 'Your first endpoint is working!'

    return app