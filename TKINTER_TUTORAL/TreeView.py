from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Canvas X-Axis Line")

label=Label(win, text="Canvas X-Axis Line", font=("Arial", 20))
label.place(x=10,y=20,height=50,width=300)

tree=ttk.Treeview(win)



tree.insert("",END,text="Python",iid="0")
tree.insert("",END,text="java",iid="1")
tree.insert("",END,text="web",iid="2")


tree.insert("",END,text="ML",iid="3")
tree.insert("",END,text="DATASCIENCE",iid="4")

tree.move(3,0,0)
tree.move(4,0,1)



tree.insert("",END,text="html",iid="5")
tree.insert("",END,text="css",iid="6")

tree.move(5,2,0)
tree.move(6,2,1)


tree.place(x=10,y=90,height=300,width=100)

win.mainloop()