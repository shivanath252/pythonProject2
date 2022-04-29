
from tkinter import *
import calendar

def print_calender():
    popup = Tk()
    popup. title("Calender")

    label = Text(popup)
    label. grid(row=1, column=1)

    year = input_.get()
    mycalender = calendar. calendar(int(year))
    label. insert(END, mycalender)


root = Tk()
root.title("Calender")

heading = Label(root, text="CALENDER YEAR", fg = "red", font = ("Times", "50"))
heading.grid(row=1, column = 2)

text = Label(root, text = "Enter Year", font = ("italic", "25"))
text.grid(row=3, column=1)

input_ = Entry(root)
input_.grid(row=3, column=2)

button = Button(root, text = "Submit", padx=10, pady = 10,command = print_calender)
button.grid(row=4, column=2)

root. mainloop()







