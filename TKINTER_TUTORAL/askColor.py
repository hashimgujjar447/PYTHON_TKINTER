from tkinter import *
from tkinter.colorchooser import askcolor

win=Tk();

def askColor(title="Choose Color"):
    color=askcolor(title=title)
    print(color)
    win.config(bg=color[1])


button=Button(win,text="Click me",command=askColor)
button.place(x=10,y=10,height=50,width=50)

win.mainloop()