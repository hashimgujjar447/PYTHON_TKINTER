from tkinter import *

win = Tk()
win.geometry("300x300")  # Optional: set window size

def show(selected_value):
    lb.config(text=selected_value)

Opt_List = ["c#", "c++", "java", "python", "javascript"]

value = StringVar()
value.set("Select a language")  # default value

op = OptionMenu(win, value, *Opt_List, command=show)
op.place(x=100, y=100, width=100, height=50)

lb = Label(win, text="")
lb.place(x=100, y=200, width=100, height=50)

win.mainloop()
