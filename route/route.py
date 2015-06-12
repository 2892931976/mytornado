#!/usr/bin/env python
#coding:utf-8

import sys

import controller.index as index

import controller.public as public

handlers=[
    (r'/', index.IndexHandler),
    (r'/login',public.LoginHandler),
    ]
