# 🧑‍💻 Tkinter Login/Signup App

A simple GUI-based **Login and Signup application** built using Python's `tkinter` module. It allows users to create an account and log in using a username and password, storing data in a local `users.json` file.

---

## 🚀 Features

- ✅ User Registration (Sign Up)
- ✅ User Login with Validation
- ✅ Password confirmation
- ✅ Username uniqueness check
- ✅ Data saved to `users.json`
- ✅ Error and success dialogs using `messagebox`
- ✅ Profile Page:
  - Displays logged-in user's profile details.
  - Shows username and password (can be replaced with more details later).

---

## 📁 File Structure

```
LOGIN_SIGNUP_APP/
│
├── main.py       # Main application file
└── users.json    # User credentials stored in JSON format
                                    # (empty on first run)
```

---

## 🧰 Technologies Used

- **Python 3.x**: Core programming language.
- **Tkinter**: Standard GUI library for Python.
- **JSON**: Used for local data persistence.

---

## 📸 Screenshots

### 🔐 Login Window

- Enter your credentials to log in.

### 📝 Sign Up Window

- Register with a new username and password.
- Confirms password before registration.

---

## 💡 How It Works

1. On startup, the Login window appears.
2. New users can click "Sign Up" to open the registration form.
3. The credentials are stored in `users.json` in this format:

```json
{
  "john_doe": "mypassword123",
  "jane_doe": "pass456"
}
```

### 🛡️ Notes

- Passwords are stored in plain text (for demo purposes). For real applications, use password hashing (e.g., bcrypt).
- If `users.json` does not exist or is empty, the app will create or handle it gracefully.

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests to improve functionality, such as:

- Implementing password hashing.
- Adding login session persistence.
- Enhancing input validation.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as per the license terms.

---

## 📧 Contact

For any questions or feedback, feel free to reach out:

- **Email**: your_email@example.com
- **GitHub**: [YourGitHubProfile](https://github.com/YourGitHubProfile)

---
