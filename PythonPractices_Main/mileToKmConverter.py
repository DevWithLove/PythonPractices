from tkinter import *

windows = Tk()
windows.title("Mile to km Converter")
windows.minsize(width=500, height=200)
windows.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

milesLabel = Label(text="Miles")
milesLabel.grid(column=2, row=0)

isEqualToLabel = Label(text="is equal to")
isEqualToLabel.grid(column=0, row=1)

kmValueLabel = Label(text="0")
kmValueLabel.grid(column=1, row=1)

kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)

def button_clicked():
    miles = float(entry.get())
    km = miles * 1.609
    kmValueLabel.config(text=f"{km}")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

windows.mainloop()