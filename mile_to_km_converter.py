#!usr/bin/env python3
"""
This programs takes user input to convert miles to a km.
tkinter package is used for GUI screen
grid() method is used to place the labels in the screen
"""

from tkinter import *

tk = Tk()
label = Label()
button = Button()

# Create screen
tk.title("Miles to Km Converter")
tk.minsize(width=1000, height=500)
tk.config(padx=100, pady=100)

# Take input from user to enter miles
input = Entry(width=20, font="Verdana 20 bold")
input.grid(row=0, column=1)


# Write using label
label1 = Label(text="Miles", font="Verdana 20 bold")
label1.grid(row=0, column=2)
label1.config(padx=100, pady=10)

label2 = Label(text="is equal to", font="Verdana 20 bold")
label2.grid(row=1, column=0)
label2.config(padx=100, pady=10)


label3 = Label(text="0", font="Verdana 20 bold")
label3.grid(row=1, column=1)
label3.config(padx=100, pady=10)

label4 = Label(text="Km", font="Verdana 20 bold")
label4.grid(row=1, column=2)
label4.config(padx=100, pady=10)


# Create button
def clickbutton():
    miles = input.get()
    km = int(miles) * 1.6
    label3.config(text=km)


button = Button(text="Calculate", command=clickbutton, font="Verdana 20 bold")
button.grid(row=2, column=1)
button.config(padx=100, pady=10)

tk.mainloop()
