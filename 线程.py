# -*- coding: utf-8 -*-
#第一种开启方式：
# import time
# from multiprocessing import Process
# from threading import Thread
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(1)
#     print('%s is over'%name)
#
# t=Thread(target=task,args=('egon',))
# t.start() #创建线程的开销非常小，几乎是代码一执行线程就已经创建了
# print('主')

#第二种开启方式：
from threading import Thread
import time

class MyThead(Thread):

    def __init__(self,name):
        '''__init__的方法统一读成双下init'''
        super().__init__()
        self.name=name

    def run(self):
        print('%s is running'%self.name)
        time.sleep(1)
        print('%s is stopping'%self.name)

if __name__ == '__main__':
    t=MyThead('egon')
    t.start()
    print('master')
'''
线程理论
什么是线程
进程：资源单位（起一个进程仅仅只是在内存空间中开辟一块独立的空间
线程：执行单位（真正被cpu执行的其实是进程里面的线程，线程指的就是代码的执行过程，
执行代码中所需要使用到的资源都找所在的进程索要）
将操作系统比喻成一个大的工厂
那么进程就相当于工厂里面的车间
而线程就是车间里面的流水线
每一个进程肯定自带一个线程
总结：
进程和线程都是虚拟单位，只是为了我们更加方便的描述问题
为什么要有线程
开设进程
1.申请内存空间，耗资源
2.拷贝代码   耗资源
开设线程
一个进程内可以开设多个线程，在用一个进程内开设多个线程无需再次申请内存空间及
拷贝代码的操作
开设线程的开销远远小于进程的开销
同一个进程下的多个线程数据是共享的

开启线程的两种方式
开启线程不需要在main下面执行代码，直接书写就可以
但是我们还是习惯性的将启动命令写在main下面
'''