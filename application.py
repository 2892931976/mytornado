#!/usr/bin/env python3
#coding:utf-8

from route import route

import tornado.web
import os

setting = {
  "template_path":os.path.join(os.path.dirname(__file__),"template"),
  "static_path":os.path.join(os.path.dirname(__file__),"static"),
  }

application = tornado.web.Application(
    handlers=route.url,
    **setting
  )
