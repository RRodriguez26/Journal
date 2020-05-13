from tkinter import *
import tkinter as tk

# Main Window
master = tk.Tk()

Canvas(master, width=1000, height=300).pack()

pane = Frame(master)

pane.pack(fill=NONE, expand=True)

button1 = Button(pane, text="Previously written", width=30).pack(fil=BOTH, expand=True)


def newwindow():

    toplevel = Toplevel()
    toplevel.title('New Journal')
    toplevel.geometry('1000x300')

    label = tk.Label(toplevel, text="New Journal")
    entry = tk.Entry(toplevel)
    label.pack()
    entry.pack()


button2 = Button(pane, text="Write new Journal", command=newwindow).pack(fill=BOTH, expand=True)


mainloop()
