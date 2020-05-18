from tkinter import *
import tkinter as tk

# Main Window
master = Tk()
Canvas(master, width=500, height=250).pack()


def new_window():  # Function called by button 2

    # Creates new window
    window = Tk()
    window.title('New Journal')
    window.geometry('1000x450')

    # Allows for user to insert some text
    entry = tk.Text(window, height=25, width=100)
    entry.pack()

    # Opens a new file and users is allowed to write
    text_entry = open("new_file.txt", 'w')
    text_entry.write(entry.get('1.0', 'end-1c'))

    # Save button for user to save written files
    save = tk.Button(window, text="Save", width=10)
    save.pack()
    text_entry.close()


# Two buttons to either write a new journal or a previous journal
button1 = Button(text="Previously written", width=50).place(relx=0.5, rely=0.7, anchor=CENTER)
button2 = Button(text="Write new Journal", command=new_window, width=50).place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
