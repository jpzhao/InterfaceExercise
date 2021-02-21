# -*- coding: utf-8 -*-
from multiprocessing import Process,Lock
import json
import time
import random

def search(i):
    with open('data','r',encoding='utf8') as f:
        dic=json.load(f)
    print('用户%s查询余票:%s'%(i,dic.get('ticket_num')))
    #字典取值不用[]的形式，推荐使用get，你写的代码打死都不能报错,字典赋键值对的时候用[]

def buy(i):
    with open('data','r',encoding='utf8') as f:
        dic=json.load(f)
    #模拟网络延迟
    time.sleep(random.randint(1,3))
    #判断当前是否有票
    if dic.get('ticket_num')>0:
        #修改数据库,买票
        dic['ticket_num']-=1
        with open('data','w',encoding='utf8') as f:
            json.dump(dic,f)
        print('用户%s买票成功'%i)
    else:
        print('用户%s买票失败'%i)

def run(i,mutex):
    search(i)
    #给买票环节加锁处理
    mutex.acquire()
    buy(i)
    #释放锁
    mutex.release()

if __name__ == '__main__':
    #在主进程生成一把锁，让所有的子进程抢，谁先抢到谁先买到
    mutex=Lock()
    for i in range(1,10):
        p=Process(target=run,args=(i,mutex))
        p.start()
'''
多个进程操作同一份数据的时候，会出现数据错乱的问题
针对上述问题，解决方式就是加锁处理：将并发变成串行，牺牲效率但是保证了数据的安全
行锁，表锁
注意:
1.锁不要轻易的使用，容易造成死锁现象
2.锁只在处理数据的部分来保证数据安全(只在争抢数据环节加锁处理)
'''