import unittest
import sys
sys.path.append("my_airbnb")
from base_model import Calculations


class Test_Calculations(unittest.TestCase):
    def test_get_sum(self):
        c = Calculations(5,5)
        self.assertEqual(c.get_sum(), 10, 'the sum is not correct')

if __name__ == '__main__':
    unittest.main()