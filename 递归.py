# -*- coding: utf-8 -*-
import sys
print(sys.getrecursionlimit())#递归上限数

n=0
while True:
    if n==10:
        break
    n+=1
    print(n)

def f1(n):
    if n==10:
        return
    n+=1
    print(n)
    f1(n)
f1(0)

def age(n):
    if n==1:
        return 18
    return age(n-1)+10
res=age(5)
print(res)

def factorialtest(n):
    if(n==1):
        return n
    res=n*factorialtest(n-1)
    return res

