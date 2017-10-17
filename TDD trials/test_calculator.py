import unittest #if the code to be tested is in a folder in the same folder as the test file, use "from foldername.filename...."
from calculator import Calculator

class MyFirstTDD(unittest.TestCase):
	"""docstring for MyFirstTDD"""

	def test_calculator_addition(self):
		calc = Calculator()
		result = calc.add(2,2)
		self.assertEqual(4, result)
		pass
	def __init__(self):
		self.calc = Calculator()
		pass

	def test_calculator_addition(self):
		result = self.calc.add()
	if __name__ == '__main__':
		unittest.main()