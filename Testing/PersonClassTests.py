"""
Program: PersonClassTests.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define tests for person class.
"""

import unittest
from Classes.Person import Person as per

class PersonTestCases(unittest.TestCase):
    '''Method to set up a test object'''
    def setUp(self):
       self.Person = per('Bob', 'Billy')

    '''Method to delete a test object'''
    def tearDown(self):
       del self.Person

    '''Test to ensure attributes are being properly applied'''
    def test_per_object_created_attributes(self):
        self.assertEqual(self.Person._lName, 'Bob')
        self.assertEqual(self.Person._fName, 'Billy')

    '''Test to ensure ValueError exception is thrown with incorrect lName input'''
    def test_per_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            test = per('0000', 'Billy')

    '''Test to ensure ValueError exception is thrown with incorrect fName input'''
    def test_per_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            test = per('Bob', '0000')


if __name__ == '__main__':
    unittest.main()