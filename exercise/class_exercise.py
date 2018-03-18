class AddBookEntry(object):
	def __init__(self,nm,ph):
		self.name=nm
		self.phone=ph
		print('Created instance for:',self.name)

	def updatePhone(self,newph):
		self.phone=newph
		print ('Updated phone# for:',self.name)

class EmplAddrBookEntry(AddBookEntry):
	def __init__(self,nm,ph,id,em):
		AddBookEntry.__init__(self,nm,ph)
		self.empid=id
		self.email=em

	def updateEmail(self,newem):
		self.email=newem
		print 'Updated e-mail address for:',self.name

hozn=EmplAddrBookEntry('alan',13312312311,01,'abc@sina.com')
print hozn.email