#!/usr/bin/env python3
#coding:utf-8

import tornado.web

import sys

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        #lst = ["python","http://www.cnblogs.com/benlightning/","benlightning@gmail.com"]
        self.render("public/500.html")
