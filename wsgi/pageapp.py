__author__ = 'lorenzo'

import os

from flask import Flask
from flask import render_template, redirect, url_for, request
from flask.ext.wtf import Form

if 'OPENSHIFT_DATA_DIR' in os.environ:
    store = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'newsletter.save')
else:
    store = os.path.join(os.path.dirname(__file__), 'newsletter.save')


class NewsForm(Form):
    pass

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')

@app.route("/")
def hello():
    if request.args.get('message'):
        return render_template('index.html', message=request.args.get('message'))
    form = NewsForm()
    return render_template('index.html', form=form)

@app.route("/graph19")
def testnode():
    return render_template('testsonly.html')

@app.route("/subscribe", methods=['POST'])
def subscribe():
    mail = request.form['email']
    data = open(store).read()
    position = data.find(mail)
    if position == -1:
        with open(store, 'a') as f:
            f.write(mail+' \n')
        return redirect(url_for('.hello', message=message_ok))

    return redirect(url_for('.hello', message=message_already))


message_ok = 'You subscribed the newsletter. Wait for confirmation email. Thanks for your interest!'
message_already = 'You already subscribed with this email address. Wait for confirmation in the next 24 hours.'


if __name__ == "__main__":
    app.run()
