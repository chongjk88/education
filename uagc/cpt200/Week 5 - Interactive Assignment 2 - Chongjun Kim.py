'''
CPT200 - Week 5 - Interactive Assignment 2
Author: Chongjun Kim
Due Date: 09/16/2021
Title: Employee Management System - Functionality 5
'''
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename # module that opens file selector
import os

class AddEmployee(Toplevel):
    index = 0

    def __init__(self, master, index, title, save):
        Toplevel.__init__(self, master)
        self.index = index
        self.title(title) #since toplevel widgets define a method called title you can't store it as an attribute
        self.save = save
        self.display_add_gui() #maybe just leave that code part of the __init__?

    def display_add_gui(self):
        global employeeName, employeeSSN, employeePhone, employeeEmail, employeeSalary # global variables that can be referenced outside the current function

        # field labels
        employeeNameLabel = Label(self ,text = "Name").grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)
        employeeSSNLabel = Label(self ,text = "SSN").grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)
        employeePhoneLabel = Label(self ,text = "Phone").grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)
        employeeEmailLabel = Label(self ,text = "Email").grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)
        employeeSalaryLabel = Label(self ,text = "Salary").grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

        # dynamic string variables
        self.employeeNameVar = StringVar()
        self.employeeSSNVar = StringVar()
        self.employeePhoneVar = StringVar()
        self.employeeEmailVar = StringVar()
        self.employeeSalaryVar = StringVar()

        # field entry data input fields
        employeeName = Entry(self, textvariable = self.employeeNameVar)
        employeeSSN = Entry(self, textvariable = self.employeeSSNVar)
        employeePhone = Entry(self, textvariable = self.employeePhoneVar)
        employeeEmail = Entry(self, textvariable = self.employeeEmailVar)
        employeeSalary = Entry(self, textvariable = self.employeeSalaryVar)

        # field entry grid UI layout
        employeeName.grid(row = 1, column = 1, sticky = E, padx = 5, pady = 5)
        employeeSSN.grid(row = 2, column = 1, sticky = E, padx = 5, pady = 5)
        employeePhone.grid(row = 3, column = 1, sticky = E, padx = 5, pady = 5)
        employeeEmail.grid(row = 4, column = 1, sticky = E, padx = 5, pady = 5)
        employeeSalary.grid(row = 5, column = 1, sticky = E, padx = 5, pady = 5)

        #employeeName.focus_set() # focus on first field when the new window opens
        
        submitButton = Button(self, text = "Submit", command = lambda:self.add(self.save, self.index))
        submitButton.grid(row = 6, column = 1, sticky = E, padx = 5, pady = 5) # submit button

    def run(self):
        self.display_add_gui()

    # function that adds employee data to employeeList variable
    def add(self, save, index):
        # new dictionary for storing employee information/data
        employeeInfo = {}
        employeeInfo["Name"] = self.employeeNameVar.get()
        employeeInfo["SSN"] = self.employeeSSNVar.get()
        employeeInfo["Phone"] = self.employeePhoneVar.get()
        employeeInfo["Email"] = self.employeeEmailVar.get()
        employeeInfo["Salary"] = self.employeeSalaryVar.get()

        if save:
            employeeList[index] = employeeInfo
            nameList[index] = employeeInfo["Name"]
        else:
            nameList.append(employeeInfo["Name"])
            employeeList.append(employeeInfo) # add dictionary to employeeList for print

            employeeInfo.update({
                employeeInfo["Name"] : employeeName.get()
            })
        
        updateList() # utilizing new updateList function
        Toplevel.destroy(self) # close window after submitting information
    
    # generic function for alerts on add window
    def alertAdd(self, m):
        print(m)
        return messagebox.showinfo(parent = self, title = 'message', message = m) # parent = rootAdd allows window focus to stay on rootAdd
      
# generic function for alerts on main window
def alert(m):
    print(m)
    return messagebox.showinfo(parent = root, title = 'message', message = m)

# pop-up window for when the user clicks on the "Add" button
def addWindow(save, index):
    rootAdd = AddEmployee(root, index, "Edit", save)
    rootAdd.grab_set() 
    
# pop-up window for when the user clicks on the "Edit" button
def editWindow():
    printInfoList = printInfo.get().split(",")
    converted_list = [int(element) for element in printInfoList]
    
    index = 0
    while len(converted_list) > index:
        addWindow(True, converted_list[index])
        
        selected = employeeList[converted_list[index]]
        employeeName.insert(0, selected["Name"])
        employeeSSN.insert(0, selected["SSN"])
        employeePhone.insert(0, clean(selected["Phone"]))
        employeeEmail.insert(0, selected["Email"])
        employeeSalary.insert(0, clean(selected["Salary"]))

        index += 1

# clean special characters for when editing existing employees
def clean(v):
    cleanNumber = v.replace("(","")
    cleanNumber = cleanNumber.replace(")","")
    cleanNumber = cleanNumber.replace("-","")
    cleanNumber = cleanNumber.replace("$","")
    cleanNumber = cleanNumber.replace(",","")
    cleanNumber = "".join(cleanNumber)
    return cleanNumber

# function that removes employee data
def delete():
    for i in reversed(selection):
        nameList.pop(i)
        employeeList.pop(i)
        
    printInfo.delete(0, 'end') # delete previous entry
    
    updateList()

# generic function updating list on main window
def updateList():
    var.set(nameList)

    # disabling buttons when not active on Listbox
    if len(printInfo.get()) == 0 and not employeeListBox.get(ACTIVE):
        editButton.config(state="disabled")
        deleteButton.config(state="disabled")

# print all existing employee data
def exportFile():
    printContent = ''
    if len(employeeList) > 0:
        # loop through the entire list of employeeList and print all
        index = 0
        while len(employeeList) > index:
            printString = employeeList[index]["Name"] + "," + \
                          employeeList[index]["SSN"] + "," + \
                          employeeList[index]["Phone"] + "," + \
                          employeeList[index]["Email"] + "," + \
                          clean(employeeList[index]["Salary"])
            lineBreak = "\n" # adding line break in a variable since f-string does not accept backslash
            printContent = printContent + f"{lineBreak if printContent != '' else ''}" + printString
            index += 1

        check = os.path.isfile("file.txt")
        with open('file.txt', 'w+') as f:
            if not check:
                f.write(printContent)
            else:
                f.truncate()
                f.write(printContent)
        print('Export complete!')
    else:
        return alert("Please add at least one employee.")

# auto-fills indexes when selecting employee(s) from the Listbox UI
def callback(event):
    global selection, converted_list
    selection = event.widget.curselection() # get selection from Listbox
    editButton.config(state="normal")
    deleteButton.config(state="normal")
    
    converted_list = [str(element) for element in selection]
    joined_string = ",".join(converted_list)
    printInfo.delete(0, 'end') # delete previous entry

    if selection:
        printInfo.insert(0, joined_string)
    if len(printInfo.get()) == 0:
        editButton.config(state="disabled")
        deleteButton.config(state="disabled")

def importFile():
    Tk().withdraw() # opens file selector when program runs
    filename = askopenfilename() # gets file directory and name

    importFile = open (filename) # gets file content
    readFile = importFile.read() # stores content from file
    splitFile = readFile.split("\n")
    
    index = 0
    while len(splitFile) > index:
        splitFileList = splitFile[index].split(",") # generates a list
        
        employeeInfo = {}
        if len(splitFileList) > 0:
            employeeInfo["Name"] = splitFileList[0]
        if len(splitFileList) > 1:
            employeeInfo["SSN"] = splitFileList[1]
        if len(splitFileList) > 2:
            employeeInfo["Phone"] = splitFileList[2]
        if len(splitFileList) > 3:
            employeeInfo["Email"] = splitFileList[3]
        if len(splitFileList) > 4:
            employeeInfo["Salary"] = splitFileList[4]

        nameList.append(splitFileList[0])
        employeeList.append(employeeInfo) # add dictionary to employeeList for print
        index += 1
        
    updateList()
    
# creating main window that shows the list and index input field
root = Tk()
root.title("Employee Management System")
root.geometry("250x300")

employeeList = [] # employee list global variable
nameList = []
var = StringVar(value = nameList)

# Listbox that shows the list of all existing employees
employeeListLabel = Label(root, text = "Employee List:")
employeeListLabel.pack(fill=X, pady=(10, 0))

employeeListBox = Listbox(root, listvariable = var, selectmode = MULTIPLE) # allows the widget to select multiple items
employeeListBox.bind("<<ListboxSelect>>", callback)
employeeListBox.pack(padx=10)

spacing = Label(root, text = "\n\n").pack() # separating with list using blank line-break

# add, edit, and delete buttons
addButton = Button(root, text = "Add", command = lambda:addWindow(False, 0))
addButton.place(x=64, y=200)

editButton = Button(root, text = "Edit", command = editWindow, state="disabled")
editButton.place(x=103, y=200)

deleteButton = Button(root, text = "Delete", command = delete, state="disabled")
deleteButton.place(x=140, y=200)

# index entry for printing employee information
printInfoLabelFrame = Frame(root)
printInfoLabelFrame.pack(padx=10)

printInfo = Entry(printInfoLabelFrame)


# search button
importExportFrame = Frame(root)
importExportFrame.pack(padx=10)

searchButton = Button(importExportFrame, text = "Import", command = importFile)
searchButton.pack(side=LEFT, padx=(0,10))

printAllButton = Button(importExportFrame, text = "Export", command = exportFile) # prints all existing data
printAllButton.pack(side=RIGHT)

root.mainloop() # end program
