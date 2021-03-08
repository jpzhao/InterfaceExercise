# -*- coding: utf-8 -*-
"""
语法
1.变量是什么
	窍门：提取知识点名词中的关键字来加以解释
2.为什么要有它
	大前提：
		python中语言中出现的所有的语法都是为了让计算机能够具备人的某一功能像人一样去做事
3.如何用

小整数池[-5,256]
Python解释器启动那一刻开始，就会在内存中事先申请一系列内存空间存放好常用的整数

is与==
is:比较左右两个值身份id是否相等
==:比较左右两个值他们的值是否相等
id不同的情况下，值有可能相同，即两块不同的内存空间里可以存相同的值
id相同的情况下，值不一定相同，x is y成立，x==y也必然成立

数据类型：存储数据是为了将来更好的取数据

内存中有两块区域：堆区和栈区，在定义变量时，变量名与值内存地址的关联关系存放于栈区，变量值存放于堆区
P67
"""