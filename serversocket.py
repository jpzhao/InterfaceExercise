# -*- coding: utf-8 -*-
import socket
#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#流式协议=》tcp协议
#绑定手机卡
phone.bind(('127.0.0.1',8080)) #0-65535,1024以前的都被系统保留使用
#开机
phone.listen(5)#5指的事半连接池的大小
#等待电话连接请求，拿到电话连接conn
while True:
    conn,client_addr=phone.accept()
    print(conn)
    print("客户端的IP和PORT", client_addr)
    while True:
        try:
            # 收\发消息
            data = conn.recv(1024)  # 最大接收的数据量为1024Bytes,收到的是bytes类型
            if len(data)==0:break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except Exception as e:
            print(e)
    #关闭电话连接conn
    conn.close()
#关机（可选操作）
#phone.close()