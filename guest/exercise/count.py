'''
Author:chongshi
Date:2018/01/31
Describe:加减乘除
'''

class Calculator():
	def __init__(self,a,b):
		self.a=int(a)
		self.b=int(b)

	def add(self):
		return self.a+self.b


	def sub(self):
		return self.a-self.b


	def mul(self):
		return self.a * self.b


	def div(self):
		return self.a/self.b

# test=Calculator(5,3)
# print(test)