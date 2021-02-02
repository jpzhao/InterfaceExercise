# -*- coding: utf-8 -*-
'''
总结：
虽然非阻塞IO给你的感觉非常牛逼
但是该模型会长时间占用着CPU并且不干活让CPU不停的空转
实际应用中也不会考虑使用非阻塞IO模型
任何的技术点都有它存在的意义
实际应用或者是思想借鉴
'''
import socket
import time
server=socket.socket()
server.bind(('127.0.0.1',8800))
server.listen(5)
server.setblocking(False)
#将所有的网络阻塞变为非阻塞
r_list=[]
del_list=[]
while True:
    try:
        conn,addr=server.accept()
        r_list.append(conn)
    except BlockingIOError as e:
        # time.sleep(0.1)
        print('列表的长度',len(r_list))
        print('做其他事')
        for conn in r_list:
            try:
                data = conn.recv(1024) #没有消息 报错
                if len(data)==0:  #客户端断开链接
                    conn.close()  #关闭conn
                    #将无用的conn从r_list删除
                    del_list.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                continue
            except ConnectionResetError:
                conn.close()
                del_list.append(conn)
        #回收无用的链接
        for conn in del_list:
            r_list.remove(conn)
        del_list.clear()
