# -*- coding: utf-8 -*-
import queue
from multiprocessing import Queue
#创建一个队列
q=queue.Queue(5)#括号内可以传数字，表示生成的队列最大可以同时存放的数据量

#往队列中存数据
q.put(111)#当队列数据放满了之后，如果还有数据要放程序会阻塞，直到有位置让出来，不会报错
print(q.full())#判断当前队列是否满了
print(q.empty())#判断当前队列是否空
#去队列中取数据
v1=q.get()#队列中如果已经没有数据的话，get方法会原地阻塞
v2=q.get_nowait()#没有数据直接报错
v3=q.get(timeout=3)#没有数据之后原地等待3秒之后在报错 queue.Empty
print(v1)
'''
存取数据，存是为了更好的取
千方百计的存，简单快捷的取
队列Queue模块
管道：subprocess stdin stdout stderr
队列：管道+锁
队列：先进先出
堆栈：先进后出
q.full() q.empty() q.get_nowait()在多进程的情况下是不精确
IPC机制

'''