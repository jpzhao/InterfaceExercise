# -*- coding: utf-8 -*-
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input('>>>: ').strip()
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8801))
    data,server_addr=client.recvfrom(1024)
    print(data.decode('utf-8'))
client.close()