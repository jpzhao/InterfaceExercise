#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 使用函数装饰器实现单例
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


@singleton
class Cls(object):
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))


# 使用类装饰器实现单例
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls2(object):
    def __init__(self):
        pass


cls3 = Cls2()
cls4 = Cls2()
print(id(cls3) == id(cls4))

# class Cls3():
#     pass
# Cls3=Singleton(Cls3)
# cls5=Cls3()
# cls6=Cls3()
# print(id(cls5)==id(cls6))

# 简单来说，元类(metaclass) 可以通过方法 __metaclass__ 创造了类(class)，而类(class)通过方法 __new__ 创造了实例(instance)。

# 使用 new 关键字实现单例模式
class Single(object):
    _instance=None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance=object.__new__(cls,*args,**kw)
            return cls._instance
    def __init__(self):
        pass

single1=Single()
single2=Single()
print(id(single1)==id(single2))

#使用 metaclass 实现单例模式

# def func(self):
#     print("do sth")
#
# Klass = type("Klass", (), {"func": func})
#
# c = Klass()
# c.func()

class SingLeton(type):
    _instances={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls]=super(SingLeton,cls).__call__(*args,**kwargs)
            return cls._instances[cls]

class Cls4(metaclass=SingLeton):
    pass

cls7=Cls4()
cls8=Cls4()
print(id(cls7)==id(cls8))