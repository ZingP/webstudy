#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/28

from werkzeug.wrappers import Request, Response

@Request.application
def hello(request):
    print(request)
    return Response('Hello Werkzeug!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, hello)
