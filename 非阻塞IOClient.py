# -*- coding: utf-8 -*-
from threading import Thread,current_thread
import socket

clinet=socket.socket()
clinet.connect(('127.0.0.1',8800))
while True:
    clinet.send(b'hello')
    data=clinet.recv(1024)
    print(data)
