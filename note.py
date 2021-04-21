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

p201





1、什么是内置方法
定义在类内部，以__开头并以__结尾的方法
特点：会在某种情况下自动触发执行
2、为何要用内置方法
为了定制化我们的类or对象
"""
