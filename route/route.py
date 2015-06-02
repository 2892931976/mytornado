#!/usr/bin/env python
#coding:utf-8

import sys

from controller.index import IndexHandler

handlers=[
    (r'/', IndexHandler),
    ]
