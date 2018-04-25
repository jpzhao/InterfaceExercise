#!/usr/bin/evn python3
# -*- coding: UTF-8 -*-
import time
import requests
import hashlib
from functools import reduce
import json
import appConfig as config

class createSign(object):
    def __init__(self,name='',password=''):
        self.name=name
        self.password=password

    def get_mark(self,token):
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
            'appVersion': config.appVersion,
            'sign': get_sign([config.appVersion, get_timestamp(), token, '']),
            'timestamp': get_timestamp(),
            'phone':self.name,
            'password':self.password
        }
        if 'token' in mark.values():
            mark.update(config.phoneInfo)
        return mark

    def get(self,path,token,data=config.phoneInfo):
        data.update(self.get_mark(token))
        parameter = ''
        for i in data:
            print(data[i])
            parameter += i + '=' + str(data[i]) + '&'
        #url = 'http://' + config.env + path + parameter.strip('&')
        url='http://' + config.env + path
        r = requests.get( url,parameter.strip('&'))
        return r

    def post(self,path, data=config.phoneInfo, token=config.token):
        data.update(self.get_mark(token))
        r = requests.post('http://' + config.env + path, data=data)
        return r

    def delete(self,path, data, token):
        data.update(self.get_mark(token))
        parameter = ''
        for i in data:
            parameter = parameter + i + '=' + data[i] + '&'
        url = 'http://' + config.env + path + parameter.strip('&')
        r = requests.delete(url)
        return r
