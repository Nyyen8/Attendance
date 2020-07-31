"""
Program: Student.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define student class.
"""

from Validation import Utilities as util

class Person:
    '''Person class constructor'''
    def __init__(self, lName, fName):
        '''Employee object, required:
        # last name, required: string
        # first name, required: string'''
        if util.valid_name_check(lName):
            if util.valid_name_check(fName):
                self._lName = lName
                self._fName = fName
            else:
                raise ValueError('Bad attribute input: ' + str(fName))
        else:
            raise ValueError('Bad attribute input: ' + str(lName))


    '''Functions to change individual characteristics of an person object'''
    def set_lName(self, lName):
        self._lName = lName

    def set_fName(self, fName):
        self._fName = fName

    '''Function to create output string based off an person class'''
    def display(self):
        return (str(self._fName) + '\n' +
                str(self._lName))


if __name__ == '__main__':
    pass