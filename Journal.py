from tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=300)

pane = Frame(master)

pane.pack(fill = BOTH,
          expand = True)

w.pack()

button1 = Button(pane,
                 text = "Previously written",
                 height = 20,
                 width = 10)

button1.pack(fill = BOTH,
             expand = True)

button2 = Button(pane,
                 text = "Write new Journal")

button2.pack(fill = BOTH,
             expand = True)

mainloop()

