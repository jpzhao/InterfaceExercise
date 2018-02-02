from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User
# Create your tests here.

class ModelTest(TestCase):
	def setUp(self):
		Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,
		                     address='shenzhen',start_time='2018-08-31 02:18:22')

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

class IndexPageTest(TestCase):
	'''测试index登录首页'''

	def test_index_page_renders_index_template(self):
		'''测试index视图'''
		response=self.client.get('/index/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'index.html')

class LoginActionTest(TestCase):
	'''测试登录动作'''

	def setUp(self):
		User.objects.create_user('admin','admin@mail.com','123456')

	def test_add_admin(self):
		user=User.objects.get(username='admin','admin@mail.com','admin123')



