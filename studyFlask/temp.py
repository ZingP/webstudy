#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/30

from flask import Flask, render_template

app = Flask(__name__)

# 可直接定义一个函数，到前端页面去使用
def myhtml(abc):
    return '<h1>liuyouyuan{}</h1>'.format(abc)

@app.route('/index', methods=['GET', 'POST'])
def login():
    return render_template('index.html', yyy=myhtml)    # yyy就相当于前端使用时的函数名字

if __name__ == '__main__':
    app.run()
