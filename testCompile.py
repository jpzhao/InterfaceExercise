#!/usr/bin/env python
# -*- coding: UTF-8 -*-

exec_code = compile("""
req=int(input('Count how many numbers?'))
for eachNum in range(req):
    print(eachNum)
""",' ','exec')
exec(exec_code)