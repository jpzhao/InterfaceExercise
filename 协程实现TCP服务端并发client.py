# -*- coding: utf-8 -*-
from threading import Thread,current_thread
import socket

def x_client():
    clinet=socket.socket()
    clinet.connect(('127.0.0.1',8080))
    n=0
    while True:
        msg='%s say hello %s'%(current_thread().name,n)
        n+1
        clinet.send(msg.encode('utf-8'))
        data=clinet.recv(1024)
        print(data.decode('utf-8'))

if __name__ == '__main__':
    for i in range(100):
        t=Thread(target=x_client)
        t.start()
