#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class FooFoo(object):
    def foo(self):
        print ('Very important foo() method.')

def barBar():
    print('foo() hidden by barBar()')

bar=FooFoo()
print(bar.foo())
bar.foo='It is no longer here.'
print(bar.foo)
del bar.foo
print(bar.foo())
print(5*'===========')
bar.foo=barBar
bar.foo()
del bar.foo
bar.foo()