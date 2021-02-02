# -*- coding: utf-8 -*-

def deco1(func1):#func1=wrapp2内存地址
    def wrapper1(*args,**kwargs):
        print('running==>deco1.wrapper1')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1

def deco2(func2):#func2=wrapp3内存地址
    def wrapper2(*args,**kwargs):
        print('running==>deco2.wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2

def deco3(x,y):
    def outter3(func3):#func3被装饰对象index函数的内存地址
        def wrapper3(*args,**kwargs):
            print('running==>outter3.deco3.wrapper3 %s %s'%(x,y))
            res3=func3(*args,**kwargs)
            return res3
        return wrapper3
    return outter3

#加载顺序自下而上
@deco1         #index=deco1(wrapper2内存地址)==>wrapper1==>index=wrapper1的内存地址
@deco2         #index=deco2(wrapper3内存地址)==>wrapper2==>index=wrapper2的内存地址
@deco3(555,666)#@outter3==>index=outter3(index)==>index=wrapper3的内存地址
def index(x,y):
    print('home pase %s,%s'%(x,y))

index(777,888)
#执行顺序：自上而下，即wrapper1->wrapper2->wrapper3