# -*- coding: utf-8 -*-

class Ftp:
    def put(self):
        print('正在执行上传功能')

    def get(self):
        print('正在执行下载功能')

    def interactive(self):
        method=input(">>>: ").strip()
        if hasattr(self,method):
            getattr(self,method)()
        else:
            print("您输入的指令不存在")

ftp=Ftp()
ftp.interactive()