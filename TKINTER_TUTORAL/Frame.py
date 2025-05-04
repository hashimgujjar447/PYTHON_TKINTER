from tkinter import *
from tkinter import ttk

win=Tk()

win.title("Frame")


frame1=Frame(win,bd=4,bg="lightblue",relief=SUNKEN)
frame1.place(x=0,y=0,width=500,height=500)



labe1=Label(frame1,text="Frame 1",bg="lightblue",font=("Arial",20,"bold"))
labe1.place(x=100,y=200)


frame2=Frame(win,bd=4,bg="lightgreen",relief=SUNKEN)
frame2.place(x=500,y=0,width=500,height=500)




win.mainloop()