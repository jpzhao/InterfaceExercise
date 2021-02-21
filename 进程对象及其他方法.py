# -*- coding: utf-8 -*-
from multiprocessing import Process,current_process
import time
import os

def task():
    print('%s is running'%current_process().pid)#查看当前进程号
    print('%s is running' %os.getpid())
    time.sleep(3)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    p.terminate() #杀死当前进程
    #告诉操作系统帮你去杀死当前进程，但是需要一定的时间
    time.sleep(0.1)
    print(p.is_alive())#判断当前进程是否存活
    '''
    一般情况下我们会默认将存储布尔值的变量名
    和返回的结果是布尔值的方法名都以is_开头
    '''
    print('主',current_process().pid)
    print('主主',os.getppid())

'''
一台计算机上面运行着很多进程，那么计算机是如何区分并管理这些进程服务端的呢？
计算机会给每一个运行的进程分配一个PID号
如何查看
    windows电脑加入cmd输入tasklist即可查看
    tasklist |findstr PID
'''