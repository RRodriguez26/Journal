from tkinter import *
import tkinter as tk

# Main Window
master = Tk()

Canvas(master, width=500, height=250).pack()


def new_window():  # Function called by button 2

    top_level = Tk()
    top_level.title('New Journal')
    top_level.geometry('1000x300')

    entry = tk.Text(top_level, height=25, width=100)
    entry.pack()

# Two buttons to either write a new journal or a previous journal
button1 = Button(text="Previously written", width=50).place(relx=0.5, rely=0.7, anchor=CENTER)
button2 = Button(text="Write new Journal", command=new_window, width=50).place(relx=0.5, rely=0.5, anchor=CENTER)


mainloop()
