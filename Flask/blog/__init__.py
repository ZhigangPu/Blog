#! encoding=utf8

from flask import Flask
from blog.blueprints.blog import blog_bp
import os

def create_app(config_name=None):
    if config_name == None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog')
    register_bp(app)
    return app

def register_bp(app):
    app.register_blueprint(blog_bp)

