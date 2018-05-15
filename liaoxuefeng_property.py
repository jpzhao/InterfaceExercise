#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Student(object):

#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integet!')
#         if value<0 or value>100:
#             raise ValueError('score must between 0 ~100!')
#         self._score=value
#
# s=Student()
# s.set_score(100)
# chengji=s.get_score()
# print(chengji)
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integet!')
        if value<0 or value>100:
            raise ValueError('score must between 0 ~100!')
        self._score=value

s=Student()
s.score=100
chengji=s.score
print(chengji)