from tkinter import *

win=Tk()

var=StringVar()

def check():
    lb.config(text="You have selected "+var.get())
    print(var.get())

Lint_1=(("python","p"),("java","j"),("c++","c++"),("c#","c#"))

for i in Lint_1:
    Radio_Button=Radiobutton(win,text=i[0],font=30,value=i[1],variable=var, command=check);  
    Radio_Button.pack(fill="x")  
    





lb=Label(win,text="",font=30,bg="red",fg="white", justify=LEFT,relief="sunken")

lb.pack()


bt=Button(win,text="Ok",font=30, cursor="pirate")
bt.pack()






win.mainloop()

