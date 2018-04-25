#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class C(object):
    a='abc'
    def __getattribute__(self, *args,**kwargs):
        print("__getattribute__() is called")
        if args[0]=='a':
            return object.__getattribute__(self,*args,**kwargs)
        else:
            print('调用函数foo()')
            return object.__getattribute__(self,'foo')()

    def foo(self):
        return "hello"

if __name__=='__main__':
    c=C()
    print (c.foo)


#__getattribute__是访问属性的方法，我们可以通过方法重写来扩展方法的功能。
# 对于python来说，属性或者函数都可以被理解成一个属性，且可以通过__getattribute__获取。
# 当获取属性时，直接return object.__getattribute__(self, *args, **kwargs)
# 如果需要获取某个方法的返回值时，则需要在函数后面加上一个()即可。如果不加的话，返回的是函数引用地址。见下方代码：