#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

def get_one_page(url):
    headers={
        'User-Ager':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    response=requests.get(url,headers=headers,verify=False)
    if response.status_code==200:
        # response.encoding = 'ISO-8859-1'
        print(response.content.decode('utf-8'))
        return response.text
    return None

def main():
    url='https://maoyan.com/board/4'
    html=get_one_page(url)
    print(html)

main()