from tkinter import *

win=Tk()


list_one=["Python","Java","C++","JavaScript","Ruby"]

p=StringVar(value=list_one)


list_box=Listbox(win,listvariable=p)
list_box.place(x=20,y=20,width=100,height=100)


list_box.bind("<<ListboxSelect>>",lambda event: print(list_box.get(list_box.curselection())))





win.mainloop()