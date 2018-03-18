# -*- coding: UTF-8 -*-
import random
value1=random.randrange(100)
status=0
for i in range(0,7,1):
	try:
		number=int(raw_input("请填写数字，'q'&'Q' 代表退出游戏 :"))
	except ValueError :
		print ("请不要输入非数字字符")
		number = int(raw_input("请填写数字，'q'&'Q' 代表退出游戏 :"))
		while number !='q' or number!='Q':
			if number==value1:
				print('您答对了！')
				break
			elif number>value1:
				print('您的答案太大了')
				number = int(raw_input("答案过大请重新填写 :"))
				continue
			elif number<value1:
				print('您的答案太小了')
				number = int(raw_input("答案过小请重新填写 :"))
				continue
		print ('游戏已结束')
print ('您的7次机会已经用完')