# -*- coding: utf-8 -*-
'''
无论是开设进程也好还是开设线程也好，是不是都需要消耗资源
只不过开设线程的消耗比开设进程的稍微小一点而已
我们是不可能做到无限制的开设进程和线程的，因为计算机硬件的资源跟不上
硬件的开发速度远远赶不上软件
我们的宗旨应该是在保证计算机硬件能够正常工作的情况下最大限度的利用它
池的概念
什么是池？
池是用来保证计算机硬件安全的情况下最大限度的利用计算机
它降低了程序的运行效率，但是保证了计算机硬件的安全，从而让你写的程序能够正常运行
基本使用

'''
import socket
from threading import Thread

def communication(conn):
    while True:
        try:
            data=conn.recv(1024)
            if len(data)==0:break
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()

def server(ip,port):
    server = socket.socket()
    server.bind((ip,port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        #开设多进程或者多线程处理客户端通信
        t=Thread(target=communication,args=(conn,))
        t.start()

if __name__ == '__main__':
    s=Thread(target=server,args=('127.0.0.1', 8000))
    s.start()