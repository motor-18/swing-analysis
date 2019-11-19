"""
Testing the function searchContinuityAboveValueTwoSignals
"""
import unittest

from analysis import searchContinuityAboveValueTwoSignals
from analysis import errorDefinitions

errd = errorDefinitions()

data1 = range(0,100,1)
data2 = range(0,100,1)

class TestFirst(unittest.TestCase):

    def testBasicOp(self):
        # testing basic operation
        result = searchContinuityAboveValueTwoSignals(data1, data2, 10, 50, 15, 30, 5)
        self.assertEqual(result, 30)
    
    def testBasicOp1(self):
        # testing basic operation
        result = searchContinuityAboveValueTwoSignals(data1, data2, 10, 50, 40, 11, 5)
        self.assertEqual(result, 40)

    def testTooSmall(self):
        # testing a failure case
        result = searchContinuityAboveValueTwoSignals(data1, data2, 2, 5, -2, -2, 10)
        self.assertEqual(result, errd.ERROR_TOO_SMALL)

    def testNoData(self):
        # testing another failure case
        result = searchContinuityAboveValueTwoSignals(None, None, 10, 50, 40, 11, 5)
        self.assertEqual(result, errd.ERROR_NO_DATA)
    
    def testNoData1(self):
        # testing another failure case
        result = searchContinuityAboveValueTwoSignals(None, data2, 10, 50, 40, 11, 5)
        self.assertEqual(result, errd.ERROR_NO_DATA)
    
    def testNoData2(self):
        # testing another failure case
        result = searchContinuityAboveValueTwoSignals(data1, None, 10, 50, 40, 11, 5)
        self.assertEqual(result, errd.ERROR_NO_DATA)

    def testNotFindingAnswerUsual(self):
        # testing case of not finding answer
        result = searchContinuityAboveValueTwoSignals(data1, data2, 10, 50, 60, 5, 5)
        self.assertEqual(result, errd.ERROR_NOT_FOUND)
    
    def testNotFindingAnswerUsual1(self):
        # testing case of not finding answer
        result = searchContinuityAboveValueTwoSignals(data1, data2, 10, 50, 5, 60, 5)
        self.assertEqual(result, errd.ERROR_NOT_FOUND)

    def testEdgeCaseAnswer(self):
        # testing edge case with an answer
        result = searchContinuityAboveValueTwoSignals(data1, data2, 0, 4, -1, -2, 5)
        self.assertEqual(result, 0)

    def testEdgeCaseNotFound(self):
        # testing edge case with no answer
        result = searchContinuityAboveValueTwoSignals(data1, data2, 0, 4, 7, 6, 5)
        self.assertEqual(result, errd.ERROR_NOT_FOUND)
    
    def testEdgeCaseNotFound1(self):
        # testing edge case with no answer
        result = searchContinuityAboveValueTwoSignals(data1, data2, 0, 4, -2, 7, 5)
        self.assertEqual(result, errd.ERROR_NOT_FOUND)
    
    def testEdgeCaseNotFound2(self):
        # testing edge case with no answer
        result = searchContinuityAboveValueTwoSignals(data1, data2, 0, 4, 7, -2, 5)
        self.assertEqual(result, errd.ERROR_NOT_FOUND)

    def testEdgeCaseOutOfBounds(self):
        # testing failure edge case
        result8 = searchContinuityAboveValueTwoSignals(data1, data2, 5, 99, 99, 99, 10)
        self.assertEqual(result8, errd.ERROR_OUT_OF_BOUNDS)

if __name__ == '__main__':
    unittest.main()