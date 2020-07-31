"""
Program: Utilities.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program of input validation utilities.
"""

from datetime import datetime as date
import re

'''Function to verify that input is valid name
:param inputString: string to be validated, required
:returns: bool value'''
def valid_name_check(inputString):
    try:
        result = bool(re.fullmatch(r"^[^\W0-9_]+([ :'\-‧][^\W0-9_]+)*?$", inputString))
        return result
    except:
        raise Exception('valid_name_check failed')


'''Function to verify that input is valid date
:param inputDate: string to be validated, required
:returns: bool value'''
def valid_date(inputDate):
        try:
            date.strptime(inputDate, '%d-%m-%Y').date()
            return True
        except ValueError:
            return False


'''Function to verify that input is valid ID
:param inputNum: string to be validated, required
:returns: bool value'''
def valid_id_check(inputNum):
    try:
        result = bool(re.fullmatch("^[0-9]+$", inputNum))
        if result:
            if len(str(inputNum)) == 10:
                return True
            else:
                return False
        else:
            return False
    except:
        raise Exception('valid_id_check failed')


'''Function to verify that input is valid PIN
:param inputNum: string to be validated, required
:returns: bool value'''
def valid_pin_check(inputNum):
    try:
        result = bool(re.fullmatch("^[0-9]+$", inputNum))
        if result:
            if len(str(inputNum)) == 4:
                return True
            else:
                return False
        else:
            return False
    except:
        raise Exception('valid_pin_check failed')


'''Function to verify that input is char
:param inputChar: char to be validated, required
:returns: bool value'''
def attended_check(inputChar):
    try:
        if inputChar == 'Y' or inputChar == 'N':
            return True
        else:
            return False
    except:
        raise Exception('attend_check failed')

if __name__ == '__main__':
    pass