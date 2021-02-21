# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote
result=urlparse('http://www.baidu.com:80/index.html;user?id=5#coment')
print(type(result),result)
print(dir(result))
print(result.port)

result1=urlparse('www.baidu.com/index.html;user?id=5#coment',scheme='https')
print(result1)

result2=urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
print(result2.scheme,result2[0],result2.netloc,result2[1],sep='\n')
print(result2)

data=['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))

result3=urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result3)
print(result3[1])

data1=['http','www.baidu.com','index.html','a=6','comment']
print(urlunsplit(data1))

print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))

params={
    'name':'germey',
    'age':22
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)

query='name=germey&age=22'
print(parse_qs(query))

query1='name=germey&age=22'
print(parse_qsl(query1))

keyword='壁纸'
url='https://www.baidu.com/s?wd='+quote(keyword)
print(url)

url='https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))