from tkinter import *

win=Tk()

def checkbutton_callback():
    print("Checkbutton clicked")
    lb.config(text="Checkbutton clicked")

menu_Button=Menubutton(win, text="File menu")
menu_Button.menu=Menu(menu_Button,tearoff=0)
menu_Button["menu"]=menu_Button.menu


menu_Button.menu.add_checkbutton(label="New File",command=checkbutton_callback)
menu_Button.menu.add_checkbutton(label="Save File",command=checkbutton_callback)
menu_Button.menu.add_checkbutton(label="Open File",command=checkbutton_callback)
menu_Button.menu.add_checkbutton(label="Exit",command=win.quit)

menu_Button.pack()


lb=Label(win, text="")
lb.pack()

win.mainloop()