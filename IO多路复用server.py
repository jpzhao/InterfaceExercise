# -*- coding: utf-8 -*-
'''
当监管的对象只有一个的时候，其实IO多路复用连阻塞IO都比不上
但是IO多路复用可以一次性监管很多个对象
监管机制是操作系统本身就有的，如果你想要用该监管机制（select）
需要你导入对应的select模块
监管：
socket=socket.socket()
conn=server.accept()
总结：
监管机制其实有很多
select机制  windows linux都有
poll机制  只在linux有 poll和select都可以监管多个对象，但是poll监管的数量更多
上述select和poll机制其实都不是很完美，当监管的对象特别多的时候
可能会出现 及其大的延时响应
epoll机制 只在linux有
 它给每一个监管对象都绑定一个回调机制
 一旦有响应 回调机制立刻发起提醒
针对不同的操作系统还需要考虑不同的检测机制，书写代码太多繁琐
有一个人能够根据你跑的平台的不同自动帮你选择对应的监管机制
selectors模块
'''
import select
import socket
server=socket.socket()
server.bind(('127.0.0.1',7070))
server.listen(5)
server.setblocking(False)
read_list=[server]
while True:
    r_list,w_list,x_list=select.select(read_list,[],[])
    '''
    帮你监管
    一旦有人来了 立刻给你返回对应的监管对象
    '''
    for i in r_list:
        '''针对不同的对象做不同的处理'''
        if i is server:
            conn,addr=i.accept()
            #也应该添加到监管队列中
            read_list.append(conn)
        else:
            res=i.recv(1024)
            if len(res)==0:
                i.close()
                #将无效的监管对象移除
                read_list.remove(i)
                continue
            print(res)
            i.send(b'hehe')
