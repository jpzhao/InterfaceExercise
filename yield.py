# -*- coding: utf-8 -*-

# def dog(name):
#     print('走到这里了%s'%(name))
#     while True:
#         #x拿到的是yield接收到的值
#         res=yield #x='肉包子'
#         print("又走到这里了%s"%(res))
#
# g=dog('alex')
# g.send(None) #等同于next(g)
# g.__next__()
# next(g)
# g.send('number No1.')
# g.send('number No2.')
# g.close()
# g.send(111)#关闭之后无法传值

def dog(name):
    food_list=[]
    print('刀哥%s准备吃东西拉菲。。。'%name)
    while True:
        # x拿到的是yield接收到的值
        x=yield food_list
        print('刀哥%s准备吃东西拉菲%s。。。'%(name,x))
        food_list.append(x)
g=dog('alex')
res=g.send(None)
print(res)
res=g.send('一根骨头')
print(res)
res=g.send('肉包子')
print(res)