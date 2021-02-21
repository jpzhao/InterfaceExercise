# -*- coding: utf-8 -*-
from multiprocessing import Queue,Process
'''
1.主进程跟子进程借助队列通信
2.子进程跟子进程借助队列通信
'''

def producer(q):
    q.put('子进程存数据')
    print('hello')

def consumer(q):
    print(q.get())

if __name__ == '__main__':
    q=Queue()
    p=Process(target=producer,args=(q,))
    p1=Process(target=consumer,args=(q,))
    p.start()
    p1.start()
    #print(q.get())#主进程取数据