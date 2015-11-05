#!/usr/bin/env python3
# coding:utf-8

from route import route

import tornado.web
import os
from utils.session import SessionHandler
from redis import client

setting = {
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    # 带签名的cookie
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    # 跨站伪造请求(Cross-site request forgery) 防范策略 xsrf_cookies
    # "xsrf_cookies": "Ture",
    "login_url": "/login",
    }

application = tornado.web.Application(
    route.handlers,
    **setting
    )

application.redis = client.Redis()
application.SessionHandler = SessionHandler
