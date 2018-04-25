#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
def findcaller(func):
    def wrapper(*args, **kwargs):
        f = sys._getframe()
        filename = f.f_back.f_code.co_filename
        lineno = f.f_back.f_lineno
        print('######################################')
        print('caller filename is ', filename)
        print('caller lineno is', lineno)
        print('the passed args is', args, kwargs)
        print('######################################')
        func(*args, **kwargs)
    return wrapper

class Tree(object):
    def __init__(self,name):
        self.name=name
        self.cate='plant'

    # @findcaller
    def __getattribute__(self, *args,**kwargs):
        if args[0]=="大树":
            print("log 大树")
            return "我爱大树"
        else:
            return object.__getattribute__(self,*args,**kwargs)
ttuple=("小树","大树")
aa=Tree(ttuple)
print(aa.name)
print(aa.cate)