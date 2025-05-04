from tkinter import *


win=Tk()

win.config(bg="red")




# def convert():
#     lb.config(text="Python is a programming language")



button=Button(win,text="CLick Me" , font=30 ,bg="blue",fg="white",activebackground="red",activeforeground="yellow",cursor="plus",relief="raised",justify=LEFT,command=lambda: lb.config(text="Python is a programming language"))

button.place(x=100,y=100)

lb=Label(win,text="Click to change me",font=30,bg="red",fg="white", justify=LEFT,relief="sunken")
lb.place(x=100,y=200)



win.mainloop()  