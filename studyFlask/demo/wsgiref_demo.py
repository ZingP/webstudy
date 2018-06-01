#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/29

from wsgiref.simple_server import make_server


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

