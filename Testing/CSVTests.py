"""
Program: CSVTests.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to test functions of CSVFunctions.py.
"""

import unittest
from Data import CSVFunctions as csv


class CSVTestCase(unittest.TestCase):
    '''Method to set up a test object'''
    def setUp(self):
       self.testDictionary = csv.build_attendance_dictionary\
           (r'C:\Users\15712\PycharmProjects\Attendance\Data\MathClassStudentList.csv')

    '''Method to delete a test object'''
    def tearDown(self):
       del self.testDictionary

    '''Test to ensure output of return_attendance_results is correct'''
    def test_return_attendance_results(self):
        testDictionary = csv.build_attendance_dictionary\
            (r'C:\Users\15712\PycharmProjects\Attendance\Data\TestStudentList.csv')
        self.assertEqual(csv.return_attendance_results(testDictionary), ['Guy Test was absent.',
                                                                         'Gal Test attended.'])

    '''Test to ensure output of confirm_attendance is correct'''
    def test_confirm_attendance(self):
        testDictionary = csv.build_attendance_dictionary\
            (r'C:\Users\15712\PycharmProjects\Attendance\Data\TestStudentList.csv')
        self.assertEqual(csv.confirm_attendance(testDictionary, '0000000001'), 'Sign in completed.')
        self.assertEqual(csv.confirm_attendance(testDictionary, '1000000000'), 'Already signed in.')
        self.assertEqual(csv.confirm_attendance(testDictionary, '0000000000'), 'Student ID not found.')

    '''Test to ensure output of confirm_pin is correct'''
    def test_confirm_pin(self):
        testDictionary = csv.build_teacher_dictionary\
            (r'C:\Users\15712\PycharmProjects\Attendance\Data\TestTeacherList.csv')
        self.assertEqual(csv.confirm_PIN(testDictionary, '9999999999', '5555'), True)
        self.assertEqual(csv.confirm_PIN(testDictionary, '0000000000', '5555'), False)
        self.assertEqual(csv.confirm_PIN(testDictionary, '9999999999', '0000'), False)


if __name__ == '__main__':
    unittest.main()


