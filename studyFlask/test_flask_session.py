#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1

"""
pip install redis
pip install flask-session

"""

from flask import Flask, session, redirect
from flask.ext.session import Session


app = Flask(__name__)
app.debug = True
app.secret_key = 'asdfasdfasd'


app.config['SESSION_TYPE'] = 'redis'
from redis import Redis
app.config['SESSION_REDIS'] = Redis(host='****',port='6379')
Session(app)


@app.route('/login')
def login():
    session['username'] = 'alex'
    return redirect('/index')


@app.route('/index')
def index():
    name = session['username']
    return name


if __name__ == '__main__':
    app.run()

