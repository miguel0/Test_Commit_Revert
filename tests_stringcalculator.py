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
	
	def test_dif_separators_args(self):
		self.assertEqual(stringcalculator.add("3,7\n10,20"), 40)
		self.assertEqual(stringcalculator.add("100\n20\n1000"), 1120)


if __name__ == '__main__':
	unittest.main()
