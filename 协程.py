# -*- coding: utf-8 -*-
'''
进程：资源单位
线程：执行单位
协程：
    单线程下实现并发
    我们程序员自己再代码层面上检测我们所有的IO操作
    一旦遇到IO了，在代码级别完成切换
    给CPU的感觉是你这个程序一直运行，没有IO
    从而提升程序的运行效率
多道技术
    切换+保存状态
    cpu两种切换
    1.程序遇到IO
    2.程序长时间占用

TCP服务端
    accept
    recv

切换
    切换不一定是提升效率，也有可能是降低效率
    IO切提升
    没有IO切降低
保存状态
    保存上一次执行的状态，下一次来接着上一次的操作继续往后执行

总结：
我们可以通过
多进程下面开多线程
多线程下面开设协程
从而使我们的程序执行效率提升
'''
import time

# #串行执行计算密集型的任务 1.3650782108306885
# def func1():
#     for i in range(10000000):
#         i+1
# def func2():
#     for i in range(10000000):
#         i+1
# start_time=time.time()
# func1()
# func2()
# print(time.time()-start_time)

#切换+yield 2.286130905151367
# def func1():
#     while True:
#         10000000+1
#         yield
# def func2():
#     g=func1() #先初始化生成器
#     for i in range(10000000):
#         i+1
#         next(g)
# start_time=time.time()
# func2()
# print(time.time()-start_time)

