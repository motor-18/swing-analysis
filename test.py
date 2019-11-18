"""
Testing the programs
"""
import unittest

from analysis import searchContinuityAboveThreshold()

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test the first main function with simple array
        """
        data = range(0,100,1)
        result1 = searchContinuityAboveThreshold(data, 10, 50, 20, 5)
        self.assertEqual(result1, 20)

if __name__ == '__main__':
    unittest.main()