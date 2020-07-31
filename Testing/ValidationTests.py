"""
Program: ValidationTests.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define tests for validation utilities.
"""
import unittest
from Validation import Utilities as util

class ValidationTestCases(unittest.TestCase):
    '''Test to ensure valid_name_check returns proper bool'''
    def test_valid_name_check(self):
        testInputName = 'Tom'
        testInputNum = '10'
        testInputBadChar = '1234'
        self.assertEqual(util.valid_name_check(testInputName), True)
        self.assertEqual(util.valid_name_check(testInputNum), False)
        self.assertEqual(util.valid_name_check(testInputBadChar), False)

    '''Test to ensure valid_id_check returns proper bool'''
    def test_valid_id_check(self):
        testInputName = 'Tom'
        testInputShortNum = '10'
        testInputGoodNum = '1234567890'
        testInputLongNum = '12345678900'
        testInputStringNum = '1234'
        self.assertEqual(util.valid_id_check(testInputName), False)
        self.assertEqual(util.valid_id_check(testInputShortNum), False)
        self.assertEqual(util.valid_id_check(testInputGoodNum), True)
        self.assertEqual(util.valid_id_check(testInputLongNum), False)
        self.assertEqual(util.valid_id_check(testInputStringNum), False)

    '''Test to ensure valid_pin_check returns proper bool'''
    def test_valid_pin_check(self):
        testInputName = 'Tom'
        testInputShortNum = '10'
        testInputGoodNum = '1234'
        testInputLongNum = '12345'
        testInputFloatNum = '1.234'
        self.assertEqual(util.valid_pin_check(testInputName), False)
        self.assertEqual(util.valid_pin_check(testInputShortNum), False)
        self.assertEqual(util.valid_pin_check(testInputGoodNum), True)
        self.assertEqual(util.valid_pin_check(testInputLongNum), False)
        self.assertEqual(util.valid_pin_check(testInputFloatNum), False)

    '''Test to ensure valid_date returns proper bool'''
    def test_valid_date(self):
        testInputDate = '01-01-1000'
        testInputMissingDay = '1-01-1000'
        testInputMissingMon = '01-1-1000'
        testInputMissingYear = '01-01-100'
        testInputDayTooLong = '32-01-1000'
        testInputMonTooLong = '01-13-1000'
        testInputYearTooLong = '01-01-10001'
        testDateBackward = '1000-01-01'
        testDateWritten = '12-Jun-1212'
        self.assertEqual(util.valid_date(testInputDate), True)
        self.assertEqual(util.valid_date(testInputMissingDay), True)
        self.assertEqual(util.valid_date(testInputMissingMon), True)
        self.assertEqual(util.valid_date(testInputMissingYear), False)
        self.assertEqual(util.valid_date(testInputDayTooLong), False)
        self.assertEqual(util.valid_date(testInputMonTooLong), False)
        self.assertEqual(util.valid_date(testInputYearTooLong), False)
        self.assertEqual(util.valid_date(testDateBackward), False)
        self.assertEqual(util.valid_date(testDateWritten), False)

if __name__ == '__main__':
    pass