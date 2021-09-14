import unittest
import bubblesort as st
import random

class Test_TestValue(unittest.TestCase):
    def test_simple(self):
        testList = [4,3,2,1]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubbleSort(testList)
        self.assertEqual(actualList, expectedList)

    def test_empty(self):
        testlist = []
        expectedList = testlist.copy()
        expectedList.sort()
        actualList = st.bubbleSort(testlist)
        self.assertEqual(actualList, expectedList)

    def test_presorted(self):
        testList = [1,2,3,4]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubbleSort(testList)
        self.assertEqual(actualList, expectedList)

    def test_negative(self):
        testList = [-4,-3,-2,-1]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubbleSort(testList)
        self.assertEqual(actualList, expectedList)

    def test_random(self):
        testList = [random.randint(0, 20), random.randint(0,20),  random.randint(0,20), random.randint(0,20)]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubbleSort(testList)
        self.assertEqual(actualList, expectedList)