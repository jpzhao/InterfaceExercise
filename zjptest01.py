# -*- coding: utf-8 -*-

class Fun_A(object):
    def __init__(self):
        self.name=None
        self.age=0

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

class Fun_B(Fun_A):
    def __call__(self, *args, **kwargs):
        print(self)

if isinstance(Fun_A,type):
    #isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
    print(type(Fun_A))

if issubclass(Fun_A,object):
    #issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
    print(type(Fun_A))

funb=Fun_B()
if issubclass(Fun_B,(Fun_A,object)):
    pass
    # raise TypeError("type error")

if getattr(funb,'getName1',None):
    print(funb.getName())

print(callable(funb),dir(funb))
funb()
