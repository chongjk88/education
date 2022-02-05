'''
CPT200 - Week 2 - Assignment
Author: Chongjun Kim
Due Date: 08/30/2021
Title: Employee Management System - Functionality 2
'''
from tkinter import *
from tkinter import messagebox
import re # module used for regex validation

# formatting ssn: ###-##-####
def ssnFormat(num):
    return num[:3]+"-"+num[3:5]+"-"+num[5:]

# formatting phone number: (###)###-####
def phoneFormat(num):
    return "("+num[:3]+")"+num[3:6]+"-"+num[6:]

# pop-up window for when the user clicks on the "Add" button
def addWindow():
    global rootAdd, employeeName, employeeSSN, employeePhone, employeeEmail, employeeSalary # global variables that can be referenced outside the current function
    
    rootAdd = Toplevel() # creating child form in a new window
    rootAdd.grab_set() # prevent any button clicks on main window
    rootAdd.title("Add a new employee")

    # field labels
    employeeNameLabel = Label(rootAdd ,text = "Name").grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)
    employeeSSNLabel = Label(rootAdd ,text = "SSN").grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)
    employeePhoneLabel = Label(rootAdd ,text = "Phone").grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)
    employeeEmailLabel = Label(rootAdd ,text = "Email").grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)
    employeeSalaryLabel = Label(rootAdd ,text = "Salary").grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    # field entry data input fields
    employeeName = Entry(rootAdd)
    employeeSSN = Entry(rootAdd)
    employeePhone = Entry(rootAdd)
    employeeEmail = Entry(rootAdd)
    employeeSalary = Entry(rootAdd)

    # field entry grid UI layout
    employeeName.grid(row = 1, column = 1, sticky = E, padx = 5, pady = 5)
    employeeSSN.grid(row = 2, column = 1, sticky = E, padx = 5, pady = 5)
    employeePhone.grid(row = 3, column = 1, sticky = E, padx = 5, pady = 5)
    employeeEmail.grid(row = 4, column = 1, sticky = E, padx = 5, pady = 5)
    employeeSalary.grid(row = 5, column = 1, sticky = E, padx = 5, pady = 5)

    employeeName.focus_set() # focus on first field when the new window opens
    
    Button(rootAdd, text="Submit", command=add).grid(row = 6, column = 1, sticky = E, padx = 5, pady = 5) # submit button

# function that adds employee data to employeeList variable
def add():
    if not employeeName.get():
        warning = 'Please enter a name.'
        employeeName.focus_set()
        print(warning)
        return messagebox.showinfo(parent = rootAdd, title = 'message', message = warning) # parent = rootAdd allows window focus to stay on rootAdd

    if not employeeSSN.get() or len(employeeSSN.get()) != 9:
        warning = 'Please enter a valid SSN (only 9 digit numbers).'
        employeeSSN.focus_set()
        print(warning)
        return messagebox.showinfo(parent = rootAdd, title = 'message', message = warning)
    else:
        try:
            int(employeeSSN.get()) # making sure only numbers get submitted
            employeeSSNFormat = ssnFormat(employeeSSN.get())
        except ValueError:
            employeeSSN.focus_set()
            return messagebox.showinfo(parent = rootAdd, title = 'message', message = 'Please enter only numbers for SSN.')

    if not employeePhone.get() or len(employeePhone.get()) != 10:
        warning = 'Please enter a valid phone number (only 10 digit numbers).'
        employeePhone.focus_set()
        print(warning)
        return messagebox.showinfo(parent = rootAdd, title = 'message', message = warning)
    else:
        try:
            int(employeePhone.get()) # making sure only numbers get submitted
            employeePhoneFormat = phoneFormat(employeePhone.get())
        except ValueError:
            employeePhone.focus_set()
            return messagebox.showinfo(parent = rootAdd, title = 'message', message = 'Please enter only numbers for phone number.')

    if not employeeEmail.get() or \
        not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', employeeEmail.get()):
        warning = 'Please enter a valid email address.'
        employeeEmail.focus_set()
        print(warning)
        return messagebox.showinfo(parent = rootAdd, title = 'message', message = warning)

    if not employeeSalary.get():
        warning = 'Please enter a salary amount.'
        employeeSalary.focus_set()
        print(warning)
        return messagebox.showinfo(parent = rootAdd, title = 'message', message = warning)
    else:
        try:
            float(employeeSalary.get()) # making sure only numbers (allowing decimals) get submitted
            employeeSalaryFormat = "${:,.2f}".format(float(employeeSalary.get()))
        except ValueError:
            employeeSalary.focus_set()
            return messagebox.showinfo(parent = rootAdd, title = 'message', message = 'Please enter only numbers for salary.')

    # new dictionary for storing employee information data
    employeeInfo = {}
    employeeInfo["Name"] = employeeName.get()
    employeeInfo["SSN"] = employeeSSNFormat
    employeeInfo["Phone"] = employeePhoneFormat
    employeeInfo["Email"] = employeeEmail.get()
    employeeInfo["Salary"] = employeeSalaryFormat
    
    employeeList.append(employeeInfo) # add dictionary to employeeList for print
    employeeListBox.insert("end", employeeName.get()) # add dictionary to Listbox for UI selection
    
    rootAdd.destroy() # close window after submitting information

# function that prints results of selected employees from employeeList
def printIndex():
    if not printInfo.get() or not re.match(r'^\d+(,\d+)*$', printInfo.get()):
        warning = "Please enter an index number divided in commas."
        printInfo.focus_set()
        print(warning)
        return messagebox.showinfo("message", warning)
    else:
        printInfoList = printInfo.get().split(",")
        converted_list = [int(element) for element in printInfoList]

        # loop through the list of employeeList and print the entered index number(s)
        for s in converted_list:
            try:
                selected = employeeList[s]
                result = selected["Name"] + "," + \
                    selected["SSN"] + "," + \
                    selected["Phone"] + "," + \
                    selected["Email"] + "," + \
                    selected["Salary"]
                print(result)
            except IndexError:
                printInfo.focus_set()
                if len(employeeList) == 1:
                    indexErrorMessage = "There is only one employee. Please enter 0."
                elif len(employeeList) > 1:
                    indexErrorMessage = "Please enter numbers between 0-" + str(len(employeeList) - 1) + "."
                else:
                    indexErrorMessage = "Please add at least one employee."
                return messagebox.showinfo("message", indexErrorMessage)

# auto-fills indexes when selecting employee(s) from the Listbox UI
def callback(event):
    global selection
    selection = event.widget.curselection() # get selection from Listbox
    
    converted_list = [str(element) for element in selection]
    joined_string = ",".join(converted_list)
    printInfo.delete(0, 'end') # delete previous entry

    if selection:
        printInfo.insert(0, joined_string)

# creating main window that shows the list and index input field
root = Tk()
root.title("Employee Management System")
root.geometry("250x350")

employeeList = [] # employee list variable

employeeListLabel = Label(root, text = "Employee List:")
employeeListLabel.pack()

employeeListBox = Listbox(root, selectmode = MULTIPLE) # allow multiple selection for future use like edit, delete
employeeListBox.bind("<<ListboxSelect>>", callback)
employeeListBox.pack(padx=10)

button = Button(root, text="Add", command = addWindow)
button.pack(pady=10)

spacing = Label(root, text = "").pack() # separating with list using blank line-break

printInfoLabel = Label(root, text = "Enter Index Number:")
printInfoLabel.pack()
printInfo = Entry(root)
printInfo.pack(padx=10)
printButton = Button(root, text="Print", command = printIndex)
printButton.pack(pady=10)

root.mainloop() # end program
