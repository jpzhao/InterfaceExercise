#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Monkey:
    '''
    猴子类
    '''
    def __init__(self,name):
        self.name=name

class Monkeys:
    '''
    猴群
    '''
    _monkeys=[]
    def __init__(self,monkeys):
        self._monkeys=monkeys

    def __getitem__(self, position):
        return self._monkeys[position]

    def __len__(self):
        return len(self._monkeys)

    def __repr__(self):
        return "<monkeys {}>".format(','.join((m.name for m in self)))

m1=Monkey("猴1")
m2=Monkey("猴2")
m3=Monkey("猴3")
monkeys=Monkeys([m1,m2,m3])
print(monkeys)

from random import shuffle
def set_monkey(monkeys,position,monkey):
    monkeys._monkeys[position]=monkey
Monkeys.__setitem__=set_monkey
shuffle(monkeys)
print(monkeys)