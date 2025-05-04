from tkinter import *

win = Tk()
win.geometry("400x300")


entry=input("Enter your name:")
print(entry)

var=StringVar()

lab = Label(
   
    font=("Arial", 20, "bold"),
    bg="gray",
    relief="sunken",
    justify=LEFT,
    width=20,
    textvariable=var,
    underline=1,
  
)

var.set(entry)

lab.place(x=50, y=100)

win.mainloop()
