from tkinter import *

win=Tk()

var=BooleanVar()


def check():
    print(var.get())
    bt.config(text="Checked" if var.get() else "Unchecked")


cb=Checkbutton(win,text="Python",font=30,variable=var,command=check)
cb.deselect()
cb.pack()


bt=Button(win,text="Check",font=30, cursor="pirate")
bt.pack()


print(var.get())

win.mainloop()