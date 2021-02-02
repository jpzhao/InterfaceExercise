# -*- coding: utf-8 -*-

class School:
    school_name='OLDBOY'

    def __init__(self,nickname,addr):
        self.nickname=nickname
        self.addr=addr
        self.classes=[]

    def related_class(self,class_obj):
        self.classes.append(class_obj)

    def tell_class(self):
        print(self.nickname)
        for class_obj in self.classes:
            class_obj.tell_course()

school_obj1=School('老男孩摩多校区','上海')
school_obj2=School('老男孩迪欧校区','深圳')

class Class:
    def __init__(self, name):
        self.name = name
        self.course = None

    def related_course(self, course_obj):
        self.course = course_obj

    def tell_course(self):
        print('%s' % self.name,end=" ")
        self.course.course_info()


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def course_info(self):
        print('<课程名:%s 周期:%s 价钱:%s>' % (self.name, self.period, self.price))


course_obj1 = Course("python全栈", '6mons', 20000)
course_obj2 = Course("linux运维", '5mons', 10000)
course_obj3 = Course("java全栈", '8mons', 20000)

class_obj1=Class("脱产14期")
class_obj2=Class("脱产15期")
class_obj3=Class("脱产29期")

class_obj1.related_course(course_obj1)
class_obj2.related_course(course_obj2)
class_obj3.related_course(course_obj3)

class_obj1.tell_course()
class_obj2.tell_course()
class_obj3.tell_course()

school_obj1.related_class(class_obj1)
school_obj1.related_class(class_obj2)
school_obj2.related_class(class_obj3)
school_obj1.tell_class()
school_obj2.tell_class()

class Student:
    pass