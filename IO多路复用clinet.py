# -*- coding: utf-8 -*-
import socket
client=socket.socket()
client.connect(('127.0.0.1',7070))

while True:
    client.send(b'hello world')
    data=client.recv(1024)
    print(data)