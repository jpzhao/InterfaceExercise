# -*- coding: utf-8 -*-
'''
服务端应该能满足两个特点：
1.一直对外提供服务
2.并发地服务多个客户端
'''
import subprocess
from socket import *
import struct
import json
server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)
while True:
    conn,client_addr=server.accept()#第一件事，循环从连接池取出链接请求，建立双向链接。拿到链接对象
    while True:
        try:
            res=conn.recv(1024) #拿到链接对象，与其进行通信循环
            if len(res)==0:break
            obj=subprocess.Popen(res.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )
            stdout_res=obj.stdout.read()
            stderr_res=obj.stderr.read()
            total_size=len(stdout_res)+len(stderr_res)
            #1.制作头
            header_dic={
                "filename":"a.txt",
                "total_size":total_size,
                "md5":"1343jjlj434"
            }

            json_str=json.dumps(header_dic)
            json_str_byte=json_str.encode('utf-8')
            #2.先发头信息（固定长度的bytes）：对数据描述信息
            #int->固定长度的bytes
            x=struct.pack('i',json_str_byte)
            conn.send(x)
            #3发头信息
            conn.send(json_str_byte)
            #4再发真实数据
            conn.send(stdout_res)
            conn.setd(stderr_res)
        except Exception as e:
            break
    conn.close()