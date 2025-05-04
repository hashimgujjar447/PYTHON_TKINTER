import tkinter as tk
import os
import json
from tkinter.messagebox import showerror,showinfo

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")
NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")



def get_users():
           if os.path.exists(USERS_FILE):
                with open(USERS_FILE,"r") as f:
                     content=f.read().strip()
                     if content:
                          return json.loads(content)
          
                return {}
          
def save_users(users):
     if os.path.exists(USERS_FILE):
          with open(USERS_FILE,"w") as f:
               json.dump(users,f) 

class DashBoardApp:
    def __init__(self,root):
            self.root=root;
            self.root.title("App Dashboard")
            self.root.resizable(0,0)
            self.width = self.root.winfo_screenwidth()
            self.height = self.root.winfo_screenheight()
            self.x = int((self.width / 2) - (400 / 2))
            self.y = int((self.height / 2) - (400 / 2))
            self.root.geometry(f"400x400+{self.x}+{self.y}")


            self.current_User=None;
            self.frames={}

            for F in (SignupPage,LoginPage,DashboardPage):
                 frame=F(self.root,self)
                 print(frame)
                 self.frames[F]=frame
                 frame.grid(row=0,column=0,sticky="nsew")
            self.show_frame(LoginPage)

    def show_frame(self,frameClass):
         frame=self.frames[frameClass];
         frame.tkraise()       
    def logout(self):
         self.current_User=None;
         self.show_frame(LoginPage)
                   
             


class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
         super().__init__(parent);
         self.controller=controller

         tk.Label(self, text="Login", font=("Arial", 20,"bold")).grid(row=0, column=0, columnspan=2, pady=10,padx=120)
         tk.Label(self, text="Username").grid(row=1, column=0, padx=10, pady=5)
         tk.Label(self, text="Password").grid(row=2, column=0, padx=10, pady=10)
         self.username = tk.StringVar()
         self.password = tk.StringVar()

         tk.Entry(self, textvariable=self.username).grid(row=1, column=1)
         tk.Entry(self, textvariable=self.password, show="*").grid(row=2, column=1)

         tk.Button(self, text="Login", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)
         tk.Button(self, text="Sign Up", command=lambda: controller.show_frame(SignupPage)).grid(row=4, column=0, columnspan=2)

    def login(self):
        u = self.username.get().strip()
        p = self.password.get()
        users=get_users();
        if users.get(u)==p:
             showinfo("Success", f"Welcome, {u}!")
             self.controller.show_frame(DashboardPage)
        else:
             showerror("Error", "Invalid credentials")
                  
            
             
              



class SignupPage(tk.Frame):
    def __init__(self,parent,controller):
         super().__init__(parent);
         print("Login")
         self.controller=controller;
        
         tk.Label(self,text="Signup please",font=("Arial", 20)).grid(row=0,column=0,columnspan=2,pady=10,padx=120)

         
         tk.Label(self, text="Username").grid(row=1, column=0, padx=10, pady=5)
         tk.Label(self, text="Password").grid(row=2, column=0, padx=10, pady=10)
         tk.Label(self, text="Password").grid(row=3, column=0, padx=10, pady=10)
         self.username = tk.StringVar()
         self.password = tk.StringVar()
         self.cpassword=tk.StringVar()

         tk.Entry(self, textvariable=self.username).grid(row=1, column=1)
         tk.Entry(self, textvariable=self.password, show="*").grid(row=2, column=1)
         tk.Entry(self, textvariable=self.cpassword, show="*").grid(row=3, column=1)

         tk.Button(self, text="Signup",command=self.signup).grid(row=5, column=0, columnspan=2, pady=10)
         tk.Button(self, text="Login", command=lambda: self.controller.show_frame(LoginPage)).grid(row=6, column=0, columnspan=2)
       
    def signup(self):
          u=self.username.get();
          p=self.password.get();
          cp=self.cpassword.get();
          print(p,cp)
          if not u or not p or not cp:
               showerror("Field error","All fields are required")  
          if p != cp:
             showerror("Error", "Passwords do not match")
             return

          users = get_users()
          if u in users:
             showerror("Error", "Username already exists")
             return
          
          users[u]=p;
          save_users(users);
          showinfo("Success", "User registered successfully")
          self.controller.show_frame(LoginPage)

                   
    
            

       

class DashboardPage(tk.Frame):
    def __init__(self,parent,controller):
         super().__init__(parent);
         self.controller=controller
         
             # Welcome
         tk.Label(self, text="Personal Dashboard", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons
         tk.Button(self, text="Notes", width=20,command=self.open_notes ).grid(row=1, column=0, padx=10, pady=10)
         tk.Button(self, text="Calculator", width=20, command=self.open_calculator).grid(row=1, column=1, padx=10, pady=10)
         tk.Button(self, text="Logout", width=20, command=self.controller.logout).grid(row=2, column=0, columnspan=2, pady=10)

 # Notes Area
         self.notes_text = tk.Text(self, width=40, height=10)
         self.save_notes_btn = tk.Button(self, text="Save Notes",command=self.save_notes )

         self.calc_entry = tk.Entry(self)
         self.calc_result = tk.Label(self, text="")
         self.calc_btn = tk.Button(self, text="Calculate", command=self.calculate)
         
    def open_calculator(self):
        self.clear_widgets()
        self.calc_entry.grid(row=3, column=0, columnspan=2, pady=5)
        self.calc_btn.grid(row=4, column=0, columnspan=2)
        self.calc_result.grid(row=5, column=0, columnspan=2)

    def clear_widgets(self):
        self.notes_text.grid_remove()
        self.save_notes_btn.grid_remove()
        self.calc_entry.grid_remove()
        self.calc_btn.grid_remove()
        self.calc_result.grid_remove()   

    def open_notes(self):
        self.clear_widgets()
        self.notes_text.grid(row=3, column=0, columnspan=2, pady=10)
        self.save_notes_btn.grid(row=4, column=0, columnspan=2)
        self.load_notes()    

    def save_notes(self):
        with open(NOTES_FILE, "w") as f:
            f.write(self.notes_text.get("1.0", "end").strip())
        showinfo("Saved", "Notes saved!")

    def load_notes(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                content = f.read()
                self.notes_text.delete("1.0", "end")
                self.notes_text.insert("1.0", content)
    def calculate(self):
        try:
            expression = self.calc_entry.get()
            result = eval(expression)
            self.calc_result.config(text=f"Result: {result}")
        except:
            self.calc_result.config(text="Invalid Expression")
            
















if __name__ == "__main__":
    root=tk.Tk();
    app=DashBoardApp(root);
    root.mainloop()

