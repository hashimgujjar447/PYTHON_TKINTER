from tkinter import *
from tkinter.messagebox import askyesno,askquestion

win=Tk()


val=lambda x,y: x*y;

print(val(2,6))
print(val(3,5))
btn=Button(win,text="Do you want to continue?",command=lambda:askyesno("Continue","Do you want to continue?"))
btn.pack(pady=20)



win.mainloop()