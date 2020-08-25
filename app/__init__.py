from flask import Flask
from flask import current_app
import math
import json

def create_app():
    application = Flask(__name__)
    print('name', __name__)
    application.config.from_object("app.config.DevelopmentConfig")

    from api.api import bp
    application.register_blueprint(bp)

    @application.route('/')
    def index():
        return "Hello!"
    return application

