'''
CPT200 - Week 3 - Assignment
Author: Chongjun Kim
Due Date: 09/06/2021
Title: Employee Management System - Functionality 3
'''
from tkinter import *
from tkinter import messagebox
import re # module used for regex validation

# generic function for alerts on main window
def alert(m):
    print(m)
    return messagebox.showinfo(parent = root, title = 'message', message = m)

# generic function for alerts on add window
def alertAdd(m):
    print(m)
    return messagebox.showinfo(parent = rootAdd, title = 'message', message = m) # parent = rootAdd allows window focus to stay on rootAdd

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
        employeeName.focus_set()
        warning = 'Please enter a name.'
        return alertAdd(warning)

    if not employeeSSN.get() or len(employeeSSN.get()) != 9:
        employeeSSN.focus_set()
        warning = 'Please enter a valid SSN (only 9 digit numbers).'
        return alertAdd(warning)
    else:
        try:
            int(employeeSSN.get()) # making sure only numbers get submitted
            employeeSSNFormat = ssnFormat(employeeSSN.get())
        except ValueError:
            employeeSSN.focus_set()
            warning = 'Please enter only numbers for SSN.'
            return alertAdd(warning)

    if not employeePhone.get() or len(employeePhone.get()) != 10:
        warning = 'Please enter a valid phone number (only 10 digit numbers).'
        employeePhone.focus_set()
        return alertAdd(warning)
    else:
        try:
            int(employeePhone.get()) # making sure only numbers get submitted
            employeePhoneFormat = phoneFormat(employeePhone.get())
        except ValueError:
            employeePhone.focus_set()
            warning = 'Please enter only numbers for phone number.'
            return alertAdd(warning)

    if not employeeEmail.get() or \
        not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', employeeEmail.get()): # utilizes the re module
        warning = 'Please enter a valid email address.'
        employeeEmail.focus_set()
        return alertAdd(warning)

    if not employeeSalary.get():
        warning = 'Please enter a salary amount.'
        employeeSalary.focus_set()
        return alertAdd(warning)
    else:
        try:
            float(employeeSalary.get()) # making sure only numbers (allowing decimals) get submitted
            employeeSalaryFormat = "${:,.2f}".format(float(employeeSalary.get()))
        except ValueError:
            employeeSalary.focus_set()
            warning = 'Please enter only numbers for salary.'
            return alertAdd(warning)
    
    # new dictionary for storing employee information/data
    employeeInfo = {}
    employeeInfo["Name"] = employeeName.get()
    employeeInfo["SSN"] = employeeSSNFormat
    employeeInfo["Phone"] = employeePhoneFormat
    employeeInfo["Email"] = employeeEmail.get()
    employeeInfo["Salary"] = employeeSalaryFormat
    
    employeeList.append(employeeInfo) # add dictionary to employeeList for print
    employeeListBox.insert("end", employeeName.get()) # add dictionary to Listbox for UI selection
    
    updateList() # utilizing new updateList function
    
    rootAdd.destroy() # close window after submitting information

# function that removes employee data
def delete():
    for i in reversed(selection):
        employeeListBox.delete(i)
        employeeList.pop(i)
        
    printInfo.delete(0, 'end') # delete previous entry
    
    updateList()

# generic function updating list on main window
def updateList():
    employeeListNumber.config(text = "There are (" + str(len(employeeList)) + ") employees in the system.")
    
# function that prints results of selected employees from employeeList
def printIndex():
    if not printInfo.get() or not re.match(r'^\d+(,\d+)*$', printInfo.get()):
        printInfo.focus_set()
        warning = "Please enter an index number divided in commas."
        return alert(warning)
    else:
        printInfoList = printInfo.get().split(",")
        converted_list = [int(element) for element in printInfoList]
        
        # loop through the list of employeeList and print the entered index number(s)
        index = 0
        while len(converted_list) > index:
            try:
                selected = employeeList[converted_list[index]]
                result = selected["Name"] + "," + \
                    selected["SSN"] + "," + \
                    selected["Phone"] + "," + \
                    selected["Email"] + "," + \
                    selected["Salary"]
                index += 1
                print(result)
            except IndexError:
                printInfo.focus_set()
                if len(employeeList) == 1:
                    indexErrorMessage = "There is only one employee. Please enter 0."
                elif len(employeeList) > 1:
                    indexErrorMessage = "Please enter numbers between 0-" + str(len(employeeList) - 1) + "."
                else:
                    indexErrorMessage = "Please add at least one employee."
                return alert(indexErrorMessage)

def printAll():
    if len(employeeList) > 0:
        # loop through the entire list of employeeList and print all
        index = 0
        while len(employeeList) > index:
            result = employeeList[index]["Name"] + "," + \
                employeeList[index]["SSN"] + "," + \
                employeeList[index]["Phone"] + "," + \
                employeeList[index]["Email"] + "," + \
                employeeList[index]["Salary"]
            index += 1
            print(result)
    else:
        return alert("Please add at least one employee.")

# auto-fills indexes when selecting employee(s) from the Listbox UI
def callback(event):
    global selection, converted_list
    selection = event.widget.curselection() # get selection from Listbox
    
    converted_list = [str(element) for element in selection]
    joined_string = ",".join(converted_list)
    printInfo.delete(0, 'end') # delete previous entry

    if selection:
        printInfo.insert(0, joined_string)

# creating main window that shows the list and index input field
root = Tk()
root.title("Employee Management System")
root.geometry("250x420")

employeeList = [] # employee list global variable

# Listbox that shows the list of all existing employees
employeeListLabel = Label(root, text = "Employee List:")
employeeListLabel.pack(fill=X, pady=(10, 0))

employeeListBox = Listbox(root, selectmode = MULTIPLE) # allows the widget to select multiple items
employeeListBox.bind("<<ListboxSelect>>", callback)
employeeListBox.pack(padx=10)

spacing = Label(root, text = "\n\n").pack() # separating with list using blank line-break

# add and delete buttons
addButton = Button(root, text="Add", command = addWindow)
addButton.place(x=100, y=200)

deleteButton = Button(root, text="Delete", command = delete)
deleteButton.place(x=140, y=200)

# label that shows the number of existing employees
employeeListNumber = Label(root, text = "There are (" + str(len(employeeList)) + ") employees in the system.")
employeeListNumber.pack()

spacing = Label(root, text = "").pack() # separating with list using blank line-break

# index entry for printing employee information
printInfoLabel = Label(root, text = "Enter Index Number:")
printInfoLabel.pack()

printInfo = Entry(root)
printInfo.pack(padx=10)

printSelectedButton = Button(root, text="Print Selected", command = printIndex) # prints only the ones that are mentioned in the index number field
printSelectedButton.pack(pady=(10, 0))

printAllButton = Button(root, text="Print All", command = printAll) # prints all existing data
printAllButton.pack(pady=(10, 0))

root.mainloop() # end program
