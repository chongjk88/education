'''
CPT200 - Week 1 - Assignment
Author: Chongjun Kim
Date: 08/23/2021
Title: Employee Management System – Functionality 1
'''
from tkinter import *
from tkinter import messagebox
import re

# creating a custom form window
root = Tk()
root.title("Employee Management System")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# form header
heading = Label(root, text="Functionality 1").grid(sticky = N, padx = 5, pady = 5, columnspan = 2)

# formatting fields
def ssnFormat(num):
    return num[:3]+"-"+num[3:5]+"-"+num[5:]
    
def phoneFormat(num):
    return "("+num[:3]+")"+num[3:6]+"-"+num[6:]

#submit function with validation (all fields being required)
def submitValue():
    if not employeeName.get():
        warning = 'Please enter a name.'
        employeeName.focus_set()
        print(warning)
        return messagebox.showinfo('message', warning)

    if not employeeSSN.get() or len(employeeSSN.get()) != 9:
        warning = 'Please enter a valid SSN (9 digits).'
        employeeSSN.focus_set()
        print(warning)
        return messagebox.showinfo('message', warning)
    else:
        try:
            int(employeeSSN.get()) # making sure only numbers get submitted
            employeeSSNFormat = ssnFormat(employeeSSN.get())
        except ValueError:
            employeeSSN.focus_set()
            return messagebox.showinfo('message', 'Please enter only numbers for SSN.')

    if not employeePhone.get() or len(employeePhone.get()) != 10:
        warning = 'Please enter a valid phone number (10 digits).'
        employeePhone.focus_set()
        print(warning)
        return messagebox.showinfo('message', warning)
    else:
        try:
            int(employeePhone.get()) # making sure only numbers get submitted
            employeePhoneFormat = phoneFormat(employeePhone.get())
        except ValueError:
            employeePhone.focus_set()
            return messagebox.showinfo('message', 'Please enter only numbers for phone number.')

    if not employeeEmail.get() or not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', employeeEmail.get()):
        warning = 'Please enter a valid email address.'
        employeeEmail.focus_set()
        print(warning)
        return messagebox.showinfo('message', warning)

    if not employeeSalary.get():
        warning = 'Please enter a salary amount.'
        employeeSalary.focus_set()
        print(warning)
        return messagebox.showinfo('message', warning)
    else:
        try:
            float(employeeSalary.get()) # making sure only numbers (allowing decimals) get submitted
            employeeSalaryFormat = "${:,.2f}".format(float(employeeSalary.get()))
        except ValueError:
            employeeSalary.focus_set()
            return messagebox.showinfo('message', 'Please enter only numbers for salary.')

    # generating result
    result = f"""---------------------------- {employeeName.get()} -----------------------------\n
        SSN: {employeeSSNFormat}\n
        Phone: {employeePhoneFormat}\n
        Email: {employeeEmail.get()}\n
        Salary: {employeeSalaryFormat}\n
---------------------------------------------------------------------"""
    print(result)
    return messagebox.showinfo('message', result)

# field labels
a = Label(root ,text = "Name").grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)
b = Label(root ,text = "SSN").grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)
c = Label(root ,text = "Phone").grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)
d = Label(root ,text = "Email").grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)
d = Label(root ,text = "Salary").grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

# field entry data
employeeName = Entry(root)
employeeSSN = Entry(root)
employeePhone = Entry(root)
employeeEmail = Entry(root)
employeeSalary = Entry(root)

# field entry grid
employeeName.grid(row = 1, column = 1, sticky = E, padx = 5, pady = 5)
employeeSSN.grid(row = 2, column = 1, sticky = E, padx = 5, pady = 5)
employeePhone.grid(row = 3, column = 1, sticky = E, padx = 5, pady = 5)
employeeEmail.grid(row = 4, column = 1, sticky = E, padx = 5, pady = 5)
employeeSalary.grid(row = 5, column = 1, sticky = E, padx = 5, pady = 5)

Button(root, text="Submit", command=submitValue).grid(row = 6, column = 1, sticky = E, padx = 5, pady = 5)

root.mainloop()
