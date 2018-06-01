#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/29

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
