#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    """docstring for baseHandler"""

    def initialize(self):
        redis = self.application.redis
        self.session = self.application.SessionHandler(self, redis, session_lifetime=20)
        self.current_password = self.session.password

    def get_current_user(self):
        return self.get_secure_cookie("username")
