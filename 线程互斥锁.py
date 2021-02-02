# -*- coding: utf-8 -*-
from threading import Thread,Lock
from multiprocessing import Lock
import time

money=10
mutex=Lock()
def task():
    global money
    mutex.acquire()
    tmp=money
    time.sleep(1)
    money=tmp-1
    print(money)
    mutex.release()

if __name__ == '__main__':
    t_list=[]
    for i in range(10):
        t=Thread(target=task)
        t.start()
        t_list.append(t)

    for i in t_list:
        t.join()
    print(money)