#!/usr/bin/env python
from random import choice
class randSeq(object):
    def __init__(self,seq):
        self.data=seq

    def __iter__(self):
        return self

    def __next__(self):      #python2+:next(), python3+:__next()__
        return choice(self.data)

tst=randSeq(['abc','ab'])
for i in tst:
    print(i)
