#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1

from flask import Flask, flash, request, get_flashed_messages, url_for

app = Flask(__name__)
app.secret_key = 'ewqfQWDWEhqweofhqwofn'


@app.route('/')
def index1():
    messages = get_flashed_messages()   # 取出
    print(messages)
    return "index"


@app.route('/set', endpoint="xxx")
def index2():
    v = url_for("xxx")
    flash(v)    # 存入
    return 'hahahah'


if __name__ == "__main__":
    app.run()
