#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/30

from flask import Flask

app = Flask(__name__)

# def auth(func):
#     def inner(*args, **kwargs):
#         print('before')
#         result = func(*args, **kwargs)
#         print('after')
#         return result
#
#     return inner
#
#
# @app.route('/index.html', methods=['GET', 'POST'], endpoint='index')
# @auth       # 装饰器一定要放在app.route这个装饰器之下
# def index():
#     return 'Index'
#
#
# def index():
#     return "Index"
#
# # app.add_url_rule(rule='/index.html', endpoint="index", view_func=index, methods=["GET", "POST"])
#
# app.add_url_rule(rule='/index.html', endpoint="index", view_func=index, methods=["GET", "POST"])
# app.view_functions['index'] = index
#
# 或
#
#

# from flask import views
# def auth(func):
#     def inner(*args, **kwargs):
#         print('before')
#         result = func(*args, **kwargs)
#         print('after')
#         return result
#
#     return inner


# class IndexView(views.View):
#     methods = ['GET']
#     decorators = [auth, ]
#
#     def dispatch_request(self):
#         print('Index')
#         return 'Index!'
#
#
# app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name=endpoint 反向url使用
#
# 或
#
from flask import views
def auth(func):
    def inner(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result
    return inner

class IndexView(views.MethodView):
    methods = ['GET', 'POST']
    decorators = [auth, ]

    def get(self):
        return 'Index.GET'

    def post(self):
        return 'Index.POST'

app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name=endpoint


# @app.route和app.add_url_rule参数：

# rule,                  URL规则

# view_func,             视图函数名称

# defaults = None,       默认值, 当URL中无参数，函数需要参数时，使用defaults = {'k': 'v'}为函数提供参数

# endpoint = None,       名称，用于反向生成URL，即： url_for('名称')

# methods = None,        允许的请求方式，如：["GET", "POST"]

# strict_slashes = None, 对URL最后的 / 符号是否严格要求，
# 如：@app.route('/index', strict_slashes=False)访问http: //www.xx.com/index/或http://www.xx.com/index均可
#    @app.route('/index', strict_slashes=True)仅能访问http://www.xx.com/index

# redirect_to = None, 重定向到指定地址如：@app.route('/index/<int:nid>', redirect_to='/home/<nid>')
# 或
# def func(adapter, nid):
#     return "/home/888"
# @app.route('/index/<int:nid>', redirect_to=func)

# subdomain = None, 子域名访问
# app = Flask(import_name=__name__)
# app.config['SERVER_NAME'] = 'lyy.com:5000'
# @app.route("/", subdomain="admin")
# def static_index():
#     """Flask supports static subdomains
#     This is available at static.your-domain.tld"""
#     return "static.your-domain.tld"
#
# @app.route("/dynamic", subdomain="<username>")
# def username_index(username):
#     """Dynamic subdomains are also supported
#     Try going to user1.your-domain.tld/dynamic"""
#     return username + ".your-domain.tld"


if __name__ == '__main__':
    app.run()

