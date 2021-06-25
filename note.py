# -*- coding: utf-8 -*-
"""
语法
1.变量是什么
	窍门：提取知识点名词中的关键字来加以解释
2.为什么要有它
	大前提：python中语言中出现的所有的语法都是为了让计算机能够具备人的某一功能像人一样去做事
3.如何用

核心法则：想明白怎么去用,读不是目的，存是为了将来更方便的取
引用传递：python中所有值的传递，传递的都不是值本身，而是值的引用，即内存地址

小整数池[-5,256]
Python解释器启动那一刻开始，就会在内存中事先申请一系列内存空间存放好常用的整数

is与==
is:比较左右两个值身份id是否相等
==:比较左右两个值他们的值是否相等
id不同的情况下，值有可能相同，即两块不同的内存空间里可以存相同的值
id相同的情况下，值一定相同，x is y成立，x==y也必然成立

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
    for
    list(dic.keys())
    tuple(dic.values())
6.循环

集合
1.关系运算
    作用
        关系运算
        去重
    定义
        在{}内用逗号分隔开多个元素，多个元素满足以下三个条件
        1.集合内元素必须为不可变类型
        2.集合内元素无序
        3.集合内元素没有重复
    了解
        s={}#默认是空字典
        定义集合
        s=set()
    类型转换
        set({1,2,3})
        set('hello')
        set({'k1':1,'k2':2})
    内置方法
        friends1={"zero","kevin","jason","egon"}
        friends2={"Jy","ricky","egon"}
        取交集
        friends1&friends2
        friends1.intersection(friends2)
        取并集
        friends1|friends2
        friends1.union(friends2)
        取差集
        取friends1独有的好友
        friends1-friends2
        friends1.difference(friends2)
        对称差集，求两个用户独有的
        friends1^friends2
        friends1.symmetric_difference(friends)
        父子集，包含关系
        s1={1,2,3}
        s2={1,2}
        s1>s2 #当s1大于或等于s2时，才能说是s1是s2他爹

        s1={1,2,3}
        s2={1,2,3}
        s1==s2 #s1与s2互为父子
        s1.issuperset(s2)
        s2.issubset(s1)

去重（有局限性）
    只能针对不可变类型去重
    无法保证原来的顺序

其他操作
1.长度len()
2.成员运算in
3.循环 for item in s:

其他内置方法
s={1,2,3}
s.discard(3)
s.remove(4) #删除元素不存在则报错
s.update({1,3,5})
s.pop()
s.add()
s.isdisjoint

2.总结与分类
有序or无序：有序又称之为序列类型
存一个值or多个值：存一个值称为原子类型（原子不可再分），存多个值称为容器
可变：  列表、字典
不可变：数字、字符串、元组

字符编码（理论多，结论少）
所有软件都是运行硬件之上的，与运行软件相关的三大核心硬件为cpu、内存、硬盘，我们需要明确三点
#1、软件运行前，软件的代码及其相关数据都是存放于硬盘中的
#2、任何软件的启动都是将数据从硬盘中读入内存，然后cpu从内存中取出指令并执行
#3、软件运行过程中产生的数据最先都是存放于内存中的，若想永久保存软件产生的数据，则需要将数据由内存写入硬盘

文本编辑器读取文件内容的流程
#阶段1、启动一个文件编辑器（文本编辑器如nodepad++，pycharm，word）
#阶段2、文件编辑器会将文件内容从硬盘读入内存
#阶段3、文本编辑器会将刚刚读入内存中的内容显示到屏幕上

以python test.py为例，执行流程如下
#阶段1、启动python解释器，此时就相当于启动了一个文本编辑器
#阶段2、python解释器相当于文本编辑器，从硬盘上将test.py的内容读入到内存中
#阶段3、python解释器解释执行刚刚读入的内存的内容，开始识别python语法

ASCII表：1.只支持英文字符串
        2.采用8位二进制数对应一个英文字符串
GBK表：1.支持英文字符、中午字符
      2.采用8位(8bit=1Bytes)二进制数对应一个英文字符串
        采用16位(16bit=2Bytes)二进制数对应一个中文字符串
unicode:(内存中统一使用unicode)
      1.兼容万国字符
        与万国字符都有对应关系
      2.采用16位（16bit=2Bytes）二进制数对应一个中文字符串
      个别生僻会采用4Bytes，8Bytes
      unicode表：
      人类字符--------》unicode格式数字
                          |
                          |
                        硬盘
                          |
                          |
                        GBK格式的二进制
     老的字符编码都可以转换成unicode，但是不能通过unicode互转
utf-8:
     英文->1Bytes
     汉字->3Bytes
结论：
    1.内存固定使用unicode，我们可以改变的是存入硬盘采用格式
    2.字符转unicode编码，unicode转字符解码
    3.python解释器默认读文件的编码
       python3默认:utf-8
       python2默认:ASCII
    4.指定文件头修改默认的编码
       #coding:utf-8
    5.python3的str类型默认直接存成unicode格式，不会乱码
      保证python2的str类型不乱码
      x=u'上'
    6.python2解释器有两种字符串类型：str,unicode
    str类型
    x='上' 字符串值会按照文件头指定的编码格式存入变量值的内存空间
    unicode类型
    x=u'上'强制存成unicode
编码和解码
x=‘上’
res=x.encode('gbk') #unicode--->gbk 编码
print(res)
print(res.decode('gbk')) 解码

文件
1什么是文件
    文件是操作系统提供给用户/应用程序操作硬盘的一种概念/接口
    用户/应用程序(f=open(),获得文件对象/文件句柄)
    操作系统（文件）
    计算机硬件（硬盘）
为何要用文件
    用户/应用程序可以通过文件将数据永久保存在硬盘中
    即操作文件就是操作硬盘
    用户/应用程序直接操作的是文件，对文件进行的所有操作，都是
    向操作系统发送系统调用，然后再由操作系统将其转换成具体的硬盘操作
如何用文件：open()
    控制文件读写内容的模式:t和b
        强调：t和b不能单独使用，必须跟r/w/a联用
        t文本（默认的模式）
            1.读写都以str(unicode)为单位的
            2.文本文件
            3.必须指定encoding='utf-8'
              没有指定encoding参数操作系统会使用自己默认的编码
              linux系统默认utf-8
              window系统默认gbk
            with open('c.txt',mode='rt') as f:
                res=f.read() t模式会将f.read()读出的结果解码成unicode
                             读出硬盘的二进制(gbk)->t控制将二进制转换unicode->字符
            内存：utf-8格式二进制--》解码---》unicode
            硬盘：（c.txt内容：utf-8格式的二进制）
        b二进制/bytes
    控制文件读写操作的模式
        r只读模式
            当文件不存在时报错，当文件存在时文件指针跳到开始位置
            with open('d.txt'，mode='rt',encoding='utf-8) as f:
                res=f.read() #read把所有内容从硬盘读入内存
        w只写模式
            当文件不存在时会创建空文件，当文件存在时会清空文件，指针位于开始位置
            强调1：在以w模式打开文件没有关闭的情况下，连续写入，新的内容总是跟在旧的之后
            强调2：如果重新以w模式打开文件，则会清空文件内容
        a只追加写模式
            当文件不存在时会创建空文档，在文件存在时文件指针会直接调到末尾
            强调 w 模式与 a 模式的异同：
            1 相同点：在打开的文件不关闭的情况下，连续的写入，新写的内容总会跟在前写的内容之后
            2 不同点：以 a 模式重新打开文件，不会清空原文件内容，会将文件指针直接移动到文件末尾，新写的内容永远写在最后
        了解+：r+、w+、a+
        with open('g.txt',mode='rt+',encoding='utf-8')as f:
            print(f.read())
            f.write('chiness')
        with open('g.txt',mode='w+t',encoding='utf-8')as f:
            f.write('111\n')
            f.write('222\n')
            f.write('333\n')
            print('=========>',f.read())
        with open('g.txt',mode='a+t',encoding='utf-8')as f:
            f.write('444\n')
            f.write('555\n')
            print('========>',f.read())
        x模式（控制文件操作的模式）-
            x，只写模式【不可读，不存在则创建，存在则报错】
        with open('c.txt',mode='x',encoding='utf-8') as f:
            f.write('哈哈哈\n')
        控制文件读写内容的模式
        t:
            1读写都是以字符串(unicode)为单位
            2只能针对文本文件
            3必须指定字符编码
            硬盘的二进制读入内存->t模式会将读入内存的内容进行decode解码
        b:binary模式
            1.读写都是以bytes为单位
            2.可以针对所有文件
            3.一定不能指定字符编码
            硬盘的二进制读入内存->b模式下，不做任何转换，直接读入内存
            bytes类型->当成二进制
        #强调：b模式对比t模式
        1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动编码与解码，所以此时t模式更为方便
        2、针对非文本文件（如图片、视频、音频等）只能使用b模式
        with open(r'e.txt',mode='wb') as f:
            f.write('你好hello'.encode('utf-8'))
        with open(r'g.txt',mode='r',encoding='utf-8') as f:
            for line in f:
                print(line)
        with open(r'test.jpg',mode='rb') as f:
            while True:
                res=f.read(1024)
                if len(res)==0:
                    break
                print(len(res))
1.打开文件
    open(r'c:\a\b\c\d.txt')
    f=open('c:/a/b/c/d.txt') #f的值是一种变量占用的是应用
                             程序的内存空间
2.操作文件:读/写文件，应用程序对文件的读写请求都是在向操作系统发送
 系统调用，然后由操作系统控制硬盘把输入读入内存、或者写入硬盘
3.关闭文件
f.close()
4.编写文本文件copy程序
    with open(r'源文件'，mode='rt',encoding='utf-8') as f1,\
        open(r'目标文件'，mode='wt'，encoding='utf-8') as f2
        data=f1.read()
        f2.write(data)
5常用方法
    readline()读一行
    readlines()
    强调：
    f.read()与f.readlines()都是将内容一次性读入内存，如果内容过大会导致内存溢出，
    若还想将内容全读入内存，则必须分多次读入，有两种实现方式：
    writelines():
    补充一：如果是纯英文字符，可以直接加前缀b得到bytes类型
    补充二：
    '上'.encode('utf-8)==bytes('上',encoding='utf-8')
    flush:强行写操作（写入硬盘）
    f.tell()获取文件指针当前的位置
控制文件指针操作
指针移动的单位都是以bytes/字节为单位
只有一种情况特殊：
    t模式下的read(n)，n代表的是字符个数
f.seek(n,mode)：n指的是移动的字节个数
模式：
0：参照物是文件开头位置
1：参照物是当前指针所在位置
2：参照物是文件末尾位置，应该倒着移动
强调只有0模式可以在t下使用，1,2必须在b模式下使用
with open('access.log',mode='rt',encoding='utf-8') as f
    f.seek(0,2)
    while True:
        line=f.readline()
        if len(line)==0:
            time.sleep(0.3)
        else:
            print(line)
方式一：文本编辑采用的就是这种方式
with open('c.txt',mode='rt',encoding='utf-8') as f:
    res=f.read()
    data=res.replace('alex','dsb')
    print(data)

with open('c.txt',mode='wt',encoding='utf-8') as f1:
    f1.write(data)

方式二：
with open('c.txt',mode='rt',encoding='utf-8') as f,\
    open('.c.txt.swap',mode='wt',encoding='utf-8') as f1:
    for line in f:
        f1.write(line.replace('alex','dsb'))
os.remove('c.txt')
os.rename('.c.txt.swap','c.txt')


函数
1.什么是函数
    函数就相当于具备某一功能的工具
    函数的使用必须遵循一个原则：
        先定义
        后调用
2.为何要用函数
    1代码冗余，程序的组织结构不清晰，可读性差
    2可维护性，扩展性差
3.如何用函数
    先定义
        三种定义方式
    后调用
        三种调用方式
    返回值
        三种返回值的形式
1.先定义
定义语法
def 函数名(参数1,参数2,...):
    '''文档描述'''
    函数体
    return 值

定义形式一：无参函数
def func()
    print('haha')
func()
定义函数发生的事情：
1.申请内存空间保存函数体代码
2.将上述内存地址绑定函数名
3.定义函数不会执行函数体代码，但是会检测函数体语法
调用函数发生的事情：
1.通过函数名找到函数的内存地址
2.然后加括号就是在触发函数体代码的执行

定义形式二：有参函数
def func(x,y):
    print(x,y)
func(1,2)

定义形式三：空函数，函数体代码为pass
def func(x,y):
    pass

三种定义方式各用在何处
1.无参函数的应用场景
2.有参函数的应用场景
3.空函数的应用场景

二调用函数：
1.语句的形式：只加括号调用函数
2.表达式形式：
def add(x,y)
    res=x+y
    return res
赋值表达式
res=add(1,2)
print(res)
数据表达式
res=add(1,2)*10
print(res)
3.函数调用可以当做参数
res=add(add(1,2),10)
print(res)

三、函数返回值
return是函数结束的标志，即函数体代码一旦运行到return会立刻
终止函数的运行，并且会将return后的值当做本次运行的结果返回：
1.返回None:函数体内没有return
    :return
    :return None
2.返回一个值：return 值
3.返回多个值：用逗号分隔开多个值，会被return返回成元组
def func():
    return 10,'aa',[1,2]

参数
形参：在定义函数阶段定义的参数称之为形式参数，简称形参，相当于变量名
实参：在调用函数阶段传入的值称之为实际参数，简称实参，相当于变量值
形参与实参关系：在调用阶段实参（变量值）会绑定（内存地址）给形参（变量名）
这种绑定关系只能在函数体内使用
实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定关系

实参是传入的值，但值可以是以下形式
形式一
func(1,2)
形式二
a=1
b=2
func(a,b)
形式三
func(int('1'),2)

位置参数：按照从左到右的顺序依次定义的参数称之为位置参数
位置形参:在函数定义阶段，按照从左到右的顺序直接定义的“变量名”
特点：必须被传值，多一个不行少一个不行
def func(x,y)

位置实参:在函数调用阶段，按照从左到右的顺序依次传入的值  takes 2 positional arguments but 3 were given
特点：按照顺序与形参一一对应

关键字实参：在函数调用阶段，按照key=value的形式传入值
特点：指名道姓给某个形参传值，可以完全不参考顺序
def func(x,y):
    print(x,y)
func(x=1,y=2)
混合使用，强调
1.位置实参必须放在关键字实参前
2.不能为同一个形参重复传值

默认形参：在定义函数阶段，就已经被赋值的形参，称之为默认参数
特点：在定义阶段就已经被赋值，意味着在调用阶段可以不用为其赋值

位置形参与默认形参混用，强调：
1.位置形参必须在默认形参的左边
2.默认参数的值是在函数定义阶段被赋值的,准确地说被赋予的是值得内存地址
例子：m=2
     def func(x,y=m): #y=>2的内存地址
       print(x,y)
     m=333
     func(1)

例子：m=[1111]
def func(x,y=m):
    print(x,y)
m.append(3333)
fucn(1)

3.虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
函数的最理想的状态：函数的调用只跟函数本身有关系，不受外界代码的影响

可变长度的函数（*与**的用法）
可变长度指的是在调用函数时，传入的值（实参）的个数不固定
而实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接收
可变长度的位置参数
*形参名用来接收溢出的位置实参，溢出的位置实参会被*保存成元组的格式然后赋值紧跟其后的形参名
*后跟的可以是任意名字，但是约定俗成应该是args
*可以用在实参中，实参中带*，先*后的值打散成位置实参
def func(x,y,z)
    print(x,x,z)
func(*[11,2,3,])#func(11,2,3)

l=[1,2,3]
func(*l)

形参与实参中都带*
def func(x,y,*args):
    print(x,y,args)
func(1,2,*[3,4,5,6])

可变长度的关键字参数
**形参名用来接收溢出的关键字实参，**会将溢出的关键字实参保存成字典格式，然后赋值紧跟其后的形参名
**后跟的可以是任意名字，但是约定俗成应该是kwargs
**可以用在实参中(**后跟的只能是字典)，实参中带**，先**后的值打散成关键字实参
def func(x,y,z)
print(x,y,z)
func(**{'x':1,'y':2,'z':3}) #func(x=1,y=2,z=3)

形参与实参中都带**
def func(x,y,**kwargs)
print(x,y,kwargs)
func(**{'x':1,'y':2,'z':3}) #func(y=111,x=222,a=333,b=444)

混用*与**
def func(x,*args,**kwargs):
    print(args)
    print(kwargs)
func(1,2,3,3,x=1,y=2)

def index(x,y,z):
    print(x,y,z)

def wrapper(*args,**kwargs):  #args=(1,) kwargs={'y':2,'z':3}
    index(*args,**kwargs)
    #index(*(1,),**{'y':2,'z':3})
    #index(1,z=3,y=2)
wrapper(1,z=3,y=2)

命名关键字参数
定义函数时，*后定义的参数，如下所示，称之为命名关键字参数
特点：
1.命名关键字实参必须按照key=value的形式为其传值
def func(x,y,*,a,b) 其中，a和b称之为命名关键字参数
    print(x,y)
    print(a,b)

组合使用
位置形参，默认形参,*args,命名关键字形参，**kwargs
def func(x,y=111,*args,z,**kwargs):

实参混用的顺序
def func(x,y,z,a,b)
func(111,y=222,*[333,444],**{'b':555,'c':666})


一：名称空间（nameapaces）与作用域
名称空间：存放名字的地方，是对栈区的划分
有了名称空间之后，就可以在栈区中存放相同的名字，详细的，名称空间
分为三种
1.1内置名称空间
存放的名字：存放的python解释器内置的名字
存活周期：python解释器启动则产生，python解释器关闭则销毁

1.2全局名称空间
存放的名字：只要不是函数内定义，也不是内置的，剩下的都是全局名称空间的名字
存活周期：python文件执行则产生，python文件运行完毕后销毁

1.3局部名称空间
存放的名字：在调用函数时，运行函数体代码过程中产生的函数内的名字
存活周期：在调用函数时存活，函数调用完毕后销毁

1.4名称空间的加载顺序
内置名称空间》全局名称空间》局部名称空间

1.5销毁顺序
局部名称空间-》全局名称空间-》内置名称空间

1.6名字的查找优先级：当前所在的位置向上一层一层查找
内置名称空间
全局名称空间
局部名称空间
如果当前在局部名称空间
局部名称空间-》全局名称空间》内置名称空间

如果当前在全局名称空间
全局名称空间-》内置名称空间

名称空间的“嵌套”关系是以函数定义阶段为准，与调用位置无关
x=1
def func():
    print(x)
def foo()
    x=222
    func()
foo()

函数嵌套定义
input=111
def f1():
    def f2():
        input=333
        print(input)
    input=222
    f2()
f1()

二：作用域-》作用范围
全局作用域：内置名称空间、全局名称空间
1.全局存活
2.全局有效：被所有函数共享

局部作用域：局部名称空间的名字
1.临时存活
2.局部有效

如果在局部想要修改全局的名字对应的值(不可变类型)，需要用global
global x 声明x这个名字是全局的名字，不要在造新的名字了
nonlocal 修改函数外层函数包含的名字对应的值（不可变类型）

I:三种名称空间用途与存活周期
II:三种名称空间的加载顺序
III:三种名称空间的查找名字的优先级
作用域
全局作用域
    内置名称空间+全局名称空间的名字
    全局存活，全局有效
局部作用
    临时存活，局部有效
global
    x=1
    def func():
        global x
        x=10
nonlocal

函数嵌套使用的情况下，作用域与名字的查找关系
重点：名称空间的嵌套关系决定了名字的查找顺序
而名称空间的嵌套关系是以函数定义阶段为准的
即函数的嵌套关系与名字的查找顺序是在定义阶段就已经确定好的

1.函数对象(可以把函数当成变量去用)
精髓：可以把函数当成变量去用
    可以赋值 f=func
    可以把函数当做参数传给另外一个函数print(f,func)
    可以把函数当做另外一个函数的返回值
    可以当做容器类型的一个元素
2.函数嵌套
    函数的嵌套调用：在调用一个函数的过程中又调用其他函数
    函数的嵌套定义：在函数内定义其他函数
3.闭包函数=名称空间与作用域+函数嵌套+函数对象
核心点：名字的查找关系是以函数定义阶段为准
什么是闭包函数
    “闭”函数指的该函数是内嵌函数
    “包”函数指的该函数包含对外层函数作用域名字的引用（不是对全局作用域）
                f2          f1
    def f1():
        x=1
        def f2():
            print(x)
        f2()
    闭包函数：名称空间与作用域的应用+函数嵌套
            名称空间的“嵌套”关系是在函数定义阶段，即检测语法的时候确定的
    闭包函数：函数对象
            可以把函数内存地址当做参数传入
            可以把函数内存地址当做返回值返回
    def f1():
        x=333
        def f2():
            print('函数f2',x)
        return f2    #实现全局拿到f2地址
    f=f1()
    f()
为何要有闭包函数=》闭包函数的应用
两种为函数体传参的方式
方式一：直接把函数体需要的参数定义成形参
def f2(x):
    print(x)
方式二：
def f1(x):
    def f2(x):
        print(x)
    return f2
x=f1(3)
print(x)

/**************装饰器**********/
1什么是装饰器
    器指的事工具，可以定义成函数
    装饰指的是为其他事物添加额外的东西点缀
    合到一起的解释：
        装饰器指的定义一个函数，该函数是用来装饰其他函数添加额外的功能
2为何要用装饰器
    开发封闭原则
        开放：指的是对拓展功能是开发的
        封闭：指的是对修改源代码是封闭的
    装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下为被装饰对象添加新功能
3如何用

语法糖
在被装饰对象正上方的单独一行写@装饰器名字
总结
def outter(func):
    def wrapper(*args,**kwargs):
        #1.调用原函数
        #2.为其增加新功能
        res=func(*args,**kwargs)
        return res
    return wrapper
@outter
def index():
    print('from index')

偷梁换柱，即将原函数名指向的内存地址偷梁换柱成wrapper函数
所以应该将wrapper做的跟原函数一样才行

from functools import wraps
def outter(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        #1.调用原函数
        #2.为其增加新功能
        res=func(*args,**kwargs)
        return res
    return wrapper
@outter
def index():
    print('from index')

#有参装饰器模板
def deco(x,y,z):
    def outter(func)
        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            return res
        return wrapper
    return outter

@deco(1,y=2,z=3)
def index():
    pass

叠加多个装饰器加载，运行分析
def deco1(func)  #func1=wrapper2的内存地址
    def wrapper1(*args,**kwargs)
        print('正在运行===》deco1.wrapper1')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1
def deco2(func)   #func2=wrapper3的内存地址
    def wrapper2(*args,**kwargs)
        print('正在运行===》deco2.wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2
def deco3(x)
    def outter3(func3) #func3=被装饰对象index函数的内存地址
        def wrapper3(*args,**kwargs)
            print('正在运行===》deco3.outter3.wrapper3')
            res3=func3(*args,**kwargs)
            return res3
        return wrapper3
    return output3
#加载顺序自下而上
@deco1     #index=deco1(wrapper2的内存地址)==>wrapper1的内存地址
@deco2     #index=deco2(wrapper3的内存地址)==>wrapper2的内存地址
@deco3(11) #===》@outter3==>index=outter3(index)==>index=wrapper3的内存地址
def index(x,y):
    print('from index %s:%s'%(x,y))
#执行顺序自上而下
index(x,y) #wrapper1(1,2)

/*******迭代器*********/
1.什么是迭代器(iterator)
    迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复
    都是基于上一次的结果而继续的，单纯的重复并不是迭代
2.为何要有迭代器
    迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的类型有：
    列表，字符串，元组，字典，集合，文件
    l=['egon','liu','alex']
    i=0
    while i<len(l):
        print(l[i])
        i+=1
    上述迭代取值的方式只适用于有索引的数据类型：列表、字符串、元组
    为了解决基于索引迭代器取值的局限性
    python必须提供一个能够不依赖于索引的取值方式，这就是迭代器
3.如何用迭代器
可迭代对象：但凡内置有__iter__方法的都称之为可迭代对象
''.__iter__
[].__iter__
(1,).__iter__
{'a':1}.__iter__
set1={1,3,4}
set1.__iter__
with open('a.txt',mode='w') as f:
    f.__iter__()
    pass

调用可迭代对象下的__iter__方法会将其转换成迭代器对象
d={'a':1,'b':2,'c':3}
res=d.__iter__()
print(res)
<dict_keyiterator object at 0x109e6db80>
print(res.__next__()) 超出取值范围抛出异常StopIteration
在一个迭代器取值取干净的情况下，再对其取值取不到

可迭代对象与迭代器对象详解
可迭代对象（可以转换成迭代器的对象）：内置__iter__方法对象
    可迭代对象.__iter__():得到迭代器对象
迭代器对象：内置有__next__方法并且内置有__iter__方法的对象
    迭代器对象.__next__():得到迭代器的下一个值
    迭代器对象.__iter__():得到迭代器的本身，说白了调了跟没调一个样子

#for循环的工作原理：for循环可以称之为迭代器循环
d={'a':1,'b':2,'c':3}
1.d.__iter__()得到一个迭代器对象
2.迭代器对象.__next__()拿到一个返回值，然后将该返回值赋值给k
3.循环往复步骤2，直到抛出StopIteration异常for循环会捕捉异常然后结束循环
for k in d(可迭代对象):可迭代对象.__iter__()=>迭代器对象-》x=next(迭代器对象)
    print(k)
迭代器对象一定是可迭代对象，可迭代对象不一定是迭代器对象
可迭代对象：字符串，列表，元组，字典，集合，文件对象
迭代器对象：文件对象

list('hello')#原理同for循环
迭代器优缺点总结
优点：
    迭代取值统一方案，有索引类型，没有索引的类型
    节省内存，迭代器就是一个功能，
缺点：
    无法按索引取值
    一次性取值，再取需要在调用一次迭代器

/*******生成器*********/
生成器(generator)就是自定义的迭代器
在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
会返回一个生成器对象，生成器即自定义的迭代器
g.__next__()
会触发函数体代码的运行，然后遇到yield停下来，将yield后的值
当做本次调用的结果返回

小知识点：
len('aaa') #'aaa'.__len__()
next(g) #g.__next__()

def func():
    print('run')
    yield 1
g=func()
res1=next(g)
有了yield关键字，就有了一种自定义迭代器的实现方式，yield可以用于返回值，但不同于return，
函数一旦遇到return就结束了，而yield可以保存函数的运行状态挂起函数，用来返回多次值

def dog(name):
    food_list=[]
    print('道哥%s准备东西啦...'%name)
    while True:
        #x拿到的是yield接收到的值
        x=yield food_list #x='肉包子' x=yield #赋值  yield food_list #返回值
        print('道哥%s吃了%s'%(name,x))
        food_list.append(x)
g=dog('xxx')
g.send(None) #等同于next(g)
g.send('一根骨头')
g.send('肉包子')

/*******三元表达式*********/
语法格式：条件成立时要返回的值 if 条件 else 条件不成立时要返回的值

/*******列表生成式*********/
语法格式：
[expression for item1 in iterable1 if condition1
for item2 in iterable2 if condition2
...
for itemN in iterableN if conditionN]
1、列表生成式
l=['a_dsb','b_dsb','c_dsb','abc']
new_l=[]
for name in l:
    if name.endswith('dsb'):
        new_l.append(name)
new_l=[name for name in l if name.endswith('dsb')]

2、字典生成式
items=[('name','egon'),('age',18),('gender','male')]
res={k:v for k,v in items if k!='gender'}

3、集合生成式
keys=['name','age','gender']
set1={key for key in keys}

4、生成器表达式
g=(i for i in range(10) if i>3)
with open('c.txt',mode='rt',encoding='utf-8') as f
    #生成器表达式简写
    res=sum(len(line) for line in f)

/*******函数递归*********/
函数的递归调用：是函数嵌套调用的一种特殊形式
具体是指：
    在调用一个函数的过程中又直接或者间接地调用到本身
查看默认递归数
import sys
sys.getrecursionlimit()

直接调用本身
def f1()
    print('me')
    f1()
f1()
间接调用本身
def f1():
    print('===>f1')
    f2()
def f2()
    print('===>f2')
    f1()
f1()

一段代码的循环运行的方案有两种
方式一：while,for(场景:用于取值更多)循环
方式二：递归的本质就是循环

二：需要强调的一点是：
递归调用不应该无限地调用下去，必须在满足某种条件下结束递归调用
n=0
while n<10:
    print(n)
    n+=1
等同
def func(n)
    if n==10:
        :return
    print(n)
    n+=1
    f1(n)
func(0)

三：递归的两个阶段
回溯：一层一层调用下去
递推：满足某种结束条件，结束递归调用，然后一层一层返回
age(5)=age(4)+10
age(4)=age(3)+10
age(3)=age(2)+10
age(2)=age(1)+10
age(1)=18
def age(n):
    if n==1:
        return 18
    return age(n-1)+10
res=age(5)

四：递归的应用
def f1(list1):
    for x in list1:
        if type(x) is list:
            #如果是列表，应该再循环
            f1(x)
        else:
            print(x)
f1(l)

/*******算法*********/
算法：是高效解决问题的办法
算法之二分法
l=[-3,4,7,10,13,21,33,43,89,97]
find_num=4
def binary_search(find_num,l):
    print(l)
    if len(l)==0:
        print('找的值不存在')
        return False
    mid_index=len(l)//2
    if find_num>l[mid_index]:
        l=l[mid_index+1:]
        return binary_search(find_num,l)
    elif find_num<l[mid_index]:
        l=l[:mid_index]
        return binary_search(find_num,l)
    else:
        print('find it')
binary_search(find_num)

/*******编程思想*********/
编程思想/范式
面向过程的编程思想：
核心是“过程”二字，过程即流程，指的事做事的步骤：先什么，再什么，后干什么
基于该思想编写程序就好比设计一条流水线
有点：复杂的问题流程化，进而简单化
缺点：扩展性非常差
面向过程的编程思想应用场景解析：
不是所有的软件都需要频繁更迭，比如编写脚本
即便是一个软件需要频繁更迭，也不并不代表这个软件所有的组成部分都需要一起更迭

/*******匿名函数*********/
1.def用于定义有名函数
func=函数的内存地址
def func(x,y):
    return x+y
print(func)
2.lamdab用于定义匿名函数
print(lambda x,y:x+y)
3.调用匿名函数
方式一：
res=(lambda x,y:x+y)(1,2)
print(res)
4.匿名用于临时调用一次的场景：更多的是将匿名与其他函数配合使用

def func(k):
    return salaries[k]
res=max(salaries,key=func)
等同
res=max(salaries,key=lambda k:salaries[k])
res=min(salaries,key=lambda k:salaries[k])
res=sorted(salaries,key=lambda k:salaries[k])
l=['a','b','c']
new_l=(name+'_test' for name in l)
等同
res=map(lambda name:name+'_test',l)
l=['a_test','b_test','c']
res=(name for name in l if name.endswith('test'))
等同
filter(lambda name:name.endswith('test'),l)
from functools import reduce
reduce(lambda x,y:x+y,[1,2,3],10)

/*******模块*********/
1.什么是模块
模块就是一系列功能的集合体，分为三大类
    I:内置的模块
    II:第三方的模块
    III:自定义的模块
        一个python文件本身就是一个模块，文件名m.py,模块名叫m
        模块有四种形式
        1使用python编写的.py文件
        2已被编译为共享库或DLL的C或C++扩展
        3把一系列模块组织到一起的文件夹（注：文件夹下有一个__init__.py文件，该文件夹称之为包）
        4使用C编写并链接到python解释器的内置模块
2.为何用模块
    内置与第三的模块拿来就用，无需定义，这种拿来主义，可以极大地提升自己
    自定义的模块
        可以将程序的各部分功能提取出来放到一模块中为大家共享使用
        好处是减少代码冗余，程序组织结构更加清晰
3.如何用模块
import foo
首次导入模块会发生3件事
1.执行foo.py
2.产生foo.py的名称空间，将foo.py运行过程中产生的名字都丢到foo的名称空间中
3.在当前文件中产生的有一个名字foo,该名字指向2中产生的名称空间
之后的导入，都是直接引用首次导入产生的foo.py名称空间，不会重复执行代码

引用
    强调1：模块名.名字，是指名道姓地访问某一个模块要名字对应的值，不会与当前名称空间中的名字发生冲突
    强调2：无论是查看还是修改操作的都是模块本身，与调用位置无关
    可以以逗号为分隔符在一行导入多个模块
建议如下所示导入多个模块
    import time
    import foo
    import m
不建议在一行同时导入多个模块
    import time,foo,m
导入模块的规范
1.python内置模块
2.第三方模块
3.程序员自定义模块
import .... as ....
模块是第一类对象
自定义模块的命名应该采用纯小写+下划线的风格
可以在函数内导入模块
def func():
    import time

/*******一个python文件两种用途*********/
被当做程序运行
被当做模块导入
*只要名称空间的名字还在被引用，就不会被回收
1.运行run.py，启动虚拟机，创建全局名称空间
2.import foo创建模块foo的名称空间
3.run.py文件中的foo属性指向模块foo的名称空间

/*******__name__*********/
1.当foo.py被运行时，__name__的值为'__main__'
2.当foo.py被当做模块导入时，__name__的值为'foo'

#import导入模块在使用时必须加前缀“模块.”
优点 肯定不会与当前名称空间中的名字冲突
缺点 加前缀显得麻烦

函数的名称空间与作用域关系是以定义阶段为准，与位置无关

from...import...导入也发生了三件事
1产生一个模块的名称空间
2运行foo.py将运行过程中产生的名字都丢到模块的名称空间去
3在当前名称空拿到一个名字，该名字与模块名称空间中的某一个内存地址
from foo import x
from foo import get

from...import...导入模块在使用时不用加前缀
优点：代码更精简
缺点：容易与当前名称空间混淆

一行导入多个名字（不推荐）
#from foo import x;get;change
#*:导入模块中的所有名字
from foo import *
__all__=['x',]#控制*代表的名字有哪些
from foo import get as g起别名

无论是import还是from...import在导入模块时都涉及查找
优先级：
1内存（内置模块）
2按照sys.path中存放的文件的顺序依次查找要导入的模块

import sys
值为一个列表，存放了一系列的文件夹
其中第一个文件夹是当前执行文件所在的文件夹
print(sys.path)
了解：sys.modules查看已经加载到内存中的模块
print(sys.modules)
import sys
import foo #foo=模块的内存地址
print('foo' in sys.modules)

import sys
#找foo.py就把foo.py的文件夹添加到环境变量中
sys.path.append(r'/user/xxx/xxx')

函数的类型提示
def register(name:str,age:int,hobbbies:tuple)->int:#'返回的是整型int':
    print(name)
    print(age)
    print(hobbbies)
    return 111
# 查看提示信息功能
print(register.__annotations__)
# {'name': '必须传入字符串', 'age': 111, 'hobbies': '必须传入元组', 'return': '返回的是整型int'}

1.包就是一个包含有__init__.py文件的文件夹
2.为何要有包
    包的本质就是模块的模块的一种形式，包是用来被当做模块导入

1产生一个名称空间
2运行包下的__init__.py文件，将运行过程中产生的名字都丢到1的名称空间中
3在当前执行文件的名称的空间中拿到一个名字mmm，mmm指向1的名称空间
import mmm
#绝对导入，以包的文件夹作为起始来进行导入
from m1 import f1
环境变量是以执行文件为准备的，所有的被导入的模块或者说后续的其它文件引用
的sys.path都是参照执行文件的sys.path

强调
1.关于包相关的导入语句也分为import和from ... import ...两种，但是无论哪种，
无论在什么位置，在导入时都必须遵循一个原则：凡是在导入时带点的，点的左边都必须是
一个包，否则非法。可以带有一连串的点，如import 顶级包.子包.子模块,但都必须遵循这个原则。但对于导入后，
在使用时就没有这种限制了，点的左边可以是包,模块，函数，类(它们都可以用点的方式调用自己的属性)。
from a.b.c.d.e.f import xxx
import a.b.c.d.e.f
其中a、b、c、d、e都必须是包
2、包A和包B下有同名模块也不会冲突，如A.a与B.a来自俩个命名空间
3、import导入文件时，产生名称空间中的名字来源于文件，import 包，产生的名称空间的名字同样来源于文件，
即包下的__init__.py，导入包本质就是在导入该文件

相对导入：仅限于包内使用，不能跨出包（包内模块之间的导入，推荐使用相对导入）
.:代表当前文件夹
..:代表上一层文件夹
import...
强调：相对导入不能跨出包，所以相对导入仅限于包内模块彼此之间闹着玩
而绝对导入时没有任何限制的，所以绝对导入是一种通用的导入方式

优化方案：
import os
print(__file__)#当前文件的绝对路径
BASE_DIR=os.path.dirname(os.path.dirname(__file__))

from pathlib import Path
root=Path(__file__)
res=root.parent.parent /r'\bbb\aaa\ccc'
print(res)
print(res.resolve())

/*******time*********/
一.time
import time
时间分为三种格式：
1.时间戳：从1970年到现在经过的秒数
    作用：用于时间间隔的计算
print(time.time())
2.按照某种格式显示的时间：2020-03-30 11:11:11
    作用：用于展示时间
print(time.strftime('%Y-%m-%d %H:%M:%s %P'))
print(time.strftime('%Y-%m-%d %X'))
3.结构化的时间
    作用：用于单独获取时间的某一部分
res=time.localtime()
print(res.tm_year)

二.datatime
import datatime
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(days=3))

时间模块需要掌握的操作
1.时间格式的转换
struct_time->时间戳
import time
s_time=time.localtime()
print(time.mktime(s_time))

时间戳-》struct_time
tp_timetime.time()
print(time.localtime(tp_time))
print(time.localtime())  #当前时间
print(time.gmtime())     #世界标准时间

struct_time->格式化的字符串形式的时间
s_time=time.localtime()
time.strftime('%Y-%m-%d %H:%M:%S',s_time)

time.strptime('1988-03-03 11:11:11','%Y-%m-%d %H:%M:%S')

真正需要掌握的只有一条：format string<--->timestamp
需求：'1988-03-03 11:11:11'+7 加7天
timestamp 时间戳
struct_time 结构化时间
format string 字符串时间
format string--->struct_time--->timestamp
struct_time=time.strptime('1988-03-03 11:11:11','%Y-%m-%d %H:%M:%S')
timestamp=time.mktime(struct_time)+7*86400(一天的秒数)

format string<---struct_time<---timestamp
time.strftime('%Y-%m-%d %X',time.localtime(timestamp))

time.sleep(3)
了解知识
time.asctime()
datetime.datetime.now()
datetime.datetime.utcnow()
datetime.datetime.fromtimestamp(3333)

/*******random*********/
import random
print(random.random())#(0,1)----float    大于0且小于1之间的小数
print(random.randint(1,3))  #[1,3]    大于等于1且小于等于3之间的整数
print(random.randrange(1,3)) #[1,3)    大于等于1且小于3之间的整数
print(random.choice([1,'23',[4,5]]))#1或者23或者[4,5]
print(random.sample([1,'23',[4,5]],2))#列表元素任意2个组合
print(random.uniform(1,3))#大于1小于3的小数，如1.927109612082716
item=[1,3,5,7,9]
random.shuffle(item) #打乱item的顺序,相当于"洗牌"
print(item)

import random
for i range(6):
    s1=chr(random.randint(65,90))
    s2=str(random.randint(0,9))
    res+=random.choice([s1,s2])

/*******os*********/
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  运行shell命令，直接显示
os.environ  获取系统环境变量
os.path.abspath(path)  返回path规范化的绝对路径
os.path.split(path)  将path分割成目录和文件名二元组返回
os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path) 返回path的大小

/*******sys*********/
1 sys.argv           命令行参数List，第一个元素是程序本身路径
2 sys.exit(n)        退出程序，正常退出时exit(0)
3 sys.version        获取Python解释程序的版本信息
4 sys.maxint         最大的Int值
5 sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
6 sys.platform       返回操作系统平台名称

进度条
import time
res=''
for i in range(1,61):
    res+='#'
    time.sleep(1)
    res1=i/60
    print('\r[%-60s] %d%%'% (res,res1*100),end='')

/*******序列化*********/
什么是序列化，反序列化
    序列化指的是把内存的数据类型转换成一个特定的格式内容
    该格式的内容可用于存储或者传输给其他平台使用
    内存中的数据类型--->序列化---->特定的格式(json格式或者pickle格式)
    内存中的数据类型<---反序列化<----特定的格式(json格式或者pickle格式)

土方法：
    {'aaa':111}--->序列化str({'aaa':111})---->"{'aaa':111}"
    {'aaa':111}<---反序列化eval("{'aaa':111}")<----"{'aaa':111}"
为何要序列化
    序列化得到结果-》特定的格式的内容有两种用途
    1.可用于存储-》用于存档
    2.传输给其他平台使用-》跨平台数据交互
        python   中间格式      java
        列表     特定格式       数组
    强调：
    针对用途1的特定-格式：可是一种专用的格式=》pickle只有python可以识别
    针对用途2的特定-格式：应该是一种通用，能够被所有语言识别的格式=》json
    如何序列化和反序列化
        序列化
        import json
        json_res=json.dumps([1,'aaa',True,False])
        反序列化
        l=json.loads(json_res)

        import json
        序列化的结果写入文件的复杂方法
        json_res=json.dumps([1,'aaa',True,False])
        with open('test.json',mode='wt',encoding='utf-8') as f:
            f.write(json_res)
        将序列化的结果写入文件的简单方法
        with open('test.json',mode='wt',encoding='utf-8') as f:
            json.dump([1,'aaa',True,False],f)

        反序列化
        从文件读取json格式的字符串进行反序列化操作的复杂方法
        with open('test.json',mode='rt',encoding='utf-8') as f:
            json_res=f.read()
            l=json.loads(json_res)
        从文件读取json格式的字符串进行反序列化操作的简单方法
        with open('test.json',mode='rt',encoding='utf-8') as f:
            ljson.load(f)

json验证：json格式兼容的是所有语言通用的数据类型，不能识别某一语言的所有独有类型
json.dumps({1,2,3,4,5})

json强调：一定要搞清楚json格式，不要与python混淆
l=json.loads('[1,"aaa",true,false]')

# 在python解释器2.7与3.6之后都可以json.loads(bytes类型)，但唯独3.5不可以
import json
json.loads(b'{"a":111}')
with open('test.json',mode='rb') as f:
    l=json.load(f)

/*******猴子补丁*********/
在入口处打猴子补丁
import json
import ujson
def monkey_patch_json():
    json.dumps=ujson.dumps
    json.loads=ujson.loads
monkey_patch_json() #在入口文件处运行

/*******猴子补丁*********/
1.什么是哈希hash
    hash一类算法，该算法接受传入的内容，经过运算得到一串hash值
    hash值的特定：
    I只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
    II不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码
    III不管传入的内容有多大，只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的
2.hash的用途
    特点II用于密码密文传输与验证
    特点I、III用于文件完整性校验
3.如何用
import hashlib
m=hashlib.md5()
m.update('hello'.encode('utf-8))
res=m.hexdigest()
用途2
f=open('a.txt',mode='rb')
f.seek()
f.read(2000)
m1.update(文件的一行)
m1.hexdigest()

/*******正则表达式*********/
re.findall('\w','abc')
re.findall('\d+\.?\d*',3434jljl3.4ljl3)

/*******软件质量属性*********/
可扩展性
安全性
性能
成本
可靠性
可伸缩性
可移植性
可维护性


/*******面向对象*********/
面向過程：
    核心是“過程”二字
    過程的終極奧義就是將程序流程化
    過程是“流水線”，用来分步骤解决问题的
    优点
        将程序流程化，进而程序的设计会变得简单化
    缺点
        可扩展性差
面向对象：
    核心是“对象”二字
    对象的终极奥义就是将程序“整合”
    对象是“容器”，用来盛放数据与功能
    类也是“容器”，该容器用来存放同类对象共有的数据与功能
    优点：
        1.提升程序的解耦合程度，进而增强程序的可扩展性
    缺点：
        1.设计复杂
    一：现实生活中：
        1.先找出现实生活中的对象
        2.然后总结归纳出现实生活中的类
    二：程序中
        1.先定义程序中的类
        2.后调用类产生程序中对象（调用类的过程又称之为实例化）

类是对象相似数据与功能的集合体
所以类体中最常见的是变量与函数的定义，但是类体其实是可以包含任意其他代码的
注意，类体代码是在类定义阶段就立即执行，会产生类的名称空间

属性访问的语法
1.访问数据属性
2.访问函数属性

调用类的过程又称之为实例化，发生了三件事
1.先产生一个空对象
2.自动调用类中的__init__方法，然后将空对象以及调用类时括号内的参数一同传给__init__方法
3.返回初始化完的对象

总结__init__方法
1.会在调用类时自动触发执行，用来为对象初始化自己独有的数据
2.__init__内应该存放是为对象初始化属性的功能，但是可以存放任意其他代码
想要在类调用时就立刻执行的代码都可以放到该方法内
3.__init__方法必须返回None

类中存放的是对象共有的数据与功能
一：类可以访问：
1.类的数据属性
2.类的函数属性
二：但其实类中的东西是给对象用的
1.类的数据属性是共享给所有对象用的，访问的地址都一样
2.类中定义的函数主要是给对象使用的，而且是绑定给对象的，虽然所有对象指向的都是
相同的功能，但是绑定到不同的对象就是不同的绑定方法，内存地址各不相同
绑定方法的特殊之处在于：谁来调用绑定方法就会将谁当做第一个参数自动传入

一：封装介绍
封装是面向对象三大特性最核心的一个特性
封装<->整合

二、将封装的属性进行隐藏操作
1.如何隐藏：在属性名前加__前缀，就会实现一个对外隐藏属性效果
2.为何要隐藏
class Foo:
    __x=1
    def __f1(self):
        print('from test')
该隐藏需要注意的问题：
1、在类外部无法直接访问双下滑线开头的属性，但知道了类名和属性名就可以拼出名字：_类名__属性，
然后就可以访问了，如Foo._A__N，所以说这种操作并没有严格意义上地限制外部访问，仅仅只是一种语法意义上的变形。
2、这种隐藏对外不对内，因为在类定义阶段类内部双下滑线开头的属性统一发生了变形。
3、这种变形操作只在检查类语法的时候发生一次，之后定义的__开头的属性都不会发生变形

/*******property*********/(类装饰器)
装饰器是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象添加
新功能的可调用对象
案例一：
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height

    @property
    def bmi(self):
        return self.weight/(self.height **2)

obj1=People('egon',70,1.83)
print(obj1.bmi)

隐藏数据，开接口案例二：
class People:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def set_name(self,val):
        if type(val) is not str:
            print('必须传入str类型')
            return
        self.__name=val

    def del_name(self):
        print('不能删除')

    name = property(get_name, set_name, del_name)

案例三：
class Car:
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        self.__name=val

    @name.deleter
    def name(self):
        print('不能删除')

/*******继承*********/
继承是耦合思想的体现
1、什么是继承
    I继承是一种创建新类的方式，在Python中，新建的类可以继承一个或多个父类，
       新建的类可称为子类或派生类，父类又可称为基类或超类，子类会遗传父类的属性
    II需要注意的是：python支持多继承
       在Python中，新建的类可以继承一个或多个父类
class Parent1:
    pass
class Parent2:
    pass
class Sub1(Parent1): #单继承
    pass
class Sub2(Parent1,Parent2): #多继承
    pass

ps1:在Python2中有经典类与新式类之分
新式类：继承了object类的子类，以及该子类的子类子子类
    class Bar(object):
        pass
    Bar.__base__
经典类：没有继承object类的子类，以及该子类的子类子子类
    class Foo:
        pass
    Foo.__base__

ps2:在Python3中没有继承任何类，那么会默认继承object类，所以python3中
所有的类都是新式类

III:python的多继承
    优点：子类可以同时遗传多个父类的属性，最大限度地重用代码
    确点：
        1、违背人的思维习惯，继承表达的是一种什么"是"什么的关系
        2、代码可读性会变差
        3、不建议使用多继承，有可能会引发可恶的菱形问题，扩展性变差，如果真的涉及到一个子类不可避免地
        要重用多个父类的属性，应该使用Mixins

2、为何要用继承：用来解决类与类之间代码冗余问题

/*******属性查找*********/
类以及该类的对象访问属性都是参照该类的mro列表
print(class.mro())

python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止。
而这个MRO列表的构造是通过一个C3线性化算法来实现的。我们不去深究这个算法的数学原理,
它实际上就是合并所有父类的MRO列表并遵循如下三条准则:
1.子类会先于父类被检查
2.多个父类会根据它们在列表中的顺序被检查
3.如果对下一个类存在两个合法的选择,选择第一个父类

总结：类相关的属性查找(类名.属性，该类的对象.属性)，都是参照该类的mro

如果多继承是非菱形继承，经典类与新式类的属性查找顺序一样
都是一个分支一个分支地找下去，然后最后找object
class E:
    def test(self):
        print('from E')


class F:
    def test(self):
        print('from F')


class B(E):
    def test(self):
        print('from B')


class C(F):
    def test(self):
        print('from C')


class D:
    def test(self):
        print('from D')


class A(B, C, D):
    # def test(self):
    #     print('from A')
    pass


print(A.mro())
'''
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.F'>, <class '__main__.D'>, <class 'object'>]
'''

obj = A()
obj.test()

如果多继承是菱形继承，经典类与新式类的属性查找顺序不一样
经典类：深度优先，会在检索第一条分支的时候就直接一条道走到黑，即会检索大脑袋（共同的父类）
新式类：广度优先，会在检索最后一条分支的时候检索大脑袋
class G(object):
    def test(self):
        print('from G')

class E(G):
    def test(self):
        print('from E')

class F(G):
    def test(self):
        print('from F')

class B(E):
    def test(self):
        print('from B')

class C(F):
    def test(self):
        print('from C')

class D(G):
    def test(self):
        print('from D')

class A(B,C,D):
    # def test(self):
    #     print('from A')
    pass

obj = A()
obj.test() # 如上图，查找顺序为:obj->A->B->E->C->F->D->G->object
# 可依次注释上述类中的方法test来进行验证
总结：
多继承到底要不要用
要用，但是规避几点问题
1.继承结构尽量不要过于复杂
2.要在多继承的背景下满足继承的什么“是”什么的关系=》mixins

/*******mixins机制*********/
多继承的正确打开方式：mixins机制(多继承下的一种规范)
mixins机制核心：就是在多继承背景下尽可能地提升多继承的可读性
ps:让多继承满足人的思维习惯=》什么“是”什么（CivilAircraft是Vehicle）

class Vehicle:  # 交通工具
    def fly(self):
        '''
        飞行功能相应的代码
        '''
        print("I am flying")
class FlyableMixin: #(Mixin:混合)
    def fly(self):
        pass
class CivilAircraft(FlyableMixin,Vehicle):  # 民航飞机
    pass
class Helicopter(FlyableMixin,Vehicle):  # 直升飞机
    pass
class Car(Vehicle):  # 汽车并不会飞，但按照上述继承关系，汽车也能飞了
    pass

在子类派生的新方法中如何重用父类的功能
方式一：指名道姓调用某一个类下的函数=》不依赖于继承关系
class OldbodPeople:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def f1(self):
        print('%s say hello'%self.name)

class Teacher(OldboyPeople):
    def __init__(self.name,age,sex,level,salary):
        OldboyPeople.__init__(self,name,age,sex)
        self.level=level
        self.salary=salary
tea_obj=Teacher('egon',18,'male',10,3000)
print(tea_obj.__dict__)

方式二：super()调用父类提供给自己的方法=》严格依赖继承关系
调用super()会得到一个特殊的对象，该对象会参照发起属性查找的那个类的mro，去
当前类的父类中找属性
class OldbodPeople:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def f1(self):
        print('%s say hello'%self.name)

class Teacher(OldboyPeople):
    def __init__(self.name,age,sex,level,salary):
        super(Teacher,self).__init__(self,name,age,sex) #python2
        super().__init__(self,name,age,sex) #python3 调用的是方法，自动传入对象
        self.level=level
        self.salary=salary
tea_obj=Teacher('egon',18,'male',10,3000)
print(tea_obj.__dict__)

1.什么是多态：指的是同一事物多种形态（多态代表方法len()）
class Animal:
    pass

class People(Animal):
    pass

class Dog(Animal):
    pass
2.为何要有多态=》多态会带来什么样的特性，多态性
多态性指的是可以在不考虑对象具体类型的情况下而直接使用对象

def my_len(val):
    return val.__len__()

python推崇的是鸭子类型
抽象基类
import abc
class Animal(metaclass=abc.ABCMeta): #统一所有子类的标准
    @abc.abstractmethod
    def say(self):
        pass

一：绑定方法：特殊之处在于将调用者本身当做第一个参数自动传入
    1.绑定给对象的方法：调用者是对象，自动传入的是对象
    2.绑定定给类的方法：调用者类，自动传入的是类
    提供一种新的造对象的方式
class Mysql:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port

    def func(self):
        print('%s:%s'%(self.ip,self.port))

    @classmethod  #将下面的函数装饰成绑定给类的方法
    def from_conf(xxx):
        return xxx(settings.IP,settings.PORT)

二：非绑定方法：静态方法
    没有绑定给任何人：调用者可以是类、对象、没有自动传参的效果
class Mysql:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port

    @staticmethod #将下述函数装饰成一个静态方法
    def create_id():
        import uuid
        return uuid.uuid4()
掌握
dir()
for i,v in enumerate(['a','b','c'])
    print(i,v)
res=eval('1+2') #执行字符串中的表达式
print(res)
isinstance() #判断一个对象是否是类的实例
zip() 将两个迭代对象拼接在一起
__import__
t=__import__('time')
t.sleep(3)

/*******反射*********/
反射：指的是在程序运行过程中可以“动态”获取对象的信息(数据属性，函数属性)
python是动态语言，而反射(reflection)机制被视为动态语言的关键。
反射机制指的是在程序的运行状态中
对于任意一个类，都可以知道这个类的所有属性和方法；
对于任意一个对象，都能够调用他的任意方法和属性。
这种动态获取程序信息以及动态调用对象的功能称为反射机制。

实现反射机制的步骤
1先通过多dir：查看出某一个对象下可以.出哪些属性来
2.可以通过字符串反射到真正的属性上，得到属性值
print(obj.__dict__[dir(obj)[-2]])
为何要用反射
如何实现反射
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

四个内置函数的使用：通过字符串来操作属性值
1.hasattr()
print(hasattr(obj,'name'))
print(hasattr(obj,'x'))

2.getattr()
print(getattr(obj,'name'))

3.setattr()
print(setattr(obj,'name','EGON'))

4.delattr()
delattr(obj,'name')

/*******内置方法*********/
1、什么是内置方法
定义在类内部，以__开头并以__结尾的方法
特点：会在某种情况下自动触发执行
2、为何要用内置方法
为了定制化我们的类or对象
3、如何使用内置方法
__str__
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name

__del__

/*******元类*********/
引入：一切都源自于一句话：一切皆为对象
什么是元类
元类就是用来实例化产生类的类
关系：元类---实例化---》类(People)----实例化---》对象（obj)
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name
如何得到对象
obj=调用类()
obj=People('egon',18)

如果说类也是对象
People=调用类
查看内置的元类：我们用class关键字定义的所有的类以及内置的类
都是由内置的元类type实例化产生的

三：class关键字创造类People的步骤
类有三大特征：
1.类名
class_name="People"
2.类的基类
class_bases=(object,)
3.执行类体代码拿到类的名称空间
class_dic={}
class_body='''
def __init__(self,name,age):
    self.name=name
    self.age=age
def say(self):
    print("testing")
'''
exec(class_body,{},class_dic)
print(class_dic)
4.调用元类
People=type(class_name,class_bases,class_dic)

四：如何自定义元类来控制类的产生
class Mymeta(type):#只有继承了type类的类才是元类
    def __init__(self,x,y,z)
                #空对象，“People”,(object,),{...}
        print('run...')
        print(self)
        print(x)#类名
        print(y)#基类
        print(z)#类体
        if not x.iscapitalize():
            raise NameError('类名首字母大写')
People=Mymeta(class_name,class_bases,class_dic)
调用Mymeta发生三件事
1.先造一个空对象=》People
2.调用Mymeta这个类内的__init__方法，完成初始化对象的操作
3.返回初始化好的对象

class People(metaclass=Mymeta):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print("hello")

P404
"""
