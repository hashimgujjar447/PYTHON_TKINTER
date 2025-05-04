from tkinter import *


window=Tk();
width=400;
height=400

sys_width=window.winfo_screenwidth()
sys_height=window.winfo_screenheight()
c_x=int((sys_width/2)-(width/2))
c_y=int((sys_height/2)-(height/2))
window.geometry(f"{width}x{height}+{c_x}+{c_y}")


def submitForm():
     if not var1.get() or not var2.get():
          label3.config(text="Both field are required")
          return;
     data=var1.get() + " " + var2.get()
     label3.config(text=f"Login with {data}")
     var1.set("");
     var2.set("")


window.title("SignIn");
var1=StringVar();
var2=StringVar();

label1=Label(window,text="Email Address :",font=("Times New Roman",16,"bold"))
label1.place(x=100,y=100,height=30)
entry1=Entry(window,font=20,textvariable=var1)

entry1.place(x=100,y=150,height=30,width=200)

label2=Label(window,text="Password :",font=("Times New Roman",16,"bold"))
label2.place(x=100,y=200,height=50)

entry2=Entry(window,font=20,show="*",textvariable=var2)

entry2.place(x=100,y=270,height=30,width=200)


button=Button(window,text="Sign In",font=20 ,bg="blue", fg="white",relief="ridge",cursor="hand2",justify=CENTER,command=submitForm)

button.place(x=100,y=330)



label3=Label(window,text="",font=20)
label3.place(x=100,y=380,width=500)



window.mainloop();