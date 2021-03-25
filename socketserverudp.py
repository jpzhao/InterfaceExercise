# -*- coding: utf-8 -*-
import socketserver_test

class MyRequestHanlde(socketserver_test.BaseRequestHandler):
    def handle(self):
        client_data=self.request[0]
        server=self.request[1]
        client_address=self.client_address
        print('客户端发来的数据%s'%client_data)
        server.sendto(client_data.upper(),client_address)

s=socketserver_test.ThreadingUDPServer(('127.0.0.1', 9999), MyRequestHanlde)
s.serve_forever()