from tkinter import *
from tkinter.messagebox import showinfo, showerror
import json
import os

APP_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(APP_DIRECTORY, "users.json")

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE,"r") as f:
            content=f.read().strip()
            if content:
                return json.loads(content)
    return {}


def save_users(users):
    if os.path.exists(USER_FILE):
        with open(USER_FILE,"w") as f:
            json.dump(users, f, indent=4)


def login():
    u = username.get().strip()
    p = password.get()

    if not u or not p:
        showerror("Error", "Both fields are required")
        return

    users = load_users()
    print(users)  # Debugging line to check loaded users
    if users.get(u) == p:
        showinfo("Success", f"Welcome, {u}!")
        login_win.withdraw()
        open_profile()
    else:
        showerror("Error", "Invalid username or password")

# Open signup window
def open_signup():
    login_win.withdraw()

    def register():
        u = su_username.get().strip()
        p = su_password.get()
        cp = su_confirm_password.get()

        if not u or not p or not cp:
            showerror("Error", "All fields are required")
            return

        if p != cp:
            showerror("Error", "Passwords do not match")
            return

        users = load_users()
        if u in users:
            showerror("Error", "Username already exists")
            return

        users[u] = p
        save_users(users)
        showinfo("Success", "User registered successfully")
        signup_win.destroy()
        login_win.deiconify()

    # Signup Window
    signup_win = Toplevel()
    signup_win.title("Sign Up")
    signup_win.geometry("350x300")
    signup_win.resizable(False, False)

    su_username = StringVar()
    su_password = StringVar()
    su_confirm_password = StringVar()

    Label(signup_win, text="Signup", font=("Arial", 18)).pack(pady=10)
    Entry(signup_win, textvariable=su_username, font=("Arial", 12), width=25).pack(pady=5)
    Entry(signup_win, textvariable=su_password, show="*", font=("Arial", 12), width=25).pack(pady=5)
    Entry(signup_win, textvariable=su_confirm_password, show="*", font=("Arial", 12), width=25).pack(pady=5)

    Button(signup_win, text="Register", width=15, command=register).pack(pady=10)
    Button(signup_win, text="Back to Login", command=lambda: [signup_win.destroy(), login_win.deiconify()]).pack()


def open_profile():
    profile_win=Toplevel();
    profile_win.title("User profile");
    profile_win.geometry("350x300");
    profile_win.resizable(0,0)
    pu=username.get()
    
    Label(profile_win, text=f"Profile of {pu}", font=("Arial", 18)).pack(pady=10)
    
    # Load user info (you can expand this later with more details)
    users = load_users()
    user_password = users.get(pu, "Not Found")

    Label(profile_win, text=f"Username: {pu}", font=("Arial", 12)).pack(pady=5)
    Label(profile_win, text=f"Password: {user_password}", font=("Arial", 12)).pack(pady=5)

    def logout():
        profile_win.destroy()
        login_win.deiconify()

    Button(profile_win, text="Logout", width=15, command=logout).pack(pady=10)










# Login Window
login_win = Tk()
login_win.title("Login")
login_win.geometry("350x250")
login_win.resizable(False, False)

username = StringVar()
password = StringVar()

Label(login_win, text="Login", font=("Arial", 18)).pack(pady=10)
Entry(login_win, textvariable=username, font=("Arial", 12), width=25).pack(pady=5)
Entry(login_win, textvariable=password, show="*", font=("Arial", 12), width=25).pack(pady=5)

Button(login_win, text="Login", width=15, command=login).pack(pady=10)
Button(login_win, text="Sign Up", command=open_signup).pack()

login_win.mainloop()
