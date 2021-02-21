# -*- coding: utf-8 -*-
import re
txt='Hello,my phone number is 010-86432100 and email is cqc@cuiqingcai.com,and' \
    'my website is https://cuiqingcai.com.'

res=re.findall('[a-z A-Z]+://[^\s]*',txt)
print(res)

content='Hello 1234567 World_This is  a Regex Demo'
result=re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))