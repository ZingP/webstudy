#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/1

from flask import Flask
app = Flask(__name__)

from .views import account

