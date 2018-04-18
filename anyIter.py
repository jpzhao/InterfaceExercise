#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class AnyIter(object):
    def __init__(self,data,safe=False):
        self.safe=safe
        self.iter=iter(data)

    def __iter__(self):
        return self

    def __next__(self,howmany=1):
        retval=[]
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

a=AnyIter(range(2))
gdb(a)
for j in range(1,5):
    print (j, ":" ,a.__next__(j))



