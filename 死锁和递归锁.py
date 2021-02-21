# -*- coding: utf-8 -*-
'''
死锁
当你知道锁的使用抢锁必须要释放锁，其实你在操作锁的时候也极其容易产生
死锁现象（整个程序卡死阻塞）
'''
from threading import Thread, Lock
import time

mutexA = Lock()
mutexB = Lock()


# 类只要加括号多次产生的肯定是不同的对象
# 如果你想要实现多次加括号得到的事相同的对象（单例模式）
class MyThead(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('%s 抢到A锁' % self.name)  # 获取当前线程名
        mutexB.acquire()
        print('%s 抢到B锁' % self.name)
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('%s 抢到B锁' % self.name)
        time.sleep(2)
        mutexA.acquire()
        print('%s 抢到A锁' % self.name)
        mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThead()
        t.start()
