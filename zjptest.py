# -*- coding: utf-8 -*-
import os

ecs=open(r'data','rb')
print(dir(ecs))

class Foo():
    def __init__(self):
        def __str__(self):
            print(self)

    def __enter__(self):
        print("begin")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end")

foo=Foo()
with foo:
    foo.a="进行中。。。"
    print(foo.a)

# print(os.path.join())