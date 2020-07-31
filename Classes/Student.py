"""
Program: Student.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define student class.
"""

from Classes.Person import Person
from Validation import Utilities as util

class Student(Person):
    '''Student class constructor'''
    def __init__(self, lName, fName, stdID, attend='Y'):
        '''Student object, required:
        # last name, required: string
        # first name, required: string
        # stdID, required: 10 digit number
        # attend, optional: char Y or N'''
        if util.valid_name_check(lName):
            if util.valid_name_check(fName):
                if util.valid_id_check(stdID):
                    if util.attended_check(attend):
                        super().__init__(lName, fName)
                        self._stdID = stdID
                        self._attend = attend
                    else:
                        raise ValueError('Bad attribute input: ' + str(attend))
                else:
                    raise ValueError('Bad attribute input: ' + str(stdID))
            else:
                raise ValueError('Bad attribute input: ' + str(fName))
        else:
            raise ValueError('Bad attribute input: ' + str(lName))


    '''Functions to change individual characteristic of an student object'''
    def set_stdID(self, stdID):
        self._stdID = stdID

    def set_attend(self, attend='Y'):
        self._attend = attend


    '''Function to create output string based off an student class'''
    def display(self):
        return (str(self._fName) + '\n' +
                str(self._lName) + '\n' +
                str(self._stdID) + '\n' +
                str(self._attend))


if __name__ == '__main__':
    pass