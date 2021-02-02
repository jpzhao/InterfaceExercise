# -*- coding: utf-8 -*-
from multiprocessing import Queue,Process,JoinableQueue
import time
import random

def producer(name,food,q):
    for i in range(6):
        data='%s生产了%s%s'%(name,food,i)
        time.sleep(random.randint(1,3))
        print(data)
        q.put(data)

def consumer(name,q):
    while True:
        food=q.get()
        #if food is None:break
        time.sleep(random.randint(1,3))
        print('%s吃了%s'%(name,food))
        q.task_done() #告诉队列你已经从里面取出了一个数据并且处理完毕了

if __name__ == '__main__':
    # q=Queue()
    q=JoinableQueue()#能够等待的队列
    p1 = Process(target=producer,args=('大厨egon','包子',q))
    p2 = Process(target=producer,args=('马叉','碳水',q))
    c1 = Process(target=consumer,args=('春哥',q))
    c2 = Process(target=consumer, args=('刘哥', q))
    p1.start()
    p2.start()
    c1.daemon=True
    c2.daemon=True
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    #等待生产者生产完毕之后，往队列中添加特定的结束符号
    #q.put(None)#肯定在所有生产者生产的数据的末尾
    #q.put(None)
    q.join()#等待队列中所有的数据被取完在执行往下执行代码
'''
生产者：生产/制造东西的
消费者：消费/处理东西的
该模型除了上述两个之外还需要一个媒介
    厨师做菜做完之后用盘子装着给消费者端过去
    生产者和消费者之间不是直接做交互的，而是借助于媒介做交互
生产者（做包子的）+消息队列（蒸笼）+消费者（吃包子的）
JoinableQueue每当你往该队列中存入数据的时候，内部会有一个计数器+1
每当你调用task_done的时候，计数器-1
q.join()当计数器为0的时候，才往后运行
'''
