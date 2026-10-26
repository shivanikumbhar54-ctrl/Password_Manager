# Password_Manager
# Personal Password Manager 🔐

A secure, lightweight command-line tool built with Python to generate, store, and look up account credentials safely on your local machine.

---

## 🚀 Features

- **Dynamic Generation:** Automatically generates secure, 8-character passwords with alphanumeric characters and symbols (`string.ascii_letters`, `string.digits`, and symbols).
- **Instant Integration:** Gives you the choice to automatically save a newly generated password directly to a target website entry.
- **Local Persistence:** Saves everything seamlessly into a local text database (`passwords.txt`) so your records remain intact when you close the application.
- **Robust Parsing:** Implements parsing limits (`.split(":", 1)`) to ensure that passwords containing custom characters or structural symbols don't crash your system.

---

## 🛠️ How to Setup and Run

### 1. Prerequisites
Ensure you have Python 3 installed on your system. You can check your version by running:
```bash
python --version
```

### 2. Execution Steps
Clone this repository or download the source code, open your terminal inside the folder, and run:
```bash
python password_Manager.py
```

---

## 📋 Interactive Menu Options

1. **Save Password:** Manually register a website name and custom password configuration.
2. **View Passwords:** Fetch and neatly display all active credentials in your vault line-by-line.
3. **Generate Password:** Instantiate a completely random high-strength password phrase with an optional save hook.
4. **Exit:** Securely close file streaming processes and terminate execution.

---

## ⚠️ Security Warning

**Important Note for Public Repositories:** This app stores encrypted or plain-text values directly inside a local text file called `passwords.txt`. 

If you plan to use this script for your real personal passwords, you **MUST** change your GitHub repository setting from **Public to Private** to prevent unauthorized users from viewing your active file history!
