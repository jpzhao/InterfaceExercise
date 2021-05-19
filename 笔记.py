# -*- coding: utf-8 -*-
'''
存一个值or多个值：存一个值称为原子类型，存多个值称为容器
ASCII表
1.只支持英文字符串
2.采用8位二进制数对应一个英文字符串
GBK表
1.支持英文字符，中文字符
2.采用8位（8bit=1Bytes）二进制数对应一个英文字符串
采用16位（16bit=2Bytes）二进制数对应一个中文字符串
unicode（内存中统一使用Unicode）
1.兼容万国字符
2.采用16位（16bit=2Bytes）二进制数对应一个中文字符串，
个别生僻会采用4Bytes，8Bytes
结论：
1.内存固定使用Unicode。我们可以改变的是存入硬盘采用格式
英文+汉字-》Unicode-》gbk
英文+日文-》Unicode-》shift-jis
万国字符-》Unicode-》utf-8
2.文本文件存取乱码问题
存乱了：解决方法是，编码格式应该设置成支持文件内字符串的格式
取乱了：解决方法是，文件是以什么编码格式存入硬盘的，就应该以什么编码格式读入内存
3.Python解释器默认读文件的编码
Python3默认:utf-8
Python2默认：ASCII
指定文件头修改默认的编码：#coding:gbk
4.保证运行Python程序前两个阶段不乱码的核心法则：
指定文件头
#coding：文件当初存入硬盘时采用的编码格式
5.python3的str类型默认直接存成unicode格式，无论如何都不会乱码保证python2的str
类型不乱码：x=u'上'
6.了解
python2解释器有两种字符串类型：str,unicode
#str类型
x='上' #字符串值会按照文件头指定的编码格式存入变量值的内存空间
#unicode类型
x=u'上' #强制存成unicode
------------------------------------------------------------------
1.集合内元素的三个特征
必须为不可变类型
无序
不重复
2.集合的用途是什么
关系运算
去重
3.举例说明关系运算
交集
并集
差集
对称差集
父子集
4.基于集合对列表去重l=[1,1,1,1,2,3,'a']
简述集合去重的局限性
    1.无法保证被去重对象的顺序
      l=list(set(l))
    2.从被去重对象中取出的元素必须都为不可变类型
      set(l)
----------------------------------------------------------
没有指定encoding参数操作系统会使用自己默认的编码
linux系统默认utf-8
Windows系统默认gbk
with open('c.txt',mode='rt',encoding='utf-8')as f:
    res=f.read() #t模式会将f.read()读出的结果解码成Unicode
    print(res,type(res))
内存：utf-8格式的二进制--解码--Unicode
硬盘：(c.txt内容：utf-8格式的二进制)
指针移动的单位都是以bytes/字节为单位
只有一种情况特殊：t模式下的read(n),n代表的是字符个数
with open('a.txt',mode='rt',encoding='utf-8')as f:
    res=f.read(4)
    print(res)
f.seek(n,模式)：n指的是移动的字节个数
模式：
0：参照物是文件开头位置
例：f.seek(9,0)  f.seek(3,0)
1：参照物是当前指针所在位置
例：f.seek(9,1) f.seek(3,1)
2:参照物是文件末尾位置，应该倒着移动
例：f.seek(9,2)  f.seek(3,2)
只有0模式可以在t下使用，1,2必须在b模式下使用
----------------------------------------------------------
def func():
    print('haha')
定义函数发生的事情
1.申请内存空间保存函数体代码
2.将上述内存地址绑定函数名
3.定义函数不会执行函数体代码，但是会检测函数体语法
调用函数发生的事情
1.通过函数名找到函数的内存地址
2.然后加括号就是在触发函数体代码的执行
调用函数
1.语句形式：只加括号调用函数
interactive()  add(1,2)
2.表达式形式
def add(x,y): #参数-》原材料
    res=x+y
    return res #返回值-》产品
res=add(1,2)
print(res)
res=add(1,2)*10
print(res)
3.函数调用可以当做参数
res=add(add(1,2),10)
print(res)
函数返回值
return是函数结束的标志，即函数体代码一旦运行到return会立刻终止函数的运行，
并且会将return后的值当做本次运行的结果返回：
1.返回NONE：函数体内没有return
return
return none
2.返回一个值：return 值
def func()
    return 10
res=func()
print(res)
3.返回多个值：用逗号分隔多个值，会被return返回成元组
def func():
    return 10,'aa',[1,2]
res=func()
print(res,type(res))
形参与实参介绍
形参：在定义函数阶段定义的参数称之为形式参数，简称形参，相当于变量名
def func(x,y):#x=1,y=2
    print(x,y)
实参：在调用函数阶段传入的值称之为实际参数，简称实参，相当于变量值
func(1,2)
形参与实参的关系：
在调用阶段，实参（变量值）会绑定给形参（变量名）
这种绑定关系只能在函数体内使用
实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定关系
实参是传入的值，单值可以是以下形式
形式一：func(1,2)
形式二：a=1,b=2 func(a,b)
形式三：func(int('1'),2),func(func1(1,2,),func2(2,3),333)
混合使用，强调
位置实参必须放在关键字实参前
不能为同一个形参重复传值
默认参数
默认形参：在定义函数阶段，就已经被赋值的形参，称之为默认参数
特点：在定义阶段就已经被赋值，意味着在调用阶段可以不用为其赋值
位置形参与默认形参混用，强调：
1.位置形参必须在默认形参的左边
2.默认参数的值是在函数定义阶段被赋值的，准确地说被赋予的是值的内存地址
示范1：
m=2
def func(x,y=m): y=>2的内存地址
    print(x,y)
示范2：
m=[11111,]
def func(x,y=m):#y=>[1111,]的内存地址
    print(x,y)
3.虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
函数最理想的状态：函数的调用只跟函数本身有关系，不受外界代码的影响。
def func(x,y,z,l=None):
    if l is None:
        l=[]
        l.append(x)
        l.append(y)
        l.append(z)
        print(l)
可变长度的位置参数
*形参名：用来接收溢出的位置实参，溢出的位置实参会被*保存成元组的格式然后赋值紧跟其后的
*后跟的可以是任意名字，但是约定俗成应该是args
可变长度的关键字参数
**形参名：用来接收溢出的关键字实参，**会将溢出的关键字实参保存成字典格式，然后赋值给紧跟其后的
**后跟的可以是任意名字，但是约定俗成应该是kwargs
def func(x,y,**kwargs):
    print(x,y,kwargs)
func(1,y=2,a=1,b=2,c=3)
*可以用在实参中，实参中带*，先*后的值打散成位置实参
def func(x,y,z):
    print(x,y,z)
func(*[11,22,33])
形参与实参中都带*
def func(x,y,*args):#args=(3,4,5,6)
    print(x,y,args)
func(1,2,[3,4,5,6])
func(1,2,*[3,4,5,6])#func(1,2,3,4,5,6)
**可以用在实参中（**后跟的只能是字典），实参中带**，先**后的值
def func(x,y,z):
    print(x,y,z)
func(*{'x':1,'y':2,'z':3}) func('x','y','z')
func(**{'x':1,'y':2,'z':3}) func(x=1,y=2,z=3)
func(**{'x':1,'y':2}) func(x=1,y=2)
混用*与**：*args必须在**kwargs之前
def func(x,*args,**kwargs):
    print(args)
    print(kwargs)
0：引用传递
python中所有值的传递，传递的都不是值本身，而是值的引用，即内存地址
1：函数分为两大类，分别是什么？二者在使用时有何区别？
内置函数，自定义函数
2：什么是形参，什么是实参，形参与实参之间的关系是什么
def func(x,y):
    print(x)
    func(1,2)
3:简述两个形参的区别：位置形参，默认形参
x=1
def func(name,age,gender='male'):
    pass
func('egon',18)
func('egon1',19)

x=[]
def func(name,age,gendr=不可变类型）：gender=列表的内存地址
    print（gender)
    x.append(111)
    func('egon',18)
    ps:函数最理想的状态是函数的运行不受外界代码的干扰
-------------------------------------------------------------------
解释下述形式，即函数wrapper的参数特点是什么
def index(x,y,z):
    print(x,y,z)
def wrapper(*args,**kwargs):args=(1,)kwargs={'y':2,'z':3}
    index(*args,**kwargs)
    index(*(1,),**{'y':2,'z':3})
    index(1,z=3,y=2)
wrapper(1,z=3,y=2)
命名关键字参数（了解）
命名关键字参数：在定义函数时，*后定义的参数，如下所示，称之为命名关键字参数
特点：1.命名关键字实参必须按照key=value的形式为其传值
def func(x,y,*,a,b)#其中，a和b称之为命名关键字参数
    print(x,y)
    print(a,b)
func(1,2,b=222,a=111)
组合使用（了解）
位置形参，默认形参，*args,命名关键字形参，**kwargs
def func(x,y=111,*args,z,**kwargs):

1.1名称空间namespacs：存放名字的地方，是对栈区的划分
有了名称空间之后，就可以在栈区中存放相同的名字，详细的，名称空间
分为三种
内置名称空间
存放的名字：存放的python解释器内置的名字
print <built-in function print>
input <built-in function input>
存活周期：python解释器启动则产生，python解释器关闭则销毁
1.2全局名称空间
存放的名字：只要不是函数内定义、也不是内置的，剩下的都是全局名称空间的名字
存活周期：python文件执行则产生，python文件运行完毕后销毁
1.3局部名称空间
存放的名字：在调用函数时，运行函数体代码过程中产生的函数内的名字
存活周期：在调用函数时存活，函数调用完毕后则销毁
重点1
名词查找：当前所在的位置向外查找
局部名称空间-》全局名称空间-》内置名称空间
重点2
名称空间只有优先级之分，本身并无嵌套关系，画图只是为了理解
重点3
名称空间的嵌套关系决定了名字的查找顺序
而名称空间的嵌套关系是以函数定义阶段为准的
即函数的嵌套关系与名字的查找顺序是在定义阶段就已经确定好的
1.可以赋值
f=func
print(f,func)
f()
2.可以当做函数当做参数传给另外一个函数
def foo(x): x=func的内存地址
    print(x)
    x()
foo(func) foo(func的内存地址)
3.可以当做函数当做另外一个函数的返回值
精髓：可以把函数当成变量去用
func=内存地址
函数嵌套
1.函数的嵌套调用：在调用一个函数的过程中又调用其他函数
def max2(x,y):
    if x>y:
        return x
    else:
        return y
def max4(a,b,c,d):
    res1=max2(a,b)
    res2=max2(res1,c)
    res3=max2(res2,d)
    return res3
res=max4(1,2,3,4)
print(res)
2.函数的嵌套定义：在函数内定义其他函数
def f1():
    def f2():
        pass
圆形
from math import pi
求周长：2*pi*radius
求面积：pi*(radius**2)
def circle(radius,action=0):
    from math import pi
    求圆形的周长
    def perimiter(radius):
        return 2*pi*radus
    求圆形的面积
    def area(radius):
        return pi*(radius**2)
    if action==0:
        return perimiter(radius)
    elif action==1:
        return area(radius)
circle(33,action=0)
一：大前提：
闭包函数=名称空间与作用域+函数嵌套+函数对象
核心点：名字的查找关系是以函数定义阶段为准
二：什么是闭包函数
“闭”函数指的该函数是内嵌函数
“包”函数指的该函数包含对外层函数作用域名字的引用（不是对全局作用域）
def f1():
    def f2():
        pass
闭包函数：函数对象
def f1():
    x=33333
    def f2():
        print('函数f2: ',x)
    return f2
f=f1()
三：为何要有闭包函数=》闭包函数的应用
两种为函数体传参的方式：
方式一：直接把函数体需要的参数定义成形参
def f2(x)
    print(x)
------------------------------------------------------------------
装饰器
1什么是装饰器
器指的是工具，可以定义成函数
装饰指的事为其他事物添加额外的东西点缀
合到一起的解释：
装饰器指的定义一个函数，该函数是用来为其他函数添加额外的功能
2为何要使用装饰器
开发封闭原则
开放：指的是对拓展功能是开放的
封闭：指的是对修改源代码是封闭的
装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下为被装饰对象添加新功能
import time
def index(x,y,z):
    time.sleep(3)
    print('index %s %s %s'%(x,y,z))
def wrapper(*args,**kwargs):
    start=time.time()
    index(*args,**kwargs)
    stop=time.time()
    print(stop-start)
wrapper(333,444,555)

总结无惨装饰器模板
def outter(func):
    def wrapper(*args,**kwargs):
        1.调用原函数
        2.为其增加新功能
        res=func(*args,**kwargs)
        return res
    return warpper

无参装饰的模板：
def outter(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return res
    return wrapper
装饰的目标：
装饰器就是在不修改不被装饰器对象源代码与调用方式的前提下为其添加新功能
import time
@名字 home=名字(home)
@outter index=outter(index) #index=函数wrapper的内存地址
def index(x,y):
    print('index->%s %s'%(x,y))
@outter
def home(a,b,c):
    pass
def outter(func):
    func=被装饰对象的内存地址
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs) #index(y=3,x=4)
        stop=time.time()
        print(stop-start)
    return wrapper

def outter(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return res
    return wrapper
@outter
def index(x,y):
    print(x,y)
index(1,2)

偷梁换柱，即将原函数名指向的内存地址偷梁换柱成wrapper函数
所以应该将wrapper做的跟原函数一样才行
from functools import wraps
def outter(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return res
    手动将原函数的属性赋值给wrapper函数
    1.函数wrapper.__name__=原函数.__name__
    2.函数wrapper.__doc__=func.__doc__
    wrapper.__name__=func.__name__
    wrapper.__doc__=func.__doc__
    return wrapper
@outter#index=outter(index)
def index(x,y):
有参装饰器模板
def 有参装饰器(x,y,z):
    def outter(func):
        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            return res
        return wrapper
    return outter
@有参装饰器(1,y=2,z=3)
def 被装饰对象():
    pass
-----------------------------------------------------------------------
1.什么是迭代器
迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，
单纯的重复并不是迭代
2.为何要有迭代器
迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的类型
有：列表，字符串，元组，字典，集合，打开文件
l=['egon','liu','alex']
i=0
while i<len(i):
    print(l[i])
    i+=1
上述迭代取值的方式只适用于有索引的数据类型：列表，字符串，元组
为了解决基于索引迭代器取值的局限性
python必须提供一种能够不依赖索引的取值方式，这就是迭代器
可迭代对象：但凡内置有__iter__方法的都称之为可迭代的对象
s1='' s1.__iter__()
l=[]   l.__iter__()
t=(1,)  t.__iter__()
d={'a':1}  d.__iter__()
set1={1,2,3}  set1.__iter__()
with open('a.txt',mode='w') as f:
    f.__iter__()
调用可迭代对象下的__iter__方法会将其转换成迭代器对象
d={'a':1,'b':2,'c':3}
d_iterator=d.__iter()
print(d_iterator)
print(d_iterator.__next__())
while Ture:
    try:
        print(d_iterator.__next__())
    except StopIteratoion:
        break
print('=====>>>>')
可迭代对象与迭代器对象详解
可迭代对象(“可以转换成迭代器对象”):内置__iter__方法对象
可迭代对象.__iter__()：得到迭代器对象
迭代器对象：内置有__next__方法且内置有__iter__方法的对象
迭代器对象.__next__():得到迭代器的下一个值
迭代器对象.__iter__():得到迭代器的本身，说白了调了跟没调一个样子
dic={'a':1,'b':2,'c':3}
dic_iterator=dic.__iter__()
print(dic_iterator is dic_iterator.__iter__().__iter__().__iter__())
for循环的工作原理:for循环可以称之为叫迭代器循环
dic={'a':1,'b':2,'c':3}
1.d.__iter__()得到一个迭代器对象
2.迭代器对象.__next__()拿到一个返回值，然后将返回值赋值给k
3.循环往复步骤2，值到抛出StopIteration异常for循环会捕捉异常然后结束循环
for k in d:
    print(k)
-----------------------------------------------------------------------
如何得到自定义的迭代器：
在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
会返回一个生成器对象，生成器即自定义的迭代器
def func()
    print('第一次')
    yield1
    print('第二次')
    yield2
    print('第三次')
    yield3
g=func()
print(g)
生成器就是迭代器
g.__iter__()
g.__next__()
会触发函数体代码的运行，然后遇到yield停下来，将yield后的值，当做本次调用的结果返回
res1=g.__next__()
print(res1)
def my_range(start,stop,step=1):
    print('start....')
    whiel start<stop:
        yield start
        start+=step
    print('end....')
g=my_range(1,5,2)
res=next(g)
print(res)
有了yield关键字，我们就有了一种自定义迭代器的实现方式，yield可以用于返回值，但不同于return,
函数一旦遇到return接结束了，而yield可以保存函数的运行状态挂起函数，用来返回多次值。
-----------------------------------------------------------------------
一段代码的循环运行的方案有两种
方式一：whiel,for 循环
while True:
    print(111)
    print(222)
方式二：递归的本质就是循环
def f1():
    print(111)
    print(222)
    f1()
f1()
函数的递归调用：是函数嵌套调用的一种特殊形式
具体是指：
    在调用一个函数的过程中又直接或者间接地调用到本身
直接调用本身
def f1():
    print('是我')
    f1()
f1()
间接调用本身
def f1():
    print('=====f1')
    f2()
def f2():
    print('====f2')
    f1()
需要强调的一点是：
递归调用不应该无限地调用下去，必须在满足某种条件下结束递归调用
n=0
while n<10:
    print(n)
    n+=1
递归的两个阶段
回溯：一层一层调用下去
地推：满足某种结束条件，结束递归调用，然后一层一层返回
递归的应用
l=[1,2,[3,[4,5,6[7,8]]]]
for x in l:
    if type(x) is list:
    如果是列表，应该在循环，在判断，即重新运行本身的代码
        f1(x)
    else:
        print(x)

算法：是最高效解决问题的办法
算法之二分法
需求：有一个按照从小到大顺序排序的数字列表
需要从该数字列表中找到我们想要的那个一个数字，如何高效
编程思想/范式
面向过程的编程思想：
核心是“过程”二字，过程即流程，指的事做事的步骤：先什么，再什么，后干什么
基于该思想编写程序就好比设计一条流水线
有点：复杂的问题流程化，进而简单化
缺点：扩展性非常差
面向过程的编程思想应用场景解析：
不是所有的软件都需要频繁更迭，比如编写脚本
即便是一个软件需要频繁更迭，也不并不代表这个软件所有的组成部分都需要一起更迭
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
方式二：
func=lambda x,y:x+y
res=func(1,2)
print(res)
4.匿名用于临时调用一次的场景：更多的是将匿名与其他函数配合使用
map：
l=['alan','alex','tom']
res=map(lambda name:name+'_test',l)
print(res)#生成器
filter:
l=['alan_sb','alex','tom_sb']
res=filter(lambda name:name.endswith('sb'),l)
print(res)
reduce:
from functools import reduce
res=reduce(lambda x,y:x+y,[1,2,3],10)
print(res)
-------------------------------------------------------------
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
--------------------------------------------
递归：
def salary(n):
    if n==1:
        return 5000
    res=salary(n-1)+1000
    return res
res=salary(4)

1.当foo.py被运行时，__name__的值为'__main__'
2.当foo.py被当做模块导入时，__name__的值为'foo'

from...import...导入也发生了三件事
1产生一个模块的名称空间
2运行foo.py将运行过程中产生的名字都丢到模块的名称空间去
3在当前名称空拿到一个名字，该名字与模块名称空间中的某一个内存地址
from foo import x
from foo import get

from...import...导入模块在使用时不用加前缀
优点：代码更精简
缺点：容易与当前名称空间混淆
from foo import x #x=模块foo中值111的内存地址
x=1111
__all__=['x',]#控制*代表的名字有哪些
from foo import get as g起别名
无论是import还是from...import在导入模块时都涉及查找
优先级：
1内存（内置模块）
2按照sys.path中存放的文件的顺序依次查找要导入的模块
import sys
值为一个列表，存放了一系列的对文件夹
其中第一个文件夹是当前执行文件所在的文件夹
print(sys.path)
了解：sys.modules查看已经加载到内存中的模块
import sys
import foo
print('foo' in sys.modules)
import sys
sys.path.append(r'/user/xxx/xxx')

1.包就是一个包含有__init__.py文件的文件夹
2.为何要有包
1包的本质就是模块的模块的一种形式，包是用来被当做模块导入
产生一个名称空间
2运行包下的__init__.py文件，将运行过程中产生的名字都丢到1的名称空间中
3在当前执行文件的名称的空间中拿到一个名字mmm，mmm指向1的名称空间
import mmm
#绝对导入，以包的文件夹作为起始来进行导入
from m1 import f1
环境变量是以执行文件为准备的，所有的被导入的模块或者说后续的其它文件引用
的sys.path都是参照执行文件的sys.path
相对导入：仅限于包内使用，不能跨出包（包内模块之间的导入，推荐使用相对导入）
.:代表当前文件夹
..:代表上一层文件夹
import...强调
1相对导入不能跨出包，所以相对导入仅限于包内模块彼此之间闹着玩
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
------------------------------
import time
时间分为三种格式：
1时间戳从1970年到现在经过的秒数
print(time.time())
2按照某种格式显示的时间：2020-03-30 11:11:11
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
print(time.strftime('%Y-%m-%d %X'))

def make_code(size=4):
    res=''
    for i in range(size):
        s1=chr(random.randint(65,90))
        s2=str(random.randint(0,9))
        res+=random.choice([s1,s2])
    return res
print(make_code(6))

src_file=sys.argv[1]
dst_file=sys.argv[2]
with open(r'%s' %src_file,mode='rb') as read_f,open(r'%s' %dst_file,mode='wb') as write_f:
    for line in read_f:
        write_f.write(line)
-----------------------------------------------------------------
什么是序列化，反序列化
内存中的数据类型---》序列化----》特定的格式(json格式或者pickle格式)
内存中的数据类型---》反序列化----》特定的格式(json格式或者pickle格式)
土方法：
{'aaa':111}--->序列化str({'aaa':111})---->"{'aaa':111}"
{'aaa':111}--->反序列化eval("{'aaa':111}")---->"{'aaa':111}"
为何要序列化
序列化得到结果-》特定的格式的内容有两种用途
1.可用于存储-》用于存档
2.传输给其他平台使用-》跨平台数据交互
python             java
列表     特定格式    数组
强调：
针对用途1的特定-格式：可是一种专用的格式=》pickle只有python可以识别
针对用途2的特定-格式：应该是一种通用，能够被所有语言识别的格式=》json
如何序列化和反序列化
import json
json_res=json.dumps([1,'aaa',True,False])

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
202012130049
'''