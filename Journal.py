from tkinter import *
import tkinter as tk

# Main Window
master = tk.Tk()

Canvas(master, width=1000, height=300).pack()

pane = Frame(master)

pane.pack(fill=NONE, expand=True)

button1 = Button(pane, text="Previously written", width=30).pack(fil=BOTH, expand=True)


def new_window():

    top_level = Toplevel()
    top_level.title('New Journal')
    top_level.geometry('1000x300')

    label = tk.Label(top_level, text="New Journal")
    entry = tk.Text(top_level, height=100, width=100)
    label.pack()
    entry.pack()


button2 = Button(pane, text="Write new Journal", command=new_window).pack(fill=BOTH, expand=True)


mainloop()
