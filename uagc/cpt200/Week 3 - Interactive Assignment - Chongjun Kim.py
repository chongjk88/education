'''
CPT200 - Week 3 - Interactive Assignment
Author: Chongjun Kim
Date: 09/02/2021
Title: Countdown and Factorial
'''
from tkinter import *
from tkinter import messagebox
import time # imported time module for countdown

# creating a custom form window
root = Tk()
root.title("Countdown and Factorial")
root.geometry("200x100")

# generic function for alerts
def alert(m):
    return messagebox.showinfo(parent = root, title = 'message', message = m)

# generic validation for checking integer & number greater than 1
def checkInteger(num):
    while True:
        try:
            n = int(num)
            if n > 1:
                return n
            else:
                numberInput.focus_set()
                alert("Please enter a number greater than 1.")
                break
        except ValueError:
            numberInput.focus_set()
            alert("Please enter a number.")
            break

def countdownHandler():
    num = numberInput.get()
    if checkInteger(num):
        n = int(num)
        
        while n > -1:
            print(n)
            time.sleep(1) # delays print in real-time seconds
            n = n - 1
            
        print("Finished countdown.")

def factorialHandler():
    num = numberInput.get()
    if checkInteger(num):
        n = int(num)
        factorial = 1
        
        while n >= 1:
            factorial = factorial * n
            n = n - 1
            
        print("Factorial of " + str(numberInput.get()) + " is:",factorial)

# field labels
numberLabel = Label(root, text = "Enter a number (greater than 1)")
numberLabel.pack(padx=10, pady=10)

# field entry data
numberInput = Entry(root)
numberInput.pack()
numberInput.focus_set() # focus on field as soon as form opens

# buttons
countdownButton = Button(root, text="Countdown", command=countdownHandler).pack(side=LEFT, padx=10, pady=10)
factorialButton = Button(root, text="Factorial", command=factorialHandler).pack(side=RIGHT, padx=10, pady=10)

root.mainloop() # ending program
