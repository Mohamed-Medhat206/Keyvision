# KeyVision 🖥️🔐

**KeyVision** is a personal project built using **Python**, **PyQt5**, and **Flask**. It’s a real-time network monitoring and key logging system designed to help administrators observe system performance and user input across a local network.

This project was created to increase my skills in Python, desktop development, client-server communication, and database integration.

---

## 🚀 Technologies Used

- Python 3
- PyQt5
- Flask
- MySQL
- psutil
- threading

---

## 🔧 Features

- 🧠 **Real-Time Monitoring**: CPU and memory usage tracking across connected clients
- ⌨️ **Keylogger**: Logs and sends typed input with support for forbidden word alerts
- 🖥️ **PyQt5 GUI**:
  - Admin (Server) UI with live data display and user management
  - Lightweight client UI running in the background
- 🌐 **Flask API**: For communication between clients and server
- 📁 **MySQL Integration**: Stores logs, credentials, and configuration
- 🌙 **Theme Switching**: Light/Dark mode toggle
- 🌍 **Multilingual Support**: Arabic and English interface
- 🔐 **Role-Based Login**: Admin or client views depending on login

---


## 🧠 What I Learned

- Building full GUI applications with PyQt5
- Working with MySQL in Python
- Creating REST APIs with Flask
- Using threading for background operations
- Capturing and analyzing system input/output

---
## ▶️ How to Run the App

1. **Clone the project and install the requirements:**
   ```bash
   pip install -r requirements.txt

2. **Set up MySQL and import the database:
  -  Make sure you have MySQL installed. Then, create the database and tables by importing (logs_db) SQL file
3- Run the app:
   ```bash
   python main.py

---

## 🧪 To Test the Login

Admin access (server mode):
Username: admin
Password: admin

Client access (background mode):
Username: client
Password: client
