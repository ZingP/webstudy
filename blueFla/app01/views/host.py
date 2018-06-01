#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1

from flask import Blueprint

host = Blueprint('host', __name__)

@host.route('/host.html')
def hello_host():
    return "host.."
