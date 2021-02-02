# -*- coding: utf-8 -*-
'''
GIL全局解释器锁（Global Interpreter Lock）
python解释器其实有多个版本
cpython
jpython
pypypython
但是普通使用的都是cpython解释器
在cpython解释器中GIL是一把互斥锁，用来阻止同一个进程下的多个线程的同时执行
同一个进程下的多个线程无法利用多核优势！！！
疑问：python的多线程是不是一点用都没有？？无法利用多核优势
因为cpython中的内存管理不是线程安全的
内存管理（垃圾回收机制）
1.引用计数
2.标记清除
3.分代回收

重点
1.GIL不是python的特点而是cpython解释器的特点
2.GIL是保证解释器级别的数据的安全
3.GIL会导致同一个进程下的多个线程的无法同时执行即无法利用多核优势
4.针对不同的数据还是需要加不同的锁处理
5.解释型语言的通病，同一个进程下多个线程无法利用多核优势


'''
from threading import Thread,Lock
import time
mutex=Lock()
money=10
def task():
    global money
    with mutex:
        tmp=money
        time.sleep(0.1)
        money=tmp-1

if __name__ == '__main__':
    t_list=[]
    for i in range(10):
        t=Thread(target=task)
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print(money)

'''
GIL与普通互斥锁的区别
10个线程起来之后，要先去抢GIL，抢到GIL之后执行task
在task里遇到sleep(0.1)睡眠，当前线程进入IO，GIL自动释放，当前线程手上还有一把自己的互斥锁
其他线程虽然抢到了GIL但是抢不到互斥锁
当睡眠时间，IO结束后，继续执行当前线程，直到释放当前线程手上的锁

同一个进程下的多线程无法利用多核优势，是不是就没有用了
多线程是否有用要看具体情况
单核：4个任务（IO密集型\计算密集型）
多核：4个任务（IO密集型\计算密集型）
计算密集型，每个任务都需要10s
单核：（不考虑）
    多进程：额外的消耗资源
    多线程：节省开销
多核：
    多进程：总耗时10
    多线程：总耗时40
--------------------------
IO密集型，每个任务都需要10s
多核：
    多进程：相对浪费资源
    多线程：更加节省资源
'''