from tkinter import *
from tkinter.messagebox import askretrycancel


win=Tk();
def retryCancel():
    ans=askretrycancel(title="Retry Cancel",message="Do you want to retry?")
    if ans==True:
        retryCancel();
    else:
        print("Cancelled!")
        win.quit()

button=Button(win,text="Click me",command=retryCancel)

button.place(x=10,y=10,height=50,width=50)

win.mainloop()