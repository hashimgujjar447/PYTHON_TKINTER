from tkinter import *

win=Tk()

win.title("**** My First GUI ****")



win.iconbitmap(r"C:\Users\kashi\Downloads\ico.ico")

win.attributes("-alpha",0.7)

# win.config(bg="black")

win["bg"]="yellow"



# sys_width=win.winfo_screenwidth()
# sys_height=win.winfo_screenheight()
# c_x=int((sys_width/2)-(width/2))
# c_y=int((sys_height/2)-(height/2))


# print(sys_width,sys_height,c_x,c_y)



# win.geometry(f"{width}x{height}+{c_x}+{c_y}")

var=StringVar(win,value="Hello World",name="var")
var.set("Hello World")

print(var.get())




lab=Label(win,text="Hello World" ,font=("Arial",20,"bold") ,bg="red");
lab.pack()































win.mainloop()
