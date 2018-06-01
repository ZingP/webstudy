#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1

from .. import app

@app.route('/')
def hello_world():
    return 'Hello World!'