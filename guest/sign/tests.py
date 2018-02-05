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
		User.objects.create_user('admin','admin@mail.com','admin123456')


	def test_add_admin(self):
		user=User.objects.get(username="admin")
		self.assertEqual(user.username,"admin")
		self.assertEqual(user.email,"admin@mail.com")

	def test_login_action_username_password_null(self):
		'''用户名密码为空'''
		test_data={'username':'','password':''}
		response=self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,200)
		self.assertIn(b"username or password error!",response.content)

	def test_login_action_username_password_error(self):
		'''用户名密码错误'''
		test_data={'username':'abc','password':'123'}
		response=self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,200)
		self.assertIn(b"username or password error!",response.content)

	def test_login_action_success(self):
		'''登录成功'''
		test_data={'username':'admin','password':'admin123456'}
		response=self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,302)

class EventManageTest(TestCase):
	'''发布会管理'''
	def setUp(self):
		User.objects.create_user('admin','admin@mail.com','admin123456')
		Event.objects.create(name="xiaomi5",limit=2000,address='beijing',
		                     status=1,start_time='2017-8-10 12:30:00')

		self.login_user={'username':'admin','password':'admin123456'}

	def test_event_mange_success(self):
		'''测试发布会：xiaomi5'''
		response=self.client.post('/login_action/',data=self.login_user)
		response=self.client.post('/event_manage/')
		self.assertEqual(response.status_code,200)
		self.assertIn(b"xiaomi5",response.content)
		self.assertIn(b"beijing",response.content)

	def test_event_manage_sreach_success(self):
		'''测试发布会搜索'''
		response=self.client.post('/login_action/',data=self.login_user)
		response=self.client.post('/search_name/',{"name":"xiaomi5"})
		self.assertEqual(response.status_code,200)
		self.assertIn(b"xiaomi5",response.content)
		self.assertIn(b"beijing",response.content)

class GuestManageTest(TestCase):
	'''嘉宾管理'''
	def setUp(self):
		User.objects.create_user('admin','admin@mail.com','admin123456')
		Event.objects.create(id=1,name="xiaomi5",limit=2000,address='beijing',
		                     status=1,start_time='2017-8-10 12:30:00')

		Guest.objects.create(realname="alen",phone=18611001100,
		                     email='alen@mail.com',sign=0,enent_id=1)
		self.login_user={'username':'admin','password':'admin123456'}

	def test_event_manage_success(self):
		'''测试嘉宾：alen'''
		response=self.client.post('/login_action/',data=self.login_user)
		response=self.client.post('/guest_manage/')
		self.assertEqual(response.status_code,200)
		self.assertIn(b"alen",response.content)
		self.assertIn(b"15910466104",response.content)

	def test_guest_manage_sreach_success(self):
		'''测试嘉宾搜索0'''
		response=self.client.post('/login_action/',data=self.login_user)
		response=self.client.post('/search_phone/',{"phone":"13312312311"})
		self.assertIn(b"alen",response.content)
		self.assertIn(b"alen",response.content)
		self.assertIn(b"1861001100",response.content)




