__author__ = 'lorenzo'

import os

from flask import Flask
from flask import render_template, redirect, url_for, request
from flask.ext.wtf import Form

dir = os.path.dirname(__file__)


class NewsForm(Form):
    pass

app = Flask(__name__)
app.config['DEBUG'] = False
app.config.from_object('config')

@app.route("/")
def hello():
    if request.args.get('message'):
        return render_template('index.html', message=request.args.get('message'))
    form = NewsForm()
    return render_template('index.html', form=form)

@app.route("/subscribe", methods=['POST'])
def subscribe():
    mail = request.form['email']
    data = open(dir+'/data/newsletter.save').read()
    position = data.find(mail)
    if position == -1:
        with open(dir+'/data/newsletter.save', 'a') as f:
            f.write(mail+' \n')
        return redirect(url_for('.hello', message=message_ok))

    return redirect(url_for('.hello', message=message_already))


message_ok = 'You subscribed the newsletter. Wait for confirmation email. Thanks for your interest!'
message_already = 'You already subscribed with this email address. Wait for confirmation in the next 24 hours.'


if __name__ == "__main__":
    app.run()
