from flask import Flask
from app.config import Config
from app.controllers.cipher_controller import cipher_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(cipher_bp)

    return app
