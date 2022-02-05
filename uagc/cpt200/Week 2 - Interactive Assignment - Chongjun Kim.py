'''
CPT200 - Week 2 - Interactive Assignment
Author: Chongjun Kim
Date: 08/27/2021
Title: Color Mixer
'''
from tkinter import *
from tkinter import messagebox

# creating a custom form window
root = Tk()
root.title("Color Mixer")
root.resizable(0, 0) # preventing window size adjustment
root.columnconfigure(0, weight=1) # setting first column's width to be 1/3
root.columnconfigure(1, weight=3) # setting second column's width to be 2/3

# form header
heading = Label(root, text="Primary Colors: Red, Blue, Yellow").grid(sticky = N, padx = 5, pady = 5, columnspan = 2)

#submit function with validation (all fields being required)
def submitValue():
    primaryColor = ['red', 'blue', 'yellow']

    if not firstColor.get() or firstColor.get().lower() not in primaryColor:
        warning = 'Please enter a valid primary color.'
        firstColor.focus_set() # moves focus to the field that needs modification
        print(warning)
        return messagebox.showinfo('message', warning)

    if not secondColor.get() or secondColor.get().lower() not in primaryColor:
        warning = 'Please enter a valid primary color.'
        secondColor.focus_set()
        print(warning)
        return messagebox.showinfo('message', warning)
    
    # lowercase field input variables
    color1 = firstColor.get().lower()
    color2 = secondColor.get().lower()

    # combination rules
    if (color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red'):
        result = 'purple'
    elif (color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red'):
        result = 'orange'
    elif (color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue'):
        result = 'green'
    elif (color1 == color2): # make sure the colors are different
        warning = 'Please enter different colors.'
        print(warning)
        return messagebox.showinfo('message', warning)

    # generating result message
    message = 'The combination of ' + color1 + ' and ' + color2 + ' results in ' + result + '!'
    print(message)
    return messagebox.showinfo('message', message)

# field labels
a = Label(root ,text = "First Color").grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)
b = Label(root ,text = "Second Color").grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

# field entry data
firstColor = Entry(root)
secondColor = Entry(root)

# field entry grid
firstColor.grid(row = 1, column = 1, sticky = E, padx = 5, pady = 5)
secondColor.grid(row = 2, column = 1, sticky = E, padx = 5, pady = 5)

Button(root, text="Submit", command=submitValue).grid(row = 6, column = 1, sticky = E, padx = 5, pady = 5)

root.mainloop() # ending program
