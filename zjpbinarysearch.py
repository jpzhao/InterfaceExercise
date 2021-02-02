# -*- coding: utf-8 -*-
l=[-3,4,7,10,13,21,33,43,89,97]
find_num=4
def binary_search(find_num,l):
    print(l)
    if len(l)==0:
        print('找的值不存在')
        return
    mid_index=len(l)//2
    if find_num>l[mid_index]:
        l=l[mid_index+1:]
        binary_search(find_num,l)
    elif find_num<l[mid_index]:
        l=l[:mid_index]
        binary_search(find_num,l)
    else:
        print('find it')
binary_search(find_num)
