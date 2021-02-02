# -*- coding: utf-8 -*-
from requests import Request,Session
import re

# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# r = requests.get("https://daily.zhihu.com/story/9731306", headers=headers)
# pattern = re.compile('(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# r=requests.get("https://github.com/favicon.ico")
# with open('favicon.ico','wb')as f:
#     f.write(r.content)

# data={'name':'germey','age':'22'}
# r=requests.post('http://httpbin.org/post',data=data)
# print(r.text)
# print(dir(r))
# print(r.status_code)
# print(r.cookies)
# print(type(r),r.headers)

# files={'file':open('favicon.ico','rb')}
# r=requests.post("http://httpbin.org/post",files=files)
# print(r.text)

# r=requests.get('https://www.baidu.com')
# print(r.cookies)
# print(dir(r.cookies))
# print(dir(r))
# for key,value in r.cookies.items():
#     print(key+'='+value)

# headers={
#     'Cookie':'_ga=GA1.2.1847200878.1608913314; Hm_lvt_3eec0b7da6548cf07db3bc477ea905ee=1608913313,1609032437; Hm_lpvt_3eec0b7da6548cf07db3bc477ea905ee=1609032437; _gid=GA1.2.894579702.1609032437',
#     'Host':'www.runoob.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
# }
# r=requests.get('https://www.runoob.com/http/http-content-type.html')
# print(r.text)

# response=requests.get('https://www.12306.cn')
# print(response.status_code)
# print(response.text)

url='http://httpbin.org/post'
data={
    'name':'germey'
}
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
s=Session()
req=Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)