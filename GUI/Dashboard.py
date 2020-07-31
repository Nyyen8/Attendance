"""
Program: Dashboard.py
Author: Paul Elsea
Last Modified: 07/31/2020

Program to display GUI for an initial dashboard window.
"""
from tkinter import *
from tkinter import messagebox as mb
from Data import CSVFunctions as csv

'''Creating class dictionaries for future use'''
mathClassDict = csv.build_attendance_dictionary\
    (r'C:\Users\15712\PycharmProjects\Attendance\Data\MathClassStudentList.csv')
sciClassDict = csv.build_attendance_dictionary\
    (r'C:\Users\15712\PycharmProjects\Attendance\Data\ScienceClassStudentList.csv')
teacherDict = csv.build_teacher_dictionary\
    (r'C:\Users\15712\PycharmProjects\Attendance\Data\TeacherList.csv')


'''Sets science check box as unchecked when math check box is selected'''
def math_checked():
    sciChoice.set(0)

'''Sets math check box as unchecked when science check box is selected'''
def sci_checked():
    mathChoice.set(0)


'''Defining sign-in window and child functions'''
def create_sign_in_window():
    try:
        math = mathChoice.get()
        sci = sciChoice.get()

        def sign_in():
            if math == 1 and sci == 0:
                mb.showinfo(title='', message=str(csv.confirm_attendance(mathClassDict, mathID.get())))
                MathSignGUI.destroy()
                AttendanceGUI.deiconify()
                mathChoice.set(0)
                sciChoice.set(0)

            elif math == 0 and sci == 1:
                mb.showinfo(title='', message=str(csv.confirm_attendance(sciClassDict, sciID.get())))
                SciSignGUI.destroy()
                AttendanceGUI.deiconify()
                mathChoice.set(0)
                sciChoice.set(0)

            else:
                raise Exception('Sign in failed due to incorrect class selection values.')

        if math == 0 and sci == 0:
            mb.showinfo(title='No class selected.', message='Please select a class.')

        elif math == 1 and sci == 0:
            MathSignGUI = Toplevel(AttendanceGUI)
            MathSignGUI.title('Math Sign-in')
            MathSignGUI.geometry("230x90")
            AttendanceGUI.withdraw()

            def math_exit_back():
                AttendanceGUI.deiconify()
                MathSignGUI.destroy()

            '''Defining input prompt labels'''
            promptLabel = Label(MathSignGUI, text="Enter student ID")
            promptLabel.configure(font=('Courier', 16, 'bold'))
            promptLabel.grid(column=0, row=0, columnspan=2)

            idLabel = Label(MathSignGUI, text="  ID")
            idLabel.configure(font=("Courier", 12))
            idLabel.grid(column=0, row=1)

            '''Defining input variables and their text boxes'''
            mathID = StringVar()
            idEntered = Entry(MathSignGUI, width=20, textvariable=mathID)
            idEntered.grid(column=1, row=1)

            '''Defining button to call sign in function'''
            signInButton = Button(MathSignGUI, text='Sign In', width=15, command=sign_in). \
                grid(row=2, column=0)

            '''Defining button to exit program'''
            exitButton = Button(MathSignGUI, text='Exit', width=15, command=math_exit_back).grid(row=2, column=1)

        elif math == 0 and sci == 1:
            SciSignGUI = Toplevel(AttendanceGUI)
            SciSignGUI.title('Science Sign-in')
            SciSignGUI.geometry("230x90")
            AttendanceGUI.withdraw()

            def sci_exit_back():
                AttendanceGUI.deiconify()
                SciSignGUI.destroy()

            '''Defining input prompt labels'''
            promptLabel = Label(SciSignGUI, text="Enter student ID")
            promptLabel.configure(font=('Courier', 16, 'bold'))
            promptLabel.grid(column=0, row=0, columnspan=2)

            idLabel = Label(SciSignGUI, text="  ID")
            idLabel.configure(font=("Courier", 12))
            idLabel.grid(column=0, row=1)

            '''Defining input variables and their text boxes'''
            sciID = StringVar()
            idEntered = Entry(SciSignGUI, width=20, textvariable=sciID)
            idEntered.grid(column=1, row=1)

            '''Defining button to call sign in function'''
            signInButton = Button(SciSignGUI, text='Sign In', width=15, command=sign_in). \
                grid(row=2, column=0)

            '''Defining button to exit program'''
            exitButton = Button(SciSignGUI, text='Exit', width=15, command=sci_exit_back).grid(row=2, column=1)

        else:
            raise Exception('Sign in window failed to load due to incorrect class selection values.')
    except:
        raise Exception('create_sign_in_window failed')

'''Defining teacher window and child functions'''
def create_teacher_window():
    try:
        TeacherGUI = Toplevel(AttendanceGUI)
        TeacherGUI.title('Teacher Dashboard')
        TeacherGUI.geometry("230x120")
        AttendanceGUI.withdraw()

        '''Sets science check box as unchecked when math check box is selected'''
        def math_teach_checked():
            sciTeachChoice.set(0)

        '''Sets math check box as unchecked when science check box is selected'''
        def sci_teach_checked():
            mathTeachChoice.set(0)

        '''Calls return_attendance_results with relevant dictionary and displays results in message box.'''
        def show_attendance():
            try:
                math = mathTeachChoice.get()
                sci = sciTeachChoice.get()

                if math == 1 and sci == 0:
                    mb.showinfo(title='Attendance', message=("\n".join(csv.return_attendance_results(mathClassDict))))
                elif math == 0 and sci == 1:
                    mb.showinfo(title='Attendance', message=("\n".join(csv.return_attendance_results(sciClassDict))))
                else:
                    mb.showinfo(title='No class selected.', message='Please select a class.')
            except:
                raise Exception('show_attendance failed')

        '''Calls write_to_file with relevant class and dictionary object'''
        def save_attendance():
            try:
                math = mathTeachChoice.get()
                sci = sciTeachChoice.get()

                if math == 1 and sci == 0:
                    csv.write_to_file(mathClassDict, 'Math')
                    mb.showinfo(title='Save complete', message='Attendance report saved')
                elif math == 0 and sci == 1:
                    csv.write_to_file(sciClassDict, 'Science')
                    mb.showinfo(title='Save complete', message='Attendance report saved')
                else:
                    mb.showinfo(title='No class selected.', message='Please select a class.')
            except:
                raise Exception('save_attendance failed')

        '''Reveals main window and destroys teacher window'''
        def teacher_exit_back():
            try:
                AttendanceGUI.deiconify()
                TeacherGUI.destroy()
            except:
                raise Exception('teacher_exit_back failed')

        '''Check box variables'''
        mathTeachChoice = IntVar()
        sciTeachChoice = IntVar()

        mathLabel = Label(TeacherGUI, text="Math")
        mathLabel.configure(font=("Courier", 13))
        mathLabel.grid(column=0, row=1)

        sciLabel = Label(TeacherGUI, text="Science")
        sciLabel.configure(font=("Courier", 13))
        sciLabel.grid(column=1, row=1)

        '''Defining each check box and associated functions'''
        mathCheck = Checkbutton(TeacherGUI, variable=mathTeachChoice, command=math_teach_checked).grid(row=2, column=0)

        sciCheck = Checkbutton(TeacherGUI, variable=sciTeachChoice, command=sci_teach_checked).grid(row=2, column=1)

        '''Defining button to call show_attendance function'''
        showButton = Button(TeacherGUI, text='View Attendance', width=15, command=show_attendance). \
            grid(row=3, column=0)

        '''Defining button to call save_attendance function'''
        saveButton = Button(TeacherGUI, text='Save Attendance', width=15, command=save_attendance). \
            grid(row=3, column=1)

        '''Defining button to exit window'''
        exitButton = Button(TeacherGUI, text='Exit', width=15, command=teacher_exit_back).grid(row=4, columnspan=2)
    except:
        raise Exception('create_teacher_window failed')

'''Defining PIN window and child functions'''
def create_PIN_window():
    try:
        PinGUI = Toplevel(AttendanceGUI)
        PinGUI.title('Teacher Sign-in')
        PinGUI.geometry("320x120")

        '''Tries to open teacher window if valid credentials supplied, or message box with error if not.'''
        def pin_check():
            try:
                if csv.confirm_PIN(teacherDict, id.get(), pin.get()):
                    create_teacher_window()
                    AttendanceGUI.withdraw()
                    PinGUI.destroy()
                else:
                    mb.showinfo(title='Invalid info.', message='Teacher info not found. Please check and re-enter.')
            except:
                raise Exception('pin_check failed')

        '''Reveals main window and exits pin window'''
        def pin_exit_back():
            try:
                AttendanceGUI.deiconify()
                PinGUI.destroy()
            except:
                raise Exception('pin_exit_back failed')

        '''Defining input prompt labels'''
        promptLabel = Label(PinGUI, text="Enter Teacher ID and PIN")
        promptLabel.configure(font=('Courier', 16, 'bold'))
        promptLabel.grid(column=0, row=0, columnspan=2)

        pinLabel = Label(PinGUI, text="  PIN")
        pinLabel.configure(font=("Courier", 12))
        pinLabel.grid(column=0, row=2)

        idLabel = Label(PinGUI, text="  ID")
        idLabel.configure(font=("Courier", 12))
        idLabel.grid(column=0, row=1)

        '''Defining input variables and their text boxes'''
        pin = StringVar()
        pinEntered = Entry(PinGUI, width=20, textvariable=pin)
        pinEntered.grid(column=1, row=2)

        '''Defining input variables and their text boxes'''
        id = StringVar()
        idEntered = Entry(PinGUI, width=20, textvariable=id)
        idEntered.grid(column=1, row=1)

        '''Defining button to call pin_check function'''
        pinButton = Button(PinGUI, text='Sign In', width=15, command=pin_check). \
            grid(row=3, column=0)

        '''Defining button to exit program'''
        exitButton = Button(PinGUI, text='Exit', width=15, command=pin_exit_back).grid(row=3, column=1)
    except:
        raise Exception('create_pin_window failed')


'''main gui object'''
AttendanceGUI = Tk()
AttendanceGUI.title('Sign In')

'''Check box variables'''
mathChoice = IntVar()
sciChoice = IntVar()

'''Defining input prompt labels'''
classPromptLabel = Label(AttendanceGUI, text="Students")
classPromptLabel.configure(font=("Courier", 16, 'bold'))
classPromptLabel.grid(column=0, row=0, columnspan=2)

'''Defining input prompt labels'''
classPromptLabel = Label(AttendanceGUI, text="Please choose a class")
classPromptLabel.configure(font=("Courier", 14, 'bold'))
classPromptLabel.grid(column=0, row=1, columnspan=2)

mathLabel = Label(AttendanceGUI, text="Math")
mathLabel.configure(font=("Courier", 13))
mathLabel.grid(column=0, row=2)

sciLabel = Label(AttendanceGUI, text="Science")
sciLabel.configure(font=("Courier", 13))
sciLabel.grid(column=1, row=2)

'''Defining each check box and associated functions'''
mathCheck = Checkbutton(AttendanceGUI, variable=mathChoice, command=math_checked).grid(row=3, column=0)

sciCheck = Checkbutton(AttendanceGUI, variable=sciChoice, command=sci_checked).grid(row=3, column=1)

'''Defining button to open sign in window'''
signInButton = Button(AttendanceGUI, text='Sign-In', width=15, command=create_sign_in_window).grid(row=4, columnspan=2)

'''Defining spacer'''
promptLabel = Label(AttendanceGUI, text="--------------------")
promptLabel.configure(font=('Courier', 16, 'bold'))
promptLabel.grid(column=0, row=5, columnspan=2)

'''Defining teacher sign in prompt'''
promptLabel = Label(AttendanceGUI, text="Teacher Sign In")
promptLabel.configure(font=('Courier', 16, 'bold'))
promptLabel.grid(column=0, row=6, columnspan=2)

'''Defining button to call create_PIN_window() function'''
pinButton = Button(AttendanceGUI, text='Sign In', width=15, command=create_PIN_window). \
    grid(row=7, column=0, columnspan=2)

'''Defining spacer'''
promptLabel = Label(AttendanceGUI, text="--------------------")
promptLabel.configure(font=('Courier', 16, 'bold'))
promptLabel.grid(column=0, row=8, columnspan=2)

'''Defining button to exit program'''
exitButton = Button(AttendanceGUI, text='Exit', width=15, command=AttendanceGUI.destroy).grid(row=9, columnspan=2)

'''Defining spacer'''
promptLabel = Label(AttendanceGUI, text="")
promptLabel.configure(font=('Courier', 16, 'bold'))
promptLabel.grid(column=0, row=10, columnspan=2)


'''Loop to wait for input'''
AttendanceGUI.mainloop()

