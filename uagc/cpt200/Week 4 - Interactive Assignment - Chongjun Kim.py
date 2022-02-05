'''
CPT200 - Week 4 - Interactive Assignment
Author: Chongjun Kim
Due Date: 09/09/2021
Title: Number Analysis Program
'''
from tkinter import *
from tkinter import messagebox

# generic function for alerts
def alert(m):
    print(m)
    return messagebox.showinfo(parent = root, title = 'message', message = m)

# validate integer
def integerCheck(x):
    try:
        int(x)
        return True
    except ValueError:
        alert("Please enter a number!")
        return False
    
# add number to the number list
def add():
    if integerCheck(numberInput.get()):
        if len(numberList) < 20:
            numberListBox.insert("end", numberInput.get()) # add number to Listbox for UI selection
            numberList.append(int(numberInput.get())) # add number to numberList for print
        
            updateList()
        else:
            alert("You have reached 20 numbers!")

# delete number from the number list
def delete():
    for i in reversed(selection):
        numberListBox.delete(i)
        numberList.pop(i)
        
    updateList()
    
    if len(numberList) == 0:
        deleteButton.config(state="disabled")

# generic function for updating number results and list length
def updateList():
    getLowestNumber()
    getHighestNumber()
    getSumNumber()
    
    numberListLabel.config(text = "Employee List (" + str(len(numberList)) + "/20):") # update list length
    numberInput.delete(0, 'end') # delete previous entry

def getLowestNumber():
    if not len(numberList) == 0:
        lowestNumberResult.config(text = "Lowest Number: " + str(min(numberList)))
    else:
        lowestNumberResult.config(text = "Lowest Number: " + str(0))
        
def getHighestNumber():
    if not len(numberList) == 0:
        highestNumberResult.config(text = "Highest Number: " + str(max(numberList)))
    else:
        highestNumberResult.config(text = "Highest Number: " + str(0))
    
def getSumNumber():
    if not len(numberList) == 0:
        sumNumberResult.config(text = "Sum of all the numbers: " + str(sum(numberList)))
    else:
        sumNumberResult.config(text = "Sum of all the numbers: " + str(0))

# print number based on parameter 't'
def printNumber(t):
    while True:
        if t == "lowest":
            label = "The lowest number is: "
            number = str(min(numberList))
        elif t == "highest":
            label = "The highest number is: "
            number = str(max(numberList))
        elif t == "sum":
            label = "The sum of all numbers is: "
            number = str(sum(numberList))
        print(label + number)
        return False # end while loop

# auto-fills indexes when selecting employee(s) from the Listbox UI
def callback(event):
    global selection
    selection = event.widget.curselection() # get selection from Listbox
    deleteButton.config(state="normal")
        
# creating main window that shows the list and index input field
root = Tk()
root.title("Number Analysis Program")

numberList = [] # global number list variable

# number input field
numberInputLabel = Label(root ,text = "Add a number\n(up to 20 times):")
numberInputLabel.pack()
numberInputFrame = Frame(root)
numberInputFrame.pack(padx=10)
numberInput = Entry(numberInputFrame)
numberInput.pack(side=LEFT, padx=(0,10))

# add button
addButton = Button(numberInputFrame, text="Add", command = add)
addButton.pack(side=RIGHT)

spacing = Label(root, text = "").pack() # line-break

# Listbox that shows the list of all existing numbers
numberListLabel = Label(root, text = "Employee List (" + str(len(numberList)) + "/20):")
numberListLabel.pack()

numberListBoxFrame = Frame(root) # wrapping Listbox in a frame for UI layout
numberListBoxFrame.pack()
numberListBox = Listbox(numberListBoxFrame, selectmode = MULTIPLE) # allows the widget to select multiple items
numberListBox.bind("<<ListboxSelect>>", callback)
numberListBox.pack(side=LEFT, fill=Y)

#adding scrollbar to the Listbox widget
scrollbar = Scrollbar(numberListBoxFrame, orient="vertical")
scrollbar.config(command=numberListBox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
numberListBox.config(yscrollcommand=scrollbar.set)

# delete button (able to delete multiple selections)
deleteButton = Button(root, text="Delete selected", command = delete, state="disabled")
deleteButton.pack()

spacing = Label(root, text = "").pack() # line-break

# label that shows the lowest number & print button
lowestNumberResultFrame = Frame(root)
lowestNumberResultFrame.pack(fill=X, padx=10)
lowestNumberResult = Label(lowestNumberResultFrame, text = "Lowest Number: " + str(0))
lowestNumberResult.pack(side=LEFT, padx=(0,10))
lowestNumberPrint = Button(lowestNumberResultFrame, text="Print", command = lambda:printNumber("lowest")) # utilizing lambda to pass a string parameter
lowestNumberPrint.pack(side=RIGHT)

# label that shows the highest number & print button
highestNumberResultFrame = Frame(root)
highestNumberResultFrame.pack(fill=X, padx=10)
highestNumberResult = Label(highestNumberResultFrame, text = "Highest Number: " + str(0))
highestNumberResult.pack(side=LEFT, padx=(0,10))
highestNumberPrint = Button(highestNumberResultFrame, text="Print", command = lambda:printNumber("highest"))
highestNumberPrint.pack(side=RIGHT)

# label that shows the sum of all numbers & print button
sumNumberResultFrame = Frame(root)
sumNumberResultFrame.pack(fill=X, padx=10)
sumNumberResult = Label(sumNumberResultFrame, text = "Sum of all the numbers: " + str(0))
sumNumberResult.pack(side=LEFT, padx=(0,10))
sumNumberPrint = Button(sumNumberResultFrame, text="Print", command = lambda:printNumber("sum"))
sumNumberPrint.pack(side=RIGHT)

spacing = Label(root, text = "").pack() # line-break

root.mainloop() # ending program
