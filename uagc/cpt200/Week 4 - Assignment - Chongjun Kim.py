'''
CPT200 - Week 4 - Assignment
Author: Chongjun Kim
Due Date: 09/13/2021
Title: Employee Management System - Functionality 4
'''
from tkinter import *
from tkinter import messagebox
import re # module used for regex validation

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

        employeeName.focus_set() # focus on first field when the new window opens
        
        submitButton = Button(self, text="Submit", command=lambda:self.add(self.save, self.index))
        submitButton.grid(row = 6, column = 1, sticky = E, padx = 5, pady = 5) # submit button

    def run(self):
        self.display_add_gui()

    # function that adds employee data to employeeList variable
    def add(self, save, index):
        
        if not self.employeeNameVar.get():
            employeeName.focus_set()
            warning = 'Please enter a name.'
            return self.alertAdd(warning)

        if not self.employeeSSNVar.get() or len(self.employeeSSNVar.get()) != 9:
            employeeSSN.focus_set()
            warning = 'Please enter a valid SSN (only 9 digit numbers).'
            return self.alertAdd(warning)
        else:
            try:
                int(self.employeeSSNVar.get()) # making sure only numbers get submitted
                employeeSSNFormat = ssnFormat(self.employeeSSNVar.get())
            except ValueError:
                employeeSSN.focus_set()
                warning = 'Please enter only numbers for SSN.'
                return self.alertAdd(warning)

        if not self.employeePhoneVar.get() or len(self.employeePhoneVar.get()) != 10 or not phoneFormat(self.employeePhoneVar.get()):
            warning = 'Please enter a valid phone number (only 10 digit numbers).'
            employeePhone.focus_set()
            return self.alertAdd(warning)
        else:
            try:
                int(self.employeePhoneVar.get()) # making sure only numbers get submitted
                employeePhoneFormat = phoneFormat(self.employeePhoneVar.get())
            except ValueError:
                employeePhone.focus_set()
                warning = 'Please enter only numbers for phone number.'
                return self.alertAdd(warning)

        if not self.employeeEmailVar.get() or \
            not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.employeeEmailVar.get()): # utilizes the re module
            warning = 'Please enter a valid email address.'
            employeeEmail.focus_set()
            return self.alertAdd(warning)

        if not self.employeeSalaryVar.get():
            warning = 'Please enter a salary amount.'
            employeeSalary.focus_set()
            return self.alertAdd(warning)
        else:
            try:
                float(self.employeeSalaryVar.get()) # making sure only numbers (allowing decimals) get submitted
                employeeSalaryFormat = "${:,.2f}".format(float(self.employeeSalaryVar.get()))
            except ValueError:
                employeeSalary.focus_set()
                warning = 'Please enter only numbers for salary.'
                return self.alertAdd(warning)
        
        # new dictionary for storing employee information/data
        employeeInfo = {}
        employeeInfo["Name"] = self.employeeNameVar.get()
        employeeInfo["SSN"] = self.employeeSSNVar.get()
        employeeInfo["Phone"] = employeePhoneFormat
        employeeInfo["Email"] = self.employeeEmailVar.get()
        employeeInfo["Salary"] = employeeSalaryFormat

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

# formatting ssn: ###-##-####
def ssnFormat(num):
    return num[:3]+"-"+num[3:5]+"-"+num[5:]

# formatting phone number: (###)###-####
def phoneFormat(num):
    return "("+num[:3]+")"+num[3:6]+"-"+num[6:]

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
                printFormat(selected["Name"],
                        selected["SSN"],
                        selected["Phone"],
                        selected["Email"],
                        selected["Salary"])
                index += 1
            except IndexError:
                printInfo.focus_set()
                if len(employeeList) == 1:
                    indexErrorMessage = "There is only one employee. Please enter 0."
                elif len(employeeList) > 1:
                    indexErrorMessage = "Please enter numbers between 0-" + str(len(employeeList) - 1) + "."
                else:
                    indexErrorMessage = "Please add at least one employee."
                return alert(indexErrorMessage)

# print all existing employee data
def printAll():
    if len(employeeList) > 0:
        # loop through the entire list of employeeList and print all
        index = 0
        while len(employeeList) > index:
            printFormat(employeeList[index]["Name"],
                        employeeList[index]["SSN"],
                        employeeList[index]["Phone"],
                        employeeList[index]["Email"],
                        employeeList[index]["Salary"])
            index += 1
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

# search function for finding SSN (partial or full) match
def search():
    searchValue = searchInput.get()
    if len(employeeList) > 0:
        index = 0
        while len(employeeList) > index:
            if searchValue in employeeList[index]["SSN"] and searchValue: # find similar match
                printFormat(employeeList[index]["Name"],
                            employeeList[index]["SSN"],
                            employeeList[index]["Phone"],
                            employeeList[index]["Email"],
                            employeeList[index]["Salary"])
            index += 1
    else:
        return alert("Please add at least one employee.")

# generic function for improved print format
def printFormat(name, ssn, phone, email, salary):
    result = f"""---------------------------- {name} -----------------------------\n
        SSN: {ssn}\n
        Phone: {phone}\n
        Email: {email}\n
        Salary: {salary}\n
---------------------------------------------------------------------"""
    return print(result)
    
# creating main window that shows the list and index input field
root = Tk()
root.title("Employee Management System")
root.geometry("250x450")

employeeList = [] # employee list global variable
nameList = []
var = StringVar(value = nameList)

# Listbox that shows the list of all existing employees
employeeListLabel = Label(root, text = "Employee List:")
employeeListLabel.pack(fill=X, pady=(10, 0))

employeeListBox = Listbox(root, listvariable=var, selectmode = MULTIPLE) # allows the widget to select multiple items
employeeListBox.bind("<<ListboxSelect>>", callback)
employeeListBox.pack(padx=10)

spacing = Label(root, text = "\n\n").pack() # separating with list using blank line-break

# add, edit, and delete buttons
addButton = Button(root, text = "Add", command = lambda:addWindow(False, 0))
addButton.place(x=64, y=200)

editButton = Button(root, text = "Edit", command = editWindow)
editButton.place(x=103, y=200)

deleteButton = Button(root, text = "Delete", command = delete)
deleteButton.place(x=140, y=200)

# label that shows the number of existing employees
employeeListNumber = Label(root, text = "There are (" + str(len(employeeList)) + ") employees in the system.")
employeeListNumber.pack()

printAllButton = Button(root, text = "Print All", command = printAll) # prints all existing data
printAllButton.pack(pady=10)

spacing = Label(root, text = "").pack() # separating with list using blank line-break

# index entry for printing employee information
printInfoLabel = Label(root, text = "Enter Index Number:")
printInfoLabel.pack()
printInfoLabelFrame = Frame(root)
printInfoLabelFrame.pack(padx=10)

printInfo = Entry(printInfoLabelFrame)
printInfo.pack(side=LEFT, padx=(0,10))

printSelectedButton = Button(printInfoLabelFrame, text = "Print Selected", command = printIndex) # prints only the ones that are mentioned in the index number field
printSelectedButton.pack(side=LEFT)

# search input field
searchInputLabel = Label(root, text = "Search employee by SSN:")
searchInputLabel.pack(pady=(10,0))
searchInputFrame = Frame(root)
searchInputFrame.pack(padx=10)
searchInput = Entry(searchInputFrame)
searchInput.pack(side=LEFT, padx=(0,10))

# search button
searchButton = Button(searchInputFrame, text = "Search & Print", command = search)
searchButton.pack(side=RIGHT)

root.mainloop() # end program
