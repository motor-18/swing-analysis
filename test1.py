"""
Testing the programs
"""
import unittest

from analysis import searchContinuityAboveThreshold
from analysis import errorDefinitions

errd = errorDefinitions()

data = range(0,100,1)

class TestFirst(unittest.TestCase):

    def testBasicOp(self):
        # testing basic operation
        result1 = searchContinuityAboveThreshold(data, 10, 50, 20, 5)
        self.assertEqual(result1, 20)
    
    def testBasicOp1(self):
        # testing basic operation
        result = searchContinuityAboveThreshold(data, 10, 50, 10, 5)
        self.assertEqual(result, 10)
    
    def testBasicOp2(self):
        # testing basic operation
        result = searchContinuityAboveThreshold(data, 10, 50, 12, 5)
        self.assertEqual(result, 12)

    def testTooSmall(self):
        # testing a failure case
        result2 = searchContinuityAboveThreshold(data, 0, 1, -1, 5)
        self.assertEqual(result2, errd.ERROR_TOO_SMALL)

    def testNoData(self):
        # testing another failure case
        result3 = searchContinuityAboveThreshold(None, 0, 100, 20, 3)
        self.assertEqual(result3, errd.ERROR_NO_DATA)

    def testNotFindingAnswerUsual(self):
        # testing case of not finding answer
        result4 = searchContinuityAboveThreshold(data, 10, 70, 72, 10)
        self.assertEqual(result4, errd.ERROR_NOT_FOUND)

    def testNotFindingAnswerUsual1(self):
        # another test case of not finding answer
        result5 = searchContinuityAboveThreshold(data, 20, 50, 60, 5)
        self.assertEqual(result5, errd.ERROR_NOT_FOUND)

    def testEdgeCaseAnswer(self):
        # testing edge case with an answer
        result6 = searchContinuityAboveThreshold(data, 0, 4, -1, 5)
        self.assertEqual(result6, 0)

    def testEdgeCaseNotFound(self):
        # testing edge case with no answer
        result7 = searchContinuityAboveThreshold(data, 0, 4, 7, 5)
        self.assertEqual(result7, errd.ERROR_NOT_FOUND)

    def testEdgeCaseNotEnough(self):
        # testing failure edge case
        result8 = searchContinuityAboveThreshold(data, 50, 99, 96, 10)
        self.assertEqual(result8, errd.ERROR_OUT_OF_BOUNDS)

if __name__ == '__main__':
    unittest.main()