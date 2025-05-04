from tkinter import *
from tkinter.messagebox import showerror,askokcancel

root = Tk()
# adding functions
#List_items

def change_theme():
    theme = theme_var.get()
    if theme == "light":
        root.config(bg="lightblue")
        task_entry.config(bg="white", fg="black")
        task_listbox.config(bg="white", fg="black")
    elif theme == "dark":
        root.config(bg="#2e2e2e")
        task_entry.config(bg="#444", fg="white")
        task_listbox.config(bg="#444", fg="white")



def reload_todo_from_file():
    try:
        with open("tasks.txt","r") as file:
            for line in file:
                line=line.strip()
                if line:
                    list_items.append(line)

            i.set(list_items)        
    except FileNotFoundError:
        showerror(title="File Not Found" ,message="Sorry we can not find your file")




def save_to_file():
    with open("tasks.txt","w") as file:
        for task in list_items:    
            print(task)
            file.write(f"{task}\n")
        
        


def add_todo():
    text=str(todo_text.get())
    if not text.strip():
        showerror("Empty Input", "Please enter a valid todo item.")
        return


    if len(text) > 0:
        print(text)
        if text in list_items:
            showerror(title="Duplicate item",message="This todo is already exist");
            return;
       
        list_items.append(text)
        todo_text.set("")
        i.set(list_items)
        task_listbox.selection_clear(0, END)
        task_listbox.selection_set(END)
        task_listbox.see(END)
        save_to_file()



def delete_todo():
    ans=askokcancel("Delete", "Are you sure you want to delete this todo?")
    if not ans:
        return
    
    selected = task_listbox.curselection()
    print(selected)
    if selected:
        index = selected[0]
        del list_items[index]
        i.set(list_items)
    save_to_file()    

def clear_all():
    ans=askokcancel("Clear All", "Are you sure you want to clear all todos?")
    if not ans:
        return
    list_items.clear();
    i.set(list_items);
    save_to_file()

# Initialize main window

root.title("To-Do List App")

root.config(bg="lightblue")

root.resizable(False, False)
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
x=int((width/2)-(400/2))
y=int((height/2)-(430/2))
root.geometry(f"400x430+{x}+{y}")


# Entry field to add tasks
# Entry variable
list_items=[]
i=StringVar(value=list_items)
todo_text=StringVar()
theme_var=StringVar(value="light")
reload_todo_from_file()

task_entry = Entry(root, font=("Arial", 14), width=25,textvariable=todo_text)
task_entry.pack(pady=20,ipadx=10)

# Listbox to display tasks




task_listbox = Listbox(root, font=("Arial", 14), width=30, height=10,listvariable=i)
task_listbox.pack(pady=10)

#  Theme selection
light_radio = Radiobutton(root, text="Light Mode", variable=theme_var, value="light", command=change_theme, bg="lightblue")
light_radio.place(x=50, y=320)

dark_radio = Radiobutton(root, text="Dark Mode", variable=theme_var, value="dark", command=change_theme, bg="lightblue")
dark_radio.place(x=200, y=320)


# buttons

add_button=Button(root,text="Add todo",command=add_todo)
add_button.place(x=50,y=370)

delete_button=Button(root,text="Delete Select todo",command=delete_todo)
delete_button.place(x=150,y=370)

clear_button = Button(root, text="Clear All", command=clear_all)
clear_button.place(x=280, y=370)




# Run the application
root.mainloop()
