#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1

from flask import Flask
from .views.account import account
from .views.host import host

app = Flask(__name__)

app.register_blueprint(account)     # 注册蓝图
app.register_blueprint(host)

