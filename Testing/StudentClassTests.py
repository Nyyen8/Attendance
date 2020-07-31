"""
Program: StudentClassTests.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define tests for student class.
"""

import unittest
from Classes.Student import Student as std

class StudentTestCases(unittest.TestCase):
    '''Method to set up a test object'''
    def setUp(self):
       self.Student = std('Bob', 'Billy', '1234567890', 'Y')

    '''Method to delete a test object'''
    def tearDown(self):
       del self.Student

    '''Test to ensure attributes are being properly applied'''
    def test_std_object_created_required_attributes(self):
        self.assertEqual(self.Student._lName, 'Bob')
        self.assertEqual(self.Student._fName, 'Billy')
        self.assertEqual(self.Student._stdID, '1234567890')

    '''Test to ensure attributes are being properly applied'''
    def test_std_object_created_all_attributes(self):
        self.assertEqual(self.Student._lName, 'Bob')
        self.assertEqual(self.Student._fName, 'Billy')
        self.assertEqual(self.Student._stdID, '1234567890')
        self.assertEqual(self.Student._attend, 'Y')

    '''Test to ensure ValueError exception is thrown with incorrect lName input'''
    def test_std_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            test = std('0000', 'Billy', 1234567890)

    '''Test to ensure ValueError exception is thrown with incorrect fName input'''
    def test_std_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            test = std('Bob', '0000', '1234567890')

    '''Test to ensure ValueError exception is thrown with incorrect stdID input'''
    def test_std_object_not_created_error_id(self):
        with self.assertRaises(ValueError):
            test = std('Bob', 'Billy', 'aaaa')
        with self.assertRaises(ValueError):
            test = std('Bob', 'Billy', '123456')
        with self.assertRaises(ValueError):
            test = std('Bob', 'Billy', '123456789000')

    '''Test to ensure ValueError exception is thrown with incorrect attend input'''
    def test_std_object_not_created_error_attend(self):
        with self.assertRaises(ValueError):
            test = std('Bob', 'Billy', '1234567890', 'C')
        with self.assertRaises(ValueError):
            test = std('Bob', 'Billy', '1234567890', '1')
        with self.assertRaises(ValueError):
            test = std('Bob', 'Billy', '1234567890', '')


if __name__ == '__main__':
    unittest.main()