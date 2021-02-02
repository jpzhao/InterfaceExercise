# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def excuteSpider(url,headers,session):
    req=session.get(url,headers=headers)
    bsObj=BeautifulSoup(req.text,'html.parser')
    rankList=bsObj.find_all("div",{"class":"rank-index"})
    linkList=bsObj.find_all("span",{"class":"domain-like"})
    nameList=bsObj.find_all("div",{"class":"infos"})
    lranksub=[]
    llinksub=[]
    lnamesub=[]

    for rank in rankList:
        lranksub.append(rank.string.encode('utf-8').decode())

    for link in linkList:
        llinksub.append(link.a['href'].encode('utf-8').decode())

    for name in nameList:
        str1=name.contents[0].encode('utf-8').decode()
        s=str1.split('(')
        lnamesub.append(s[0])
    return lranksub,llinksub,lnamesub
if __name__ == '__main__':
    lrank=[]
    llink=[]
    lname=[]
    session=requests.Session()
    headers={"User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64;rv:56.0) Geoko/20100101"
                          "Firefox/56.0", "Accept":"*/*"}
    for i in range(1,26):
        if i==1:
            url="http://www.alexa.cn/siterank/"
        else:
            url="http://www.alexa.cn/siterank/"+str(i)
        lranksub,llinksub,lnamesub=excuteSpider(url,headers,session)
        lrank+=lranksub
        llink+=llinksub
        lname+=lnamesub
    wf=open('./spider4.csv','w')
    wf.write('rank,link,name\n')
    for i in range(len(lrank)):
        wf.write('%s,%s,%s\n'%(lrank[i],llink[i],lname[i]))
    wf.close()
    print('OK')