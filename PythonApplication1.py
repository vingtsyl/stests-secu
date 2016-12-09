import unittest
from Request import Request


class TestStringMethods(unittest.TestCase):

	def test_equal(self):
		value = 5
		self.assertEqual(value, 5)
		
	def test_SimpleReq3(self):
		req = Request()
		res = req.send("http://wikipedia.fr",  'GET', None, None)
		print "status code: " + str(res.status_code)
		self.assertEqual(res.status_code, 200)

	def test_upper(self):
		self.assertTrue('FOO'.isupper())
		#self.assertFalse('Foo'.isupper())
		
	def test_equal2(self):
		value = 5
		self.assertEqual(value, 6)
	 

if __name__ == '__main__':
    unittest.main()
