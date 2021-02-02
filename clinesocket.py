# -*- coding: utf-8 -*-
import socket
#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#流式协议=》tcp协议
#拨通服务端电话
phone.connect(("127.0.0.1",8080))
#通信
while True:
    msg=input('输入要发送的消息>>>: ').strip()
    if len(msg)==0:continue
    phone.send(msg.encode('utf-8'))
    data=phone.recv(1024)
    print(data.decode('utf-8'))
#关闭连接(必须)
phone.close()