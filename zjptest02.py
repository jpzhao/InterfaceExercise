# -*- coding: utf-8 -*-
def f1():
    x=33333
    def f2():
        print('函数f2: ',x)
    return f2
f=f1()

salaries={'siry':3000,'tom':7000,'lili':10000,'jack':2000}
def func(k):
    return salaries[k]
res=max(salaries,key=func)
print(res)
res=max(salaries,key=lambda k:salaries[k])
print(res)

def salary(n):
    if n==1:
        return 5000
    res=salary(n-1)+1000
    return res
res=salary(4)