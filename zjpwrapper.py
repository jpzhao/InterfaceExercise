# -*- coding: utf-8 -*-
def deco1(func1):  #func1=wrapper2内存地址
    def wrapper1(*args,**kwargs):
        print('正在运行===》deco1.wrapper1')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1


def deco2(func2): #func2=wrapper3内存地址
    def wrapper2(*args,**kwargs):
        print('正在运行===》deco2.wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2

def deco3(x,y): #func3被装饰对象index函数的内存地址
    def outter3(func3):
        def wrapper3(*args,**kwargs):
            print('正在运行===》deco2.wrapper3 %s %s'%(x,y))
            res3=func3(*args,**kwargs)
            return res3
        return wrapper3
    return outter3

#加载顺序自下而上
@deco1
@deco2
@deco3(111,222)
def index(x,y):
    print('from index %s:%s'%(x,y))

index(1,2)
#执行顺序：自上而下，即wrapper1-wrapper2->wrapper3
#index(1,2)#wrapper1(1,2)