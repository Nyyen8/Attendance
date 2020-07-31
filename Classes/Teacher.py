"""
Program: Teacher.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define teacher class.
"""

from Classes.Person import Person
from Validation import Utilities as util

class Teacher(Person):
    '''Teacher class constructor'''
    def __init__(self, fName, lName, tchID, tchPIN):
        '''Teacher object, required:
        # last name, required: string
        # first name, required: string
        # tchID, required: 10 digit number
        # tchPIN, required: 4 digit number'''
        if util.valid_name_check(lName):
            if util.valid_name_check(fName):
                if util.valid_id_check(tchID):
                    if util.valid_pin_check(tchPIN):
                        super().__init__(lName, fName)
                        self._tchID = tchID
                        self._tchPIN = tchPIN
                    else:
                        raise ValueError('Bad attribute input: ' + str(tchPIN))
                else:
                    raise ValueError('Bad attribute input: ' + str(tchID))
            else:
                raise ValueError('Bad attribute input: ' + str(fName))
        else:
            raise ValueError('Bad attribute input: ' + str(lName))


    '''Functions to change individual characteristics of an teacher object'''
    def set_tchID(self, tchID):
        self._tchID = tchID

    def set_tchPIN(self, tchPIN):
        self._tchPIN = tchPIN

    '''Function to create output string based off an teacher class'''
    def display(self):
        return (str(self._fName) + '\n' +
                str(self._lName) + '\n' +
                str(self._tchID) + '\n' +
                str(self._tchPIN))

if __name__ == '__main__':
    pass