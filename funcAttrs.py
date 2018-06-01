#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def foo():
    return True

def bar():
    'bar() doec not do much'
    return True

foo.__doc__='foo() does not do much'
foo.tester="""
if foo():
    print ('PASSED')
else:
    print ('FAILED')
"""
print(dir())
for eachAttr in dir():
    print(eval(eachAttr))
    obj=eval(eachAttr)
    if isinstance(obj,type(foo)): #isinstance（） 判断两个类型是否相同
        if hasattr(obj,'__doc__'): #hasattr() 函数用于判断对象是否包含对应的属性。左边是否包含右边
            print ('\nFunction "%s" has a doc string:\n\t%s'%(eachAttr,obj.__doc__))
        if hasattr(obj,'tester'):
            print ('Function "%s" has a tester...execut-ing'%eachAttr)
            exec (obj.tester)
        else:
            print('Function "%s" has no tester...skip-ping'%eachAttr)
    else:
        print('"%s" is not a function'%eachAttr)

