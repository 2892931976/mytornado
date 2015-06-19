#!/usr/bin/env python3
# coding:utf-8

from controller.base import BaseHandler
import tornado.web


class IndexHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # lst = ["python","http://www.cnblogs.com/benlightning/","benlightning@gmail.com"]
        # self.write(self.get_argument('name'))
        print(self.application.redis)
        print(self.application.redis.hget(self.session._id, 'password'))
        print(self.session._id)
        self.render("index/index.html")
