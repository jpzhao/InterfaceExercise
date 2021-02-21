# -*- coding: utf-8 -*-
import sys
import dns.resolver
import re
from collections import Counter

def my_assert(cond,message):
    if cond !=1:
        raise Exception(message)

def diff_ip(file1,file2):
    result1=[]
    result2=[]
    with open(file1,'rb') as f1:
        ip1=f1.read().split('\n')
        for i in ip1:
            result1.append(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",i))
        li1=sum(result1,[])
    with open(file2,'rb') as f2:
        ip2=f2.read().split('\n')
        for j in ip2:
            result2.append(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",j))
        li2=sum(result2,[])
    my_assert(Counter(li1) == Counter(li2),"数据不一致{}".format(ip1))
    return "True"

def main():
    filenamelist=[]
    service='10.137.93.91'
    for line in open('域名文件'):
        for i in [53,5555]:
            line=line.strip().replace('\n','')
            msg=dns.message.make_query(line,ratype=1)
            result=dns.query.udp(msg,service,port=i)
            for i in range(len(result.answer)):
                text=result.answer[i]
            filename='file{}.txt'.format(i)
            filenamelist.append(filename)
            with open(filename,'w') as f:
                f.write(str(text))
        x,y=filenamelist[0],filenamelist[1]
        status=diff_ip(x,y)
        if status=='True':
            print('两个服务器dig解析结果一致{}'.format(text))

if __name__ == '__main__':
    main()