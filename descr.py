#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import pickle #对象序列化包

class FileDescr(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError("%r used before assignment" % self.name)
        try:
            f = open(self.name, 'rb')
            val = pickle.load(f)
            f.close()
            return val
        except(pickle.UnpicklingError, IOError, EOFError, AttributeError, ImportError, IndexError) as e:
            #################################
            #1. PickleError：封装和拆封时出现的异常类，继承自Exception
            #2. PicklingError: 遇到不可封装的对象时出现的异常，继承自PickleError
            #3. UnPicklingError: 拆封对象过程中出现的异常，继承自PickleError
            #4. IOError的出现：打开一个不存在的文件
            #5. EOFError:当从 raw_input() 与 input() 函数输入，到达文件末尾时触发
            #6. AttributeError:属性引用或赋值失败的情况下引发
            #7. ImportError: 当一个 import 语句失败时触发
            #8. IndexError: 当在一个序列中没有找到一个索引时引发
            raise AttributeError("could not read %r: %s " % self.name)

    def __set__(self, obj, val):
        print(self)
        print(obj)
        print(val)
        f = open(self.name, 'wb')
        try:
            try:
                pickle.dump(val, f)
                FileDescr.saved.append(self.name)
            except(TypeError, pickle.PicklingError) as e:
                raise AttributeError("could not pickle %r" % self.name)
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except(OSError, ValueError) as e:
            pass

class MyFileVarClass(object):
    foo = FileDescr('foo')
    bar = FileDescr('bar')

fvc = MyFileVarClass()
# print(fvc.foo)
fvc.foo = 42
fvc.bar = 'leanna'
# print(fvc.foo,fvc.bar)
del fvc.foo
del fvc.bar
print(fvc.foo,fvc.bar)
fvc.foo=__builtins__
#示例中，并没有用到obj的实例。别把obj和self搞混淆，这个self是指描述符的实例，而不是类的实例
########################练习#######################
# class A(object):
#     def __init__(self,name):
#         self.name=name
#
# def save(obj):
#     return (obj.__class__,obj.__dict__)
#
# a=A('mcc')
# print(save(a))
