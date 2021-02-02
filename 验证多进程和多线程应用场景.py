# -*- coding: utf-8 -*-

from multiprocessing import Process
from threading import Thread
import os,time

#计算密集型
# def work():
#     res=0
#     for i in range(10000000):
#         res*=i
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count())#获取当前计算机CPU个数
#     start_time=time.time()
#     for i in range(4):
#         p=Process(target=work)
#         t=Thread(target=work)
#         t.start()
#         # p.start()
#         # l.append(p)
#         l.append(t)
#     for t in l:
#         t.join()
#     print(time.time()-start_time)


#IO密集型
def work():
    time.sleep(2)
if __name__ == '__main__':
    l=[]
    print(os.cpu_count())#获取当前计算机CPU个数
    start_time=time.time()
    for i in range(40):
        p=Process(target=work)
        t=Thread(target=work)
        t.start()
        p.start()
        # l.append(p)
        l.append(t)
    for t in l:
        t.join()
    print(time.time()-start_time)

'''
多进程和多线程都有各自的优势
并且我们后面在写项目的时候通常可以
  多进程下面再开设多线程
这样的话既可以利用多核也可以介绍资源消耗
'''
