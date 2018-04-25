#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
import time
import requests
import hashlib
from functools import reduce
import json

env = 'sc'
appVersion = '4.8.0'
token = 'token'
phoneInfo = {
        'channel': 'appStore',  # 渠道
        'imei': '6EE86199-5F1D-4F8E-9484-65285564341E',  # 手机imei
        'packageName': 'com.cpx.manager',  # 包名
        'phoneSystem': '10.2.1',  # 手机系统版本
        'phoneType': 'iPhone',  # 手机型号
        'platform': 'ios',  # 手机系统
        'pushToken': 'e86f06857395a3059a0ee7744e5ce9e653a95a20386160ade80597c0724f7736',  # 推送标志
        'appVersion': '4.8.0'
    }

def get_mark(token):
    def encryption(x, y):
        result = hashlib.md5()
        result.update(str(x).encode('utf-8'))
        return str(y) + result.hexdigest().upper()

    def get_timestamp():
        return str(int(time.time()))

    def get_sign(list):
        return reduce(encryption, list)

    mark = {
        'token': token,
        'appVersion': appVersion,
        'sign': get_sign([appVersion, get_timestamp(), token, '']),
        'timestamp': get_timestamp(),
    }
    mark.update(phoneInfo)
    return mark

def get(path, data, token):
    data.update(get_mark(token))
    parameter = ''
    for i in data:
        parameter = parameter + i + '=' + data[i] + '&'
    url = 'http://' + env + path + parameter.strip('&')
    r = requests.get(url)
    return r

def post(path, data, token):
    data.update(get_mark(token))
    r = requests.post('http://' +env + path, data=data)
    return r

def delete(path, data, token):
    data.update(get_mark(token))
    parameter = ''
    for i in data:
        parameter = parameter + i + '=' + data[i] + '&'
    url = 'http://' + env + path + parameter.strip('&')
    r = requests.delete(url)
    return r

def login(phone,password):
    data = {
        'phone': phone,
        'password': password,
    }
    r =post('.chupinxiu.com/app/user/login',data,'token')
    return r

tokenlogin=json.loads(login('','').text)['data']['token']


def cpxSystem():
    r=get('.chupinxiu.com/user/system?',phoneInfo,tokenlogin)
    print(r)

cpxSystem()

