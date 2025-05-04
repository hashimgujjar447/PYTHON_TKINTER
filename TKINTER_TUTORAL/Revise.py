from tkinter import *
window=Tk();

window.title("My First GUI")

window.minsize(300, 200)
window.maxsize(600, 400)

window["bg"]="lightblue"

Main_Menu=Menu(window);
f_menu=Menu(Main_Menu,tearoff=0);

f_newFile=Menu(f_menu,tearoff=0);

f_menu.add_cascade(label="New File",menu=f_newFile);
f_newFile.add_command(label="New File",command=window.quit);
f_newFile.add_command(label="New File",command=window.quit);



f_menu.add_command(label="Save File",command=window.quit);
f_menu.add_command(label="Open File",command=window.quit);
f_menu.add_command(label="Exit",command=window.quit);

Main_Menu.add_cascade(label="File",menu=f_menu)

window.config(menu=Main_Menu);

# For edit menu
edit_menu=Menu(Main_Menu,tearoff=0);
edit_menu.add_command(label="Copy",command=window.quit);
edit_menu.add_command(label="Paste",command=window.quit);
edit_menu.add_command(label="Cut",command=window.quit);
edit_menu.add_separator();
edit_menu.add_command(label="Select All",command=window.quit);
edit_menu.add_command(label="Undo",command=window.quit);

Main_Menu.add_cascade(label="Edit",menu=edit_menu)





# Adding a course section

lb=Label(window,text="Course Section",bg="lightblue",font=("Arial", 12),fg="black")

lb.place(relx=0.5,rely=0.1,anchor=CENTER)

lb2=Label(window,text="Please select a course",bg="lightblue",font=("Arial", 12),fg="black")
lb2.place(relx=0.5,rely=0.2,anchor=CENTER)


# Adding a listbox
LIST_OPT=(("python","py"),("java","java"),("c++","cpp"),("c#","c#"))

for i in LIST_OPT:
    RADIO_BUTTON=Radiobutton(window,text=i[0],value=i[1],bg="lightblue",font=("Arial", 12),fg="black", width=10)
    RADIO_BUTTON.pack(padx=10,pady=20,anchor=W)
   


LIST=["Python","C++","java"]
value = StringVar()
value.set("Select a language") 

menu_option=OptionMenu(window,value,*LIST)


menu_option.place(relx=0.5,rely=0.3,anchor=CENTER,width=100,height=50)


btn=Button(window,text="Submit",bg="lightblue",relief="ridge")


btn.place(relx=0.5,rely=0.4,anchor=CENTER,width=100,height=50)

window.mainloop();