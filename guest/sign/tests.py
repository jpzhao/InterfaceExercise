from django.test import TestCase
from sign.models import Event,Guest
# Create your tests here.

class ModelTest(TestCase):
	def setUp(self):
		Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,
		                     address='shezhen',start_time='2018-08-31 02:18:22')

		Guest.objects.create(id=1,event_id=1,realname='alen',
		                     phone='13312312311',email='alen@mail.com',sign=False)

	def test_event_models(self):
		result=Event.objects.get(name="oneplus 3 event")
		self.assertEqual(result.address,"shenzhen")
		self.assertTrue(result.status)

	def test_guest_models(self):
		result=Guest.objects.get(phone='13312312311')
		self.assertEqual(result.realname,"alen")
		self.assertFalse(result.sign)



