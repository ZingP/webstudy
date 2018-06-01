#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1
from flask import Blueprint

account = Blueprint('account', __name__, url_prefix='/yyy', template_folder='', static_folder='')
# 可以为每个蓝图单独指定一个模板文件和静态文件

@account.route('/')
def hello_world():
    return 'Hello blue!'
