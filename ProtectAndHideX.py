#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from math import pi
class ProtectAndHideX(object):
    def __init__(self,x):
        assert isinstance(x,int),'"x" must be an integer!'
        self.__x=~x

    def get_x(self):
        return ~self.__x

    x=property(get_x)

class HideX(object):
    def __init__(self,x):
        self.x=x

    def get_x(self):
        return ~self.__x

    def set_x(self,x):
        assert isinstance(x,int),'"x" must be an integer!'
        self.__x=~x

def get_pi(dummy):
    return pi

class PI(object):
    pi=property(get_pi,doc='Constant "pi"')

    # x=property(get_x,set_x)

# inst=ProtectAndHideX(10)
# print('inst.x=',inst.x)
# inst.x=20

# inst=HideX(20)
# print(inst.x)
# inst.x=30
# print(inst.x)

inst=PI()
print(inst.pi)
print(PI.pi.__doc__)
