__author__ = 'lorenzo'

from app import app
from homepage import html


@app.route('/')
@app.route('/index')
def index():
    return html
