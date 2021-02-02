# -*- coding: utf-8 -*-
from multiprocessing import Process
import time
#第一种方式：
# def task(name):
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is over'%name)
#
# if __name__ == '__main__':
#     #1 创建一个对象
#     p=Process(target=task,args=('jason',))
#     #容器类型哪怕里面只有1个元素，建议一定要用逗号隔开
#     #2 开启进程
#     p.start()#告诉操作系统帮你创建一个进程，异步
#     print('主')
'''
定心丸：代码开启进程和线程方式，代码书写基本是一样的，你学会了如何开启进程就学会了如何开启线程
windows操作系统下，创建进程一定要在main内创建
因为windows下创建进程类似于模块导入的方式
会从上往下依次执行代码
linux中则是直接将代码完整的拷贝一份
总结：创建进程就是在内存中申请一块内存空间将需要运行的代码丢进去
一个进程对应在内存中就是一块独立的内存空间
多个进程对应在内存中就是多块独立的内存空间
进程与进程之间数据默认情况下是无法之间交互，如果想交互可以借助第三方工具，模块
join方法
join是让主进程等待子进程代码运行结束之后，在继续运行。不影响其他子进程的执行
'''

#第二种方式
# class MyProcess(Process):
#     def run(self):
#         print('Hello')
#         time.sleep(1)
#         print('get out!')
#
# if __name__ == '__main__':
#     p=MyProcess()
#     p.start()
#     print('主')

#join
# def task(name):
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is over'%name)
#
# if __name__ == '__main__':
#     #1 创建一个对象
#     p=Process(target=task,args=('jason',))
#     #容器类型哪怕里面只有1个元素，建议一定要用逗号隔开
#     #2 开启进程
#     p.start()#告诉操作系统帮你创建一个进程，异步
#     p.join() #主进程等待子进程p运行结束之后在继续往后执行
#     print('主')

def task(name,n):
    print('%s is running'%name)
    time.sleep(n)
    print('%s is over'%name)

if __name__ == '__main__':
    # p1 = Process(target=task,args=('jason',1))
    # p2 = Process(target=task, args=('egon',2))
    # p3 = Process(target=task, args=('tank',3))
    # start_time=time.time()
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    start_time = time.time()
    p_list=[]
    for i in range(1,4):
        p=Process(target=task,args=('子进程%s'%i,i))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
    print('主',time.time()-start_time)

'''
多道技术
空间与时间上的复用
空间上
    多个程序公用一套计算机硬件
时间上
    切换+保存状态
1.当一个程序遇到IO操作，操作系统会立刻剥夺该程序的cpu执行权限(提高了cpu利用率
并且不影响程序的执行效率)
2.当一个程序长时间占用cpu，操作系统也会立刻剥夺该程序的cpu执行权限(降低了程序
的运行效率但是玩出了并发的效果)
进程
程序就是一堆死代码
进程则是正在执行的过程

进程的调度算法
短作业优先调度算法
时间片轮转法+多级反馈队列

进程运行的三状态图
就绪态：一切程序必须要先过就绪态才能加入运行态
运行态：正在被cpu执行
阻塞态：程序遇到IO操作了
理想：希望开发的程序一直处于就绪态与运行之间

两个重要概念
同步与异步
任务的提交方式
同步 任务提交之后原地等待任务的返回结果期间不做任何事情
异步 任务提交之后不原地等待任务的返回结果执行下一行代码
    结果由异步回调机制做处理
阻塞非阻塞
程序的运行状态
阻塞：阻塞态
非阻塞：就绪态，运行态
上面的两对概念常会组合出现，但是最常用的就是异步非阻塞

开启进程的两种方式
'''