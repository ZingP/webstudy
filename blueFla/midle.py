#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index"


class MiddleWare:
    def __init__(self, wsgi_app):
        print("123")
        self.wsgi_app = wsgi_app

    def __call__(self, *args, **kwargs):
        print("456")
        return self.wsgi_app(*args, **kwargs)


if __name__ == "__main__":
    app.wsgi_app = MiddleWare(app.wsgi_app)
    app.run(port=9999)

