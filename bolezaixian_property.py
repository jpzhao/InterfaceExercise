#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from decimal import Decimal
###源自伯乐在线
# class Persion(object):
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     # @property
#     def full_name(self):
#         return "%s %s"%(self.first_name,self.last_name)
#
# persion=Persion('Mike','Driscoll')
# # persion.last_name="hello world"
# #persion.full_name="hello world haha"
# a=persion.full_name()
# print(a)

class Fees(object):
    def __init__(self):
        self._fee=None

    # def get_fee(self):
    #     return self._fee
    #
    # def set_fee(self,value):
    #     if isinstance(value,str):
    #         self._fee=Decimal(value)
    #     elif isinstance(value,Decimal):
    #         self._fee=value
    #
    # fee=property(get_fee,set_fee)

    def __init__(self):
        self._fee=None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self,value):
        if isinstance(value,str):
            self._fee=Decimal(value)
        elif isinstance(value,Decimal):
            self._fee=value

if __name__=="__main__":
    f=Fees()
    f.fee="2"
    print(f.fee)

