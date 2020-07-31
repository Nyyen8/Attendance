"""
Program: TeacherClassTests.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define tests for teacher class.
"""


import unittest
from Classes.Teacher import Teacher as tch


class TeacherTestCases(unittest.TestCase):
    '''Method to set up a test object'''
    def setUp(self):
       self.Teacher = tch('Bob', 'Billy', 1234567890, 1234)

    '''Method to delete a test object'''
    def tearDown(self):
       del self.Teacher

    '''Test to ensure attributes are being properly applied'''
    def test_tch_object_created_required_attributes(self):
        self.assertEqual(self.Teacher._lName, 'Bob')
        self.assertEqual(self.Teacher._fName, 'Billy')
        self.assertEqual(self.Teacher._tchID, 1234567890)
        self.assertEqual(self.Teacher._tchPIN, 1234)

    '''Test to ensure ValueError exception is thrown with incorrect lName input'''
    def test_tch_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            test = tch('0000', 'Billy', 1234567890, 1234)

    '''Test to ensure ValueError exception is thrown with incorrect fName input'''
    def test_tch_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            test = tch('Bob', '0000', 1234567890, 1234)

    '''Test to ensure ValueError exception is thrown with incorrect tchID input'''
    def test_tch_object_not_created_error_id(self):
        with self.assertRaises(ValueError):
            test = tch('Bob', 'Billy', 'aaaa', 1234)
        with self.assertRaises(ValueError):
            test = tch('Bob', 'Billy', 123456, 1234)
        with self.assertRaises(ValueError):
            test = tch('Bob', 'Billy', 123456789000, 1234)

    '''Test to ensure ValueError exception is thrown with incorrect tchPIN input'''
    def test_tch_object_not_created_error_pin(self):
        with self.assertRaises(ValueError):
            test = tch('Bob', 'Billy', 1234567890, 'aaaa')
        with self.assertRaises(ValueError):
            test = tch('Bob', 'Billy', 1234567890, 12345)
        with self.assertRaises(ValueError):
            test = tch('Bob', 'Billy', 1234567890, 123)

if __name__ == '__main__':
    unittest.main()
