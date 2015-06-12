#!/usr/bin/python3
# coding:utf-8

import tornado.web

class LoginHandler(tornado.web.RequestHandler):
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
