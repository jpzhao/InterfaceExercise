#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class DevNull1(object):
	def __get__(self, obj,typ=None):
		pass

	def __set__(self,obj,vall):
		pass

class DevNull2(object):
	def __get__(self,obj,typ=None):
		print('Accessing attribute... ignoring') #访问属性忽略

	def __set__(self,obj,val):
		print('Attempt to assign %r... ignoring'%(val)) #尝试设置忽略

class DevNull3(object):
	def __init__(self,name=None):
		self.name=name

	def __get__(self,obj,typ=None):
		print('Accessing [%s]...ignoring'%self.name)

	def __set__(self,obj,val):
		print ('Assigning %r to [%s]...ignoring'%(val,self.name))

class C1(object):
	foo=DevNull1()

class C2(object):
	foo=DevNull2()

class C3(object):
	foo=DevNull3('foo')

c1=C1()
c1.foo='bar'
print('c1.foo contains:',c1.foo)  #contains 包含
print('++++++++++++++++++++++++++++++')

c2=C2()
c2.foo='bar'
x=c2.foo
print('c2.foo contains:',x)
print('++++++++++++++++++++++++++++++')

c3=C3()
c3.foo='bar'
x=c3.foo
print('c3.foo contains:',x)
print('Let us try to sneak it into c3 instance...')
c3.__dict__['foo']='bar'
x=c3.foo
print('c3.foo contains:',x)
print("c3.__dict__['foo']contains:%r"%c3.__dict__['foo'],"...why?!?")