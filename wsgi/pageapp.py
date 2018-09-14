__author__ = 'lorenzo'

import os

from flask import Flask
from flask import render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/graph19")
def testnode():
    return render_template('testsonly.html')


if __name__ == "__main__":
    app.run()
