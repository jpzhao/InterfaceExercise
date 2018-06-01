#!/usr/bin/env python
# -*- coding: UTF-8 -*-
tList=[98,300,67,44]
a=4
for j in range(len(tList)-1):
    for k in range(1,a):
        if not tList[j]<tList[j+k]:
            tList[j], tList[j + k] = tList[j + k], tList[j]
    a-=1

for i in range(len(tList)):
    print(tList[i])