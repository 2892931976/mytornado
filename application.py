#!/usr/bin/env python3
# coding:utf-8

from route import route

import tornado.web
import os
from utils.session import SessionHandler

setting = {
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "debug":True,
    "cookie_secret":"61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=", # 带签名的cookie
    "login_url":"/login",
    #"xsrf_cookies":"Ture", # 跨站伪造请求(Cross-site request forgery) 防范策略 xsrf_cookies
  }

application = tornado.web.Application(
    handlers=route.handlers,
    **setting
  )
application.SessionHandler = SessionHandler
