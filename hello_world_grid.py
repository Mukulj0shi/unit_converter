from tkinter import ttk
from tkinter import *

tk = Tk()
# Creating a label that is printed on the screen.
label = Label(text="Enter Text here", fg="blue",
              bg="yellow",
              font="Verdana 20 bold")
label.grid(row=0, column=0)  # ...pack() method will write the content in screen window
label.config(padx=20, pady=20)

# Creating screen title and fixing the size of screen.
tk.title("ScreenTitle")
tk.minsize(width=1000, height=500)
tk.config(padx=100, pady=100)

# Take input from the user
input = Entry(width=10)
input.grid(row=2, column=3)


# Creating button on the screen
def clickbutton():
    new_text = input.get()
    label.config(text=new_text)


# Creating button on the screen.
# Based on the called function respective change will happen on clicking button.
button = Button(text="Submit", command=clickbutton)
button.grid(row=1, column=1)
button.config(padx=10, pady=10)


button = Button(text="New_button", command=clickbutton)
button.grid(row=0, column=2)
button.config(padx=10, pady=10)


tk.mainloop()
