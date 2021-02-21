# -*- coding: utf-8 -*-
import struct
from socket import *
import json
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
while True:
    cmd=input("please input>>>: ").strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    #1接收端，先收4个字节，从中提取接下来要收的头的长度
    x=client.recv(4)
    header_len=struct.unpack('i',x)[0]
    #2接收头，并解析
    json_str_bytes=client.recv(x)
    json_str=json_str_bytes.decode('utf-8')
    header_dic=json.loads(json_str)
    print(header_dic)
    total_size=header_dic["total_size"]
    #3接收真实数据
    recv_size=0
    while recv_size<total_size:
        recv_data=client.recv(1024)
        recv_size+=len(recv_data)
        print(recv_data.decode('utf-8'),end='')