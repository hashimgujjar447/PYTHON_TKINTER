from tkinter import *
from tkinter import filedialog


win=Tk()

# def open_file():
#     var=filedialog.askopenfilename(title="Select a file",initialdir="/",filetypes=(("Text files","*.txt"),("All files","*.*")))
#     if var:
#         with open(var, 'r') as file:
#             content = file.read()
#             r=Text(win)
#             r.insert(1.0, content)
#             r.pack(pady=20)
#             # print(content)
#     else:
#         r=Label(win,text="No file selected",)
#         r.pack(pady=20)
#         #
#         print("No file selected")
#     print(r)


def save_file():
    # var=filedialog.asksaveasfilename(title="Save file",initialdir="/",filetypes=(("Text files","*.txt"),("python","*.py"),("All files","*.*")))
    # print(var)
    var=filedialog.asksaveasfile(title="Save file",initialdir="/" ,defaultextension=".txt",filetypes=(("Text files","*.txt"),("python","*.py"),("All files","*.*")))
    var.write("Hello World")
    var.close()
    print(var)


btn=Button(win,text="Open File",command=save_file)
btn.pack(pady=20)

win.mainloop()