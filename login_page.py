from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
import MySQLdb
from PyQt5.uic import loadUiType
from os import path

from client import ClientUI
from server import ServerUI

Form2, _ = loadUiType(path.join(path.dirname(__file__), "login.ui"))

user_name = ''
password = ''

class Login(QMainWindow, Form2):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Log in")
        self.setWindowIcon(QIcon("logo.ico")) 
        self.pushButton.clicked.connect(self.handle_login)
        self.checkBox.stateChanged.connect(self.show_password)

    def handle_login(self):
        global user_name, password
        self.db = MySQLdb.connect(host="localhost",
                                  user="root",
                                  password="M.M.M@mo206",
                                  db="logs_db")
        self.cur = self.db.cursor()
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        sql = '''SELECT * FROM accounts '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if row[1] == user_name and row[2] == password:
                if row[3] == 1:
                    self.open_server_ui()
                    self.db.commit()
                elif row[3] == 0:
                    self.open_client_ui()
                    self.db.commit()
                return
        self.label.setText("تأكد من اسم المستخدم والباسورد")

    def show_password(self):
        self.lineEdit_2.setEchoMode(QLineEdit.Normal if self.checkBox.isChecked() else QLineEdit.Password)

    def open_server_ui(self):
        self.close()
        self.server_ui = ServerUI()
        self.server_ui.show()

    def open_client_ui(self):
        self.close()
        self.client_ui = ClientUI()
        self.client_ui.show()
