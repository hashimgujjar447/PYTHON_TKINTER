import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import json
import os

# File paths
USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")
NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

# Load and save users
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Main App
class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Dashboard")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.current_user = None
        self.frames = {}

        for F in (LoginPage, SignupPage, DashboardPage):
            frame = F(self.root,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

    def logout(self):
        self.current_user = None
        self.show_frame(LoginPage)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Login", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="Username").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Password").grid(row=2, column=0, padx=10, pady=5)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Entry(self, textvariable=self.username).grid(row=1, column=1)
        tk.Entry(self, textvariable=self.password, show="*").grid(row=2, column=1)

        tk.Button(self, text="Login", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Sign Up", command=lambda: controller.show_frame(SignupPage)).grid(row=4, column=0, columnspan=2)

    def login(self):
        u = self.username.get().strip()
        p = self.password.get()
        users = load_users()
        if users.get(u) == p:
            self.controller.current_user = u
            showinfo("Success", f"Welcome, {u}!")
            self.controller.show_frame(DashboardPage)
        else:
            showerror("Error", "Invalid credentials")

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Sign Up", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="Username").grid(row=1, column=0)
        tk.Label(self, text="Password").grid(row=2, column=0)
        tk.Label(self, text="Confirm Password").grid(row=3, column=0)

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_password = tk.StringVar()

        tk.Entry(self, textvariable=self.username).grid(row=1, column=1)
        tk.Entry(self, textvariable=self.password, show="*").grid(row=2, column=1)
        tk.Entry(self, textvariable=self.confirm_password, show="*").grid(row=3, column=1)

        tk.Button(self, text="Register", command=self.register).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Back to Login", command=lambda: controller.show_frame(LoginPage)).grid(row=5, column=0, columnspan=2)

    def register(self):
        u = self.username.get().strip()
        p = self.password.get()
        cp = self.confirm_password.get()

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
        self.controller.show_frame(LoginPage)

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Welcome
        tk.Label(self, text="Personal Dashboard", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons
        tk.Button(self, text="Notes", width=20, command=self.open_notes).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self, text="Calculator", width=20, command=self.open_calculator).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self, text="Logout", width=20, command=controller.logout).grid(row=2, column=0, columnspan=2, pady=10)

        # Notes Area
        self.notes_text = tk.Text(self, width=40, height=10)
        self.save_notes_btn = tk.Button(self, text="Save Notes", command=self.save_notes)

        # Calculator
        self.calc_entry = tk.Entry(self)
        self.calc_result = tk.Label(self, text="")
        self.calc_btn = tk.Button(self, text="Calculate", command=self.calculate)

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

    def open_calculator(self):
        self.clear_widgets()
        self.calc_entry.grid(row=3, column=0, columnspan=2, pady=5)
        self.calc_btn.grid(row=4, column=0, columnspan=2)
        self.calc_result.grid(row=5, column=0, columnspan=2)

    def calculate(self):
        try:
            expression = self.calc_entry.get()
            result = eval(expression)
            self.calc_result.config(text=f"Result: {result}")
        except:
            self.calc_result.config(text="Invalid Expression")

    def clear_widgets(self):
        self.notes_text.grid_remove()
        self.save_notes_btn.grid_remove()
        self.calc_entry.grid_remove()
        self.calc_btn.grid_remove()
        self.calc_result.grid_remove()

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
