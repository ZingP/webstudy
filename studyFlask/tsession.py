#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/31

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # 从session移除username
    session.pop('username', None)
    return redirect(url_for('index'))


# 如果要加密session，在此处设置秘钥
app.secret_key = 'reffbyujHSDU!ASn#UIddODN*1243 WEfM'

if __name__ == '__main__':
    app.run()
