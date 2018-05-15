#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from operator import *
vec1=[12,24]
vec2=[2,3,4]
opvec=(add,sub,mul,truediv)
for eachOp in opvec:
    for i in vec1:
        for j in vec2:
            print('%s(%d,%d) = %d'%(eachOp.__name__,i,j,eachOp(i,j)))
abcd=truediv(12,3)