# -*- coding: utf-8 -*-
class oldBodyPeople():
    school="OLDBODY"
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class student(oldBodyPeople):
    def tell_info(self):
        print('My name is %s,how old are you %s'%(self.name,self.age))

class teacher(oldBodyPeople):
    def __init__(self,name,age,sex,salary,level):
        oldBodyPeople.__init__(self,name,age,sex)
        self.salary=salary
        self.level=level

    def score(self):
        print('老师正在给%s打分'%(self.name))