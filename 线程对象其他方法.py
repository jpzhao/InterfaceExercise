# -*- coding: utf-8 -*-
from threading import Thread,active_count,current_thread
import os,time
def task():
    print('backup',os.getpid())
    print('backup',current_thread().name)

if __name__ == '__main__':
    t=Thread(target=task)
    t.start()
    print('master',active_count()) #统计当前正在活跃的线程数
    print('master',os.getpid())
    print('master',current_thread().name)#获取线程名字