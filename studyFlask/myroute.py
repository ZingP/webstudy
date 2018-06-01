#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/30
from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自定义通过正则匹配url
class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex   # 会按照传入的正则表达式进行匹配

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value: 
        :return: 
        """
        return value

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value: 
        :return: 
        """
        val = super(RegexConverter, self).to_url(value)
        return val

# 添加到flask中
app.url_map.converters['regex'] = RegexConverter


@app.route('/index/<regex("\d+"):nid>/<int:bid>')
def index(nid, bid):
    print(nid)
    url = url_for('index', nid=nid, bid=bid)    # 反向生成url
    print(url)
    return 'Index'


if __name__ == '__main__':
    app.run()

