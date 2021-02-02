# -*- coding: utf-8 -*-
class People:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def set_name(self,val):
        if type(val) is not str:
            print('必须传入str类型')
            return
        self.__name=val

    def del_name(self):
        print('不能删除')

    name = property(get_name, set_name, del_name)

class Car:
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        self.__name=val

    @name.deleter
    def name(self):
        print('不能删除')

obj=People('alan')
print(obj.name)
obj.name=18
del obj.name

car=Car('奥迪A8')
print(car.name)
car.name='宝马Z3'
print(car.name)
del car.name