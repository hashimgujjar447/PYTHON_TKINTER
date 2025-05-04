from tkinter import *
from tkinter import ttk

window=Tk()

window.title("Label")

text=Text(window,font=(30))
text.place(x=10,y=10,height=400,width=400)

scollbar=Scrollbar(window,orient="vertical",command=text.yview)


scollbar.place(x=410,y=10,height=400,width=20)


text["yscrollcommand"]=scollbar.set






window.mainloop()