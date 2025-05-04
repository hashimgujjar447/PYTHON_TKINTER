from tkinter import *

win=Tk()


def top():
    tp=Toplevel(win)
    tp.title("Top Level Window")
    tp.config(bg="lightblue")
    label=Label(tp,text="This is a Top Level Window",bg="lightblue")
    label.place(x=20,y=20,width=200,height=50)
    tp.mainloop()
    


button=Button(win,text="Open",command=top)

button.place(x=20,y=20,width=100,height=50)



win.mainloop()