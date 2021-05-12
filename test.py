# -*- coding: utf-8 -*-
"""
从大到小排序
"""

# def call_fun(fun):
#     def warpe(*args,**kwargs):
#         import time
#         stat=time.time()
#         print(stat)
#         fun(*args,**kwargs)
#         time.sleep(0.5)
#         end=time.time()
#         print(end-stat)
#     return warpe
#
# @call_fun
# def sort(testlist):
#     testlen = len(testlist)
#     for i in range(0, testlen - 1):
#         for j in range(i + 1, testlen):
#             if not testlist[i] < testlist[j]:
#                 testlist[i], testlist[j] = testlist[j], testlist[i]
#     print(testlist)
# testlist = [12, 43, 55, 21, 8, 10, 33, 86]
# sort(testlist)

# def fun(x,y):
#     return x+y
#
# a=fun(2,4)
#
# f'{print(dir(a))}'

demo1_list=[
    {"key1":"a1","key2":"b1","key3":"c1"},
    {"key1":"a1","key2":"b1","key3":"c2"},
    {"key1":"a1","key2":"b2","key3":"c3"},
    {"key1":"a2","key2":"b3","key3":"c4"},
    {"key1":"a2","key2":"b4","key3":"c4"},
    {"key1":"a3","key2":"b4","key3":"c4"},
]

def test():
    for i in demo1_list:
        for k,v in i.items():
            if k == "key3":
                res={"data":[{"key":v}]}
                return res
b=[{"key":"a1","data":[{"key":"b1","data":[{"key":"c1"},{"key":"c2"}]}]}]
# a=test()
# b.update(a)
print(b)







