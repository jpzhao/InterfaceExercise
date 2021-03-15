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
变量名传参，传递的都是栈区的数据，而且栈区的数据是变量名与内存地址的对应关系，或者说是对值的引用
GC(垃圾回收机制)管理的堆区数据

算术运算符：
'/'结果带小数
'//'结果只保留整数部分
'%'取余数
赋值运算符：
增量赋值+=
链式赋值x=y=z=10
交叉赋值m=20,n=10 m,n=n,m
解压赋值salaries=[111,222,333] a,b,c=salaries
解压赋值只取一个值a,*_=salaries

f的新用法：{}内的字符串可以被当做表达式运行：例f'{print("abc")}'
可变类型：值改变，id不变（列表,字典）
不可变类型：值改变，id也变了（整型,浮点型,字符串,元组）

关于字典补充：
定义：{}内用逗号分隔多key:value,其中value可以是任意类型
但是key必须是不可变类型

其中0,Node,空(空字符串、空列表、空字典)代表的布尔值为False,其余都为True
逻辑运算符优先级：not>and>or
not:就是把紧跟其后的那个条件结果取反
and:逻辑与,and用来链接左右两个条件，两个条件同时为true，最终结果才为真
or:逻辑或,or用来链接左右两个条件，两个条件但凡有一个为true，最终结果就为true

成员运算符 in and not in
字符串判断一个字符串是否存在于一个大字符串中
列表判断一个元素是否存在于列表
字典判断一个k是否存在于字典

身份运算符 in and not in
判断的是id是否相等，id相等值一定相等，值相等id不一定相等

浅拷贝：是把原列表第一层的内存地址完全copy一份给新列表
list2=list1.copy()
深拷贝：
list3=copy.deepcopy(list1)

while:条件循环
退出循环的两种方式
方式一：将条件改为False，等到下次循环，判断条件时才会生效
方式二：break,只要运行到break就会立刻终止本层循环
while+continue:结束本次循环，直接进入下一次循环
强调：在continue之后添加同级代码毫无意义，因为永远无法运行
while+else:else包含的代码会在while循环结束后，并且while循环在没有被break打断的情况下正常结束的，才不会运行。
name='alan'
passwd='123123'
tag=True
count=0
while count<3:
    inp_name=input('please to username: ')
    inp_pwd=input('please to password: ')
    if inp_name==name and inp_pwd==passwd:
        print('login success')
        while tag:
            cmd=input('please to command>: ')
            if cmd=='q':
                tag=False
            else:
                print('command running....')
        break
    else:
        print('username or password error')
        count+=1
else:
    print('input to third error,quit')
P101
1、什么是内置方法
定义在类内部，以__开头并以__结尾的方法
特点：会在某种情况下自动触发执行
2、为何要用内置方法
为了定制化我们的类or对象
"""