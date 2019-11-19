"""
Testing the programs
"""
import unittest

from analysis import backSearchContinuityWithinRange
from analysis import errorDefinitions

errd = errorDefinitions()

data = range(0,100,1)

class TestFirst(unittest.TestCase):

    def testBasicOp(self):
        # testing basic operation
        result1 = backSearchContinuityWithinRange(data, 50, 10, 20, 30, 5)
        self.assertEqual(result1, 30)
    
    def testBasicOp1(self):
        # testing basic operation
        result = backSearchContinuityWithinRange(data, 50, 10, 0, 100, 5)
        self.assertEqual(result, 50)
    
    def testBasicOp2(self):
        # testing basic operation
        result = backSearchContinuityWithinRange(data, 50, 10, 8, 15, 5)
        self.assertEqual(result, 15)

    def testTooSmall(self):
        # testing a failure case
        result2 = backSearchContinuityWithinRange(data, 1, 0, -1, 1000, 5)
        self.assertEqual(result2, errd.ERROR_TOO_SMALL)

    def testNoData(self):
        # testing another failure case
        result3 = backSearchContinuityWithinRange(None, 100, 0, 20, 100, 3)
        self.assertEqual(result3, errd.ERROR_NO_DATA)

    def testNotFindingAnswerUsual(self):
        # testing case of not finding answer
        result4 = backSearchContinuityWithinRange(data, 70, 10, 68, 72, 10)
        self.assertEqual(result4, errd.ERROR_NOT_FOUND)

    def testNotFindingAnswerUsual1(self):
        # another test case of not finding answer
        result5 = backSearchContinuityWithinRange(data, 50, 20, 60, 80, 5)
        self.assertEqual(result5, errd.ERROR_NOT_FOUND)

    def testEdgeCaseAnswer(self):
        # testing edge case with an answer
        result6 = backSearchContinuityWithinRange(data, 4, 0, -1, 100, 5)
        self.assertEqual(result6, 4)

    def testEdgeCaseNotEnough(self):
        # testing failure edge case
        result8 = backSearchContinuityWithinRange(data, 50, 1, -10, 2, 5)
        self.assertEqual(result8, errd.ERROR_OUT_OF_BOUNDS)

if __name__ == '__main__':
    unittest.main()