from tkinter import *
from tkinter import ttk

win=Tk()

notebook=ttk.Notebook(win)

notebook.pack(pady=20,expand=True)

frame1=ttk.Frame(notebook,height=500,width=500);
frame2=ttk.Frame(notebook,height=500,width=500);

frame1.pack(fill=BOTH,expand=True)
frame2.pack(fill=BOTH,expand=True)

label1=Label(frame1,text="python")
label1.place(x=10,y=10)

label2=Label(frame2,text="java")
label2.place(x=10,y=10)


notebook.add(frame1,text="New");
notebook.add(frame2,text="File")


win.mainloop()


