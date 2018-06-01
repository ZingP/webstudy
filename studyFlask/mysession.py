#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/31

from flask import Flask
from flask import session
from session import MySessionInterface
app = Flask(__name__)

app.secret_key = 'asdWhuDW!@##%bxwy'
app.session_interface = MySessionInterface()

@app.route('/login', methods=['GET', "POST"])
def login():
    print(session)
    session['user1'] = 'lyy'
    session['user2'] = 'yy'
    del session['user2']
    print(session)
    return "test mysession"

if __name__ == '__main__':
    app.run()
