'''
AUTHOR: Braden Shrum

PROJECT NAME: Unit Testing with various addition operations

DESCRIPTION: This program performs unit tests on various addition operations like adding integers and 
             adding fractions and tests the results against expected results
'''

import unittest
from fractions import Fraction # to get the fractions for testing

from my_sum import sum # import the sum() function from the folder "my_sum"


class TestSum(unittest.TestCase): # a class that inherits from unittest.TestCase so that unittest can check for tests across the file
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        # declare the numbers and add them together
        data = [1, 2, 3]
        result = sum(data)

        self.assertEqual(result, 6) # test the result against the expected result: 6

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        # declare the fractions and add them together
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)

        self.assertEqual(result, 1) # test the result against the expected result: 1

if __name__ == '__main__':
    unittest.main() # start unittest's main function