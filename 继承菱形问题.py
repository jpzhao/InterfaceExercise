#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B,C):
    pass

obj=D()
obj.test()
print(D.mro())