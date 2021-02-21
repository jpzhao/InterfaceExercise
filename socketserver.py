# -*- coding: utf-8 -*-
from socket import *
import socketserver

class MyRequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        print(self.client_address)
        while True:
            try:
                msg=self.request.recv(1024)
                if len(msg)==0:break
                self.request.send(msg.upper())
            except Exception:
                break
        self.request.close()


# 1.循环从半链接池中取出链接请求与其建立双向的链接，拿到链接对象
s=socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyRequestHandle)
s.serve_forever()
#等同于
# while True:
#     conn,client_addr=server.accept()

#2 拿到链接对象，与其通信循环245596

