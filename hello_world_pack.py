from tkinter import ttk
from tkinter import *

tk = Tk()
# Creating a label that is printed on the screen.
label = Label(text="Enter Text here", fg="blue",
              bg="yellow",
              font="Verdana 50 bold")
label.pack(side="left")  # ...pack() method will write the content in screen window

# Creating screen title and fixing the size of screen.
tk.title("ScreenTitle")
tk.minsize(width=1000, height=500)

# Take input from the user
input = Entry(width=10)
input.pack(side="left")


# Creating button on the screen
def clickbutton():
    new_text = input.get()
    label.config(text=new_text)


# Creating button on the screen.
# Based on the called function respective change will happen on clicking button.
button = Button(text="Submit", command=clickbutton)
button.pack(side="left")

tk.mainloop()
