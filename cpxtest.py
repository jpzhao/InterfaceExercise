#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
# def a(func):
#     def b():
#         print('abc')
#         return func
#     return b
#
# @a
# def c():
#     print('def')
# c()

# def test():
#     time.sleep(2)
#     print("test is running!")
#
# def deco(func):
#     start=time.time()
#     func()
#     stop=time.time()
#     print(stop-start)
#     print(func)
#     return func
# t=deco(test)
# t()
# test()


def timer(func):
    def deco():
        start=time.time()
        func()
        stop=time.time()
        print(stop-start)
    return deco

@timer
def test():
    time.sleep(2)
    print("test is running!")

test()
################################
# class SlottedClass(object):
#     __slots__ = ('foo','boo')
#
# c=SlottedClass()
# c.foo=42
# c.abc=33
# print(c.abc)

