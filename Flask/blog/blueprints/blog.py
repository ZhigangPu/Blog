#! encodind=utf8

from flask import Blueprint

blog_bp = Blueprint('auth', __name__)

@blog_bp.route('/blog')
def index():
    return '<h1>Hello World!</h1>'
