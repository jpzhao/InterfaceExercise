# -*- coding: utf-8 -*-
"""
语法
1.变量是什么
	窍门：提取知识点名词中的关键字来加以解释
2.为什么要有它
	大前提：python中语言中出现的所有的语法都是为了让计算机能够具备人的某一功能像人一样去做事
3.如何用

核心法则：想明白怎么去用,读不是目的，存是为了将来更方便的取

小整数池[-5,256]
Python解释器启动那一刻开始，就会在内存中事先申请一系列内存空间存放好常用的整数

is与==
is:比较左右两个值身份id是否相等
==:比较左右两个值他们的值是否相等
id不同的情况下，值有可能相同，即两块不同的内存空间里可以存相同的值
id相同的情况下，值不一定相同，x is y成立，x==y也必然成立

数据类型：存储数据是为了将来更好的取数据
内存中有两块区域：堆区和栈区，在定义变量时，变量名与值内存地址id(变量)的关联关系存放于栈区，变量值存放于堆区
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

浅拷贝：是把原列表第一层的内存地址完全copy一份给新列表(不加区分可变和不可变类型），默认情况下都是浅拷贝
list2=list1.copy()
深拷贝：针对不可变类型沿用旧的内存地址，可变类型重新新建内存地址（加以区分可变和不可变类型）
想让两个列表完全独立开，并且针对的是改操作的独立而不是读操作
import copy
list3=copy.deepcopy(list1)

while:条件循环
退出循环的两种方式
方式一：将条件改为False，等到下次循环，判断条件时才会生效
方式二：break,只要运行到break就会立刻终止本层循环
while+continue:结束本次循环，直接进入下一次循环
强调：在continue之后添加同级代码毫无意义，因为永远无法运行
while+else:else包含的代码会在while循环结束后，并且while循环在没有被break打断的情况下正常结束的，才会运行。
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

1.什么是for循环
    循环就是重复做某件事，for循环是python提供第二种循环机制
2.为何要有for循环
    理论上for循环能做的事情，while循环都可以做
    之所以要有for循环，是因为for循环在循环取值（遍历取值）比while循环更简洁
3.如何用for循环
语法：for 变量名 in 可迭代对象：可迭代对象可以是：列表，字典，字符串，元组，集合
    ...
总结for循环与while循环的异同
1.相同之处：都是循环
2.不同之处：
    while循环称之为条件循环，循环次数取决于条件何时变为假
    for循环称之为取值循环，循环次数取决in后包含的值的个数
for循环控制循环次数：range()顾头不顾尾

字符串
str可以把任意其他类型都转成字符串
掌握：
strip,lstrip,rstrip    去掉两边，左边，右边字符
lower,upper           大小写
startswith,endswith  开始结尾
format
split,rsplit  分割
join      拼接
replace  替换
isdigit 字符串是否由纯数字组成

了解：
find,rfind,index,rindex,count
center,ljust,rjust,zfill
expandtabs

num=b'5' bytes
num=u'6' unicode,python3中无需加u就是unicode

列表：
作用：按位置存放多个值
定义：
l=[1,1.2,'a'] #l=list([1,1.2,'a'])
print(type(l))
类型转换：但凡能够被for循环遍历的类型都可以当做参数传给list()转成列表
new_l=l[:] 切片等同于拷贝行为，而且相当于浅拷贝
len,in,not in,append,extend,insert,pop,remove,reverse
sort,
字符之间的大小取决于它们在ASCII表中的先后顺序，越往后越大

队列:FIFO,先进先出
l=[]
入队:l.append('first')
出队:l.pop(0)

堆栈:LIFO,后进先出
l=[]
入队:l.append('first')
出队:l.pop()
#优先掌握的操作
list(可以被for循环遍历的类型)
1.按索引存取值(正向存取+反向存取)：即可存也可以取
2.切片（顾头不顾尾，步长）
3.长度
4.成员运算in和not in
5.追加 append,insert
6.删除 pop del
7.循环

元组
元组就是一个不可变的列表
作用：按照索引/位置存放多个值，只用于读不用于改
定义：()内用逗号分隔开多个任意类型的元素
t=(1,2,3,1.3) #t=tuple((1,2,3,1.3))
print(t,type(t))
t=(1,2,3,1.3) #t=(0->值1的内存地址，1->值2的内存地址，2->值3的内存地址，3->值1.3的内存地址)，内存地址不可变
类型转换
tuple('hello')
tuple([1,2,3])
tuple({'a1':111,'a2':222})
内置方法：
t.index
t.count
#优先掌握的操作
tuple()
如果元组中只有一个元素，记住加逗号：t=(1,)
1.按索引取值(正向取+反向取)：只能取
2.切片（顾头不顾尾，步长）
3.长度
4.成员运算in和not in
5.循环

字典
key对应一个值
定义：{}内用逗号分隔开多个key:value,其中value可以是任意类型，但是key
注意：必须是不可变类型,且不能重复
d={'k1':111,(1,2):222} #dict('k1':111,(1,2):222)
数据类型转换
info=[
 ['name','egon'],
 ('age',18),
 ['gender','male']
]
d={}
for k,v in info:
    d[k]=v
res=dict(info) #一行代码搞定上述for循环工作
print(res)
快速初始化一个字典：
k=['name','age','gender']
{}.formkeys(k,None)
#优先掌握的操作

1.按key存取值：可存可取
2.长度len
3.成员运算in和not in
4.删除
5.键keys(),值values(),键值对items()
6.循环

P138
1、什么是内置方法
定义在类内部，以__开头并以__结尾的方法
特点：会在某种情况下自动触发执行
2、为何要用内置方法
为了定制化我们的类or对象
"""