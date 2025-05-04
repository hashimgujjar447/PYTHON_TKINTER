from tkinter import *

win=Tk();

Main_Menu=Menu(win);

f_Menu=Menu(Main_Menu,tearoff=0)

f_Menu.add_command(label="New File",command=win.quit)

Sub_Menu=Menu(f_Menu,tearoff=0)
Sub_Menu.add_command(label="REd",command=win.quit)
Sub_Menu.add_command(label="Green",command=win.quit)

f_Menu.add_cascade(label="Color",menu=Sub_Menu)


f_Menu.add_command(label="Save File",command=win.quit)
f_Menu.add_command(label="Open File",command=win.quit)
f_Menu.add_command(label="Save as File",command=win.quit)
f_Menu.add_command(label="Exit",command=win.quit)



Main_Menu.add_cascade(label="File",menu=f_Menu)

win.config(menu=Main_Menu)

f1_Menu=Menu(Main_Menu,tearoff=0)
f1_Menu.add_command(label="Copy",command=win.quit)
f1_Menu.add_command(label="Paste",command=win.quit)
f1_Menu.add_command(label="Cut",command=win.quit)
f1_Menu.add_separator()
f1_Menu.add_command(label="Select All",command=win.quit)
f1_Menu.add_command(label="Undo",command=win.quit)

Main_Menu.add_cascade(label="Edit",menu=f1_Menu)

win.config(menu=Main_Menu)




win.mainloop()