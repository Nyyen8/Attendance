"""
Program: CSVFunctions.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to define functions for handling CSV files.
"""

import csv
from datetime import *
from Classes.Student import Student as std
from Classes.Teacher import Teacher as tch

'''build_attendance_dictionary:
param inputCSV: csv file to be read from, required
Returns: Dictionary based on inputCSV'''
def build_attendance_dictionary(inputCSV):
    try:
        with open(inputCSV) as classCSVFile:
            csv_reader = csv.reader(classCSVFile, delimiter=',')
            line_count = 0
            classDict = {}
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                elif row[0] == '':
                    continue
                classDict[str(row[0])] = std(row[1], row[2], row[0], row[3])
        return classDict
    except:
        raise Exception('build_attendance_dictionary failed')

'''build_teacher_dictionary:
param inputCSV: csv file to be read from, required
Returns: Dictionary based on inputCSV'''
def build_teacher_dictionary(inputCSV):
    try:
        with open(inputCSV) as classCSVFile:
            csv_reader = csv.reader(classCSVFile, delimiter=',')
            line_count = 0
            teacherDict = {}
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                elif row[0] == '':
                    continue
                teacherDict[str(row[0])] = tch(row[1], row[2], row[0], row[3])
        return teacherDict
    except:
        raise Exception('build_teacher_dictionary failed')

'''return_attendance_results:
param inputDict: dictionary variable to be read from, required
Returns: String of resulting attendance sheet results'''
def return_attendance_results(inputDict):
    try:
        resultsList = []
        for student in inputDict:
            if inputDict[student]._attend == 'Y':
                resultsList.append(inputDict[student]._fName + ' ' + inputDict[student]._lName + ' attended.')
            else:
                resultsList.append(inputDict[student]._fName + ' ' + inputDict[student]._lName + ' was absent.')
        return resultsList
    except:
        raise Exception('return_attendance_results failed')

'''confirm_attendance:
param inputDict: dictionary variable to be read from, required
param stdID: id variable to be read from, required
Returns: modified dictionary with input student marked as signed in, or not, and return message'''
def confirm_attendance(inputDict, stdID):
    try:
        if stdID in inputDict:
            if inputDict[stdID]._attend == 'N':
                inputDict[stdID].set_attend()
                return 'Sign in completed.'
            else:
                return 'Already signed in.'
        else:
            return 'Student ID not found.'
    except:
        raise Exception('confirm_attendance failed')

'''confirm_PIN:
param inputDict: dictionary variable to be read from, required
param id: dictionary variable to be read from, required
param pin: PIN variable to be read from, required
Returns: Bool based on if pin is present with relevant teacher in dictionary'''
def confirm_PIN(inputDict, id, pin):
    try:
        if id in inputDict:
            if inputDict[id]._tchPIN == str(pin):
                return True
            else:
                return False
        else:
            return False
    except:
        raise Exception('confirm_PIN failed')

'''Creates a new text file, names it based on the current date and string input, then writes dictionary contents to it
and saves it.
:writeDoc: The file being opened and written to
:param inputDict: The input dictionary to read from
:param classChoice: The class selected that will be used to name the output file
:returns: Nothing.'''
def write_to_file(inputDict, classChoice):
    try:
        date.today()
        reportName = classChoice + ' Attendance - ' + str(date.today())
        with open(str(reportName), 'w') as writeDoc:
            writeDoc.write(classChoice + ' Attendance - ' + str(date.today()) + '\n')
            attendance = return_attendance_results(inputDict)
            for student in attendance:
                writeDoc.write(str(student)+'\n')
        writeDoc.close()
    except:
        raise Exception('write_to_file failed')

if __name__ == '__main__':
    pass