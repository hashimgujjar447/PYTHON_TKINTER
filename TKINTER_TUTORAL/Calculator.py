#Calculator
from tkinter import *

win=Tk() #Start

clear_on_next_input=False
def get_data(data):
    global clear_on_next_input
    print(data)
  
    
   
    if data == "C":
        input_var.set("")  # Clear the input variable
        clear_on_next_input = False
        return
    elif data == "=":
        # Replace 'x' with '*' and '÷' with '/'
        expression = input_var.get().replace("x", "*").replace("÷", "/")
        try:
           calculator(expression)
        except Exception as e:
            input_var.set("Error")  # If there's an error, show Error
            print(f"Error: {e}")
        return
    # If the input is not "=" or "C", just append the data
    if clear_on_next_input and data not in ["C", "="]:
        input_var.set("")
        clear_on_next_input = False
    input_var.set(input_var.get() + str(data))



def calculator(expression):
    global clear_on_next_input
    try:
        # Safely evaluate the expression using eval
        result = eval(expression)  # Evaluate the expression
      
        input_var.set(str(result))
  # Update the input variable with the result
        clear_on_next_input = True  # Set the flag to clear on next input
    except ZeroDivisionError:
        # Handle division by zero explicitly
        input_var.set("Error: Division by Zero")
        clear_on_next_input = True
    except Exception:
        # If there is any other error, show Error
        input_var.set("Invalid expression")
        clear_on_next_input = True
    


win.title("Calculator")
win.config(bg="yellow")
win.iconbitmap(r"C:\Users\kashi\Downloads\Calculator_30001.ico")
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
x=int((width/2)-(500/2))
y=int((height/2)-(500/2))
win.geometry(f"500x500+{x}+{y}") # Set window size and position
win.resizable(0,0)

#Creating a input variable

input_var=StringVar()


Label_Title=Label(win,text="Calculator",font=("Arial",30,"bold"),bg="yellow",fg="black")
Label_Title.place(x=25,y=20,height=60,width=450) # Set position of label

entry=Entry(win,font=("Arial",20,"bold"),bg="white",fg="black",bd=5,relief="sunken",textvariable=input_var,justify="right")
entry.place(x=20,y=100,height=50,width=460) # Set position of entry


# Creating buttons

buttons = [
    ("9", 20, 190), ("8", 135, 190), ("7", 250, 190), ("÷", 365, 190),
    ("4", 20, 260), ("5", 135, 260), ("6", 250, 260), ("x", 365, 260),
    ("1", 20, 320), ("2", 135, 320), ("3", 250, 320), ("-", 365, 320),
    ("C", 20, 390), ("0", 135, 390), ("=", 250, 390), ("+", 365, 390)
]


for (text,x,y) in buttons:
    button=Button(win,text=text,font=("Arial",20,"bold"),command=lambda t=text: get_data(t))
    button.place(x=x,y=y,height=70,width=115) # Set position of button

win.mainloop()


