# -*- coding: utf-8 -*-
from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8082))

while True:
    cmd=input('Please input>>: ').strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    cmd_res=client.recv(1024)
    print(cmd_res.decode('utf-8'))