import os
import logging
from flask import Flask, Blueprint


def create_app(blueprints: list[Blueprint]) -> Flask:
    """Create a Flask app"""
    app = Flask(__name__)

    # Load the app config based on the APP_CONFIG environment variable
    environment = os.getenv('APP_CONFIG')
    if environment == 'dev':
        app.config.from_pyfile('config/development.py')
    else:
        app.config.from_pyfile('config/production.py')

    # Register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app


def get_logger(name: str, filename: str) -> logging.Logger:
    """Get or create a logger with a file handler"""
    logger = logging.getLogger(name)
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    file_handler = logging.FileHandler(filename, encoding='utf8')
    file_handler.setFormatter(log_formatter)

    logger.addHandler(file_handler)
    return logger
