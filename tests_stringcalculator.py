import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

	def test_zero_args(self):
		self.assertEqual(stringcalculator.add(""), 0)
	
	def test_one_args(self):
		self.assertEqual(stringcalculator.add("3"), 3)
		self.assertEqual(stringcalculator.add("35"), 35)
	
	def test_two_args(self):
		self.assertEqual(stringcalculator.add("3,7"), 10)
		self.assertEqual(stringcalculator.add("100,20"), 120)
	
	def test_any_args(self):
		self.assertEqual(stringcalculator.add("3,7,10,20"), 40)
		self.assertEqual(stringcalculator.add("100,20,1000"), 1120)
	
	def test_two_delimiters_args(self):
		self.assertEqual(stringcalculator.add("3,7\n10,20"), 40)
		self.assertEqual(stringcalculator.add("100\n20\n1000"), 1120)
		with self.assertRaises(ValueError):
			stringcalculator.add("100\n,20,\n1000")
	
	def test_dif_delimiters_args(self):
		self.assertEqual(stringcalculator.add("a\n3a7a10a20"), 40)
		self.assertEqual(stringcalculator.add("-\n100-20-1000"), 1120)
		with self.assertRaises(ValueError):
			stringcalculator.add("a\n100,20,1000")
			stringcalculator.add("a\n100a20aa1000")
		with self.assertRaises(TypeError):
			stringcalculator.add("a100,20,1000")
		with self.assertRaises(IndexError):
			stringcalculator.add("a")


if __name__ == '__main__':
	unittest.main()
