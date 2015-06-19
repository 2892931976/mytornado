#!/usr/bin/python3
# coding:utf-8

from controller.base import BaseHandler
import tornado.web


class LoginHandler(tornado.web.RequestHandler):
    """docstring for baseHandler"""
    def initialize(self):
        redis = self.application.redis
        self.session = self.application.SessionHandler(self, redis, session_lifetime=20)
        self.current_password = self.session.password

    def get(self):
        if self.current_user and not self.current_password:
            self.render('public/login.html')
        else:
            self.render('public/login.html')

    def post(self):
        username = self.get_secure_cookie("username") or self.get_argument("username")
        password = self.get_argument("password")
        if not self.current_password:
            if username == "admin" and password == "123456":
                self.set_secure_cookie("username", username)
                self.session.password = password
                self.redirect("/")
            else:
                raise tornado.web.HTTPError(403, "user or password error")
        else:
            self.redirect("/")


class LogoutHandler(BaseHandler):
    def get(self):
            self.clear_cookie("username")
            self.redirect("/")
