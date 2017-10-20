import os
import unittest

import app
class LoginTest(unittest.TestCase):
	"""docstring for LoginTest"""

	def setup(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False

		self.path = app.main()

		pass

	def tearDown(self):
		pass

	def test_home(self):
		resp = self.path.get('/', follow_redirects = True)
		self.assertEqual(resp.statu_code, 200)
		pass
	def test_login_method(self):
		pass
		



if __name__ == '__main__':
    unittest.main()