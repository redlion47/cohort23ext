import os
import unittest
from flask import Flask, render_template, request, json
import app
app = Flask(__name__)
class LoginTest(unittest.TestCase):
	"""docstring for LoginTest"""


	def test_mainPage(self):
		resp = app.test_client(self)
		response = resp.get('127.0.0.1:5000/', content_type ='html/txt')
		
		self.assertEqual(response.status_code, 404)
		

	def test_showLogin(self):
		tester = app.test_client(self)
		response = tester.get('/login', follow_redirects=True)
		self.assertEqual(response.status_code, 404)
		pass
		



if __name__ == '__main__':
    unittest.main()