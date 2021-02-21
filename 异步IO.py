# -*- coding: utf-8 -*-
'''
asyncio
异步IO模型是所有模型中效率最高的 也是使用最广泛的
相关的模块和框架
模块：asyncio模块
框架：sanic tronado twisted
特点：速度快
'''
import asyncio
import threading
@asyncio.coroutine
def hello():
    print('hello world %s'%threading.current_thread())
    yield  from asyncio.sleep(1)
    print('hello world %s' % threading.current_thread())

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()