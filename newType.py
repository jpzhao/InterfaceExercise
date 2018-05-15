#!/usr/bin/env python
# -*- coding: UTF-8 -*-
def __init__(self):
    self.a=1

def magic(self):
    return self.a

Foo=type('Foo',(object,),{"__doc__":"A class that does nthing.","__init__":__init__,"magic":magic})
foo=Foo()
print (foo)
print(foo.magic)