__author__ = 'lorenzo'

from flask import Flask
from wsgi.homepage import html


app = Flask(__name__)

@app.route("/")
def hello():
    return html


if __name__ == "__main__":
    app.run()
