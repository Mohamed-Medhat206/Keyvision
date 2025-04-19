import socket
import MySQLdb
from threading import Thread
from flask import Flask, request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.uic import loadUiType
from os import path

Form, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))

class ServerUI(QMainWindow,Form):
    alert_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(ServerUI, self).__init__(parent)
        self.alert_signal.connect(self.show_alert)
        self.setupUi(self)
        self.setWindowTitle("Keyvision")
        self.setWindowIcon(QIcon("logo.ico")) 
        self.start_server()
        self.Handel_DB_Connection()
        self.handlebuttons()
        self.initUI()

    def show_alert(self, message):
        QMessageBox.information(self, "Alert", message)
    def initUI(self):
        self.tabWidget.tabBar().setVisible(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_Info)
        self.timer.start(1000)
        self.styles = {
            'dark': self.load_style('dark.css'),
            'light': self.load_style('light.css')
        }
        self.current_style = 'dark'
        self.setStyleSheet(self.styles[self.current_style])

    def Handel_DB_Connection(self):
        self.db = MySQLdb.connect(
        host='localhost',
        user='root',
        password='M.M.M@mo206',
        database='logs_db')
        self.cur = self.db.cursor()

    def handlebuttons(self):
        self.server.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.setting_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.about.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.accounts_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_6.clicked.connect(self.Dark_Light)
        self.Arabic_button.clicked.connect(self.Arabic_Language)
        self.English_button.clicked.connect(self.English_Language)
        self.pushButton_5.clicked.connect(self.insert_server_ip)
        self.pushButton_2.clicked.connect(self.insert_sleeptime)
        self.pushButton_7.clicked.connect(self.add_forbidden_word)
                            ##Users
        self.pushButton_4.clicked.connect(self.add_user)
        self.checkBox_2.stateChanged.connect(self.show_passowrd)
        self.checkBox_3.stateChanged.connect(self.show_passowrd)
        self.checkBox_4.stateChanged.connect(self.show_passowrd)
        self.checkBox_5.stateChanged.connect(self.show_passowrd)
        self.checkBox_6.stateChanged.connect(self.show_passowrd)
        self.pushButton_3.clicked.connect(self.update_user)
        self.pushButton_17.clicked.connect(self.delete_user)

    def on_click(self):
        ip_address = self.get_ip_address()
        self.lineEdit_2.setText(ip_address)

    def get_ip_address(self):
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address

    def Dark_Light(self):
        self.current_style = 'light' if self.current_style == 'dark' else 'dark'
        self.setStyleSheet(self.styles[self.current_style])
        self.setStyleSheet(self.styles[self.current_style])

    def load_style(self, style_file):
        with open(style_file, 'r') as file:
            return file.read()

    def English_Language(self):
        self.lineEdit_22.setPlaceholderText("Enter user name")
        self.lineEdit_20.setPlaceholderText("Enter Passowrd")
        self.lineEdit_23.setPlaceholderText("Enter Passowrd")
        self.lineEdit_21.setPlaceholderText("Re-enter new password")
        self.lineEdit_4.setPlaceholderText("Enter user name")
        self.lineEdit_24.setPlaceholderText("Enter user name")
        self.lineEdit_5.setPlaceholderText("Enter old password")
        self.lineEdit_19.setPlaceholderText("Enter new password")
        self.lineEdit_18.setPlaceholderText("Re-enter new password")
        self.checkBox_2.setText("Show password")
        self.checkBox_3.setText("Show password")
        self.checkBox_4.setText("Show password")
        self.checkBox_5.setText("Show password")
        self.checkBox_6.setText("Show password")
        self.Admin_checkBox.setText("Make it Admin")
        self.pushButton_4.setText("Add new user")
        self.pushButton_3.setText("Edit user data")
        self.pushButton_17.setText("Delete user data")
        self.pushButton_2.setText("Save")
        self.pushButton_5.setText("Save")
        self.pushButton_6.setText("change mode")
        self.pushButton_7.setText("save")
        self.pushButton.setText("Get Server Ip")
        self.server.setText("Server")
        self.setting_button.setText("Settings")
        self.about.setText("About Us")
        self.accounts_button.setText("Accounts")
        self.label_6.setText("Sleep Time")
        self.label_8.setText("forbidden words")
        self.label_5.setText("Server IP")
        self.label_4.setText("Change App Mode (Dark / light)")
        self.label_12.setText("Change App Language")

    def Arabic_Language(self):
        self.lineEdit_22.setPlaceholderText("أدخل اسم المستخدم")
        self.lineEdit_20.setPlaceholderText("أدخل كلمة المرور ")
        self.lineEdit_23.setPlaceholderText("أدخل كلمة المرور ")
        self.lineEdit_21.setPlaceholderText("أعد أدخال كلمة المرور")
        self.lineEdit_4.setPlaceholderText("أدخل اسم المستخدم")
        self.lineEdit_24.setPlaceholderText("أدخل اسم المستخدم")
        self.lineEdit_5.setPlaceholderText("أدخل كلمة المرور القديمة")
        self.lineEdit_19.setPlaceholderText("أدخل كلمة المرور الجديده")
        self.lineEdit_18.setPlaceholderText("أعد أدخال كلمة المرور الجديده")
        self.checkBox_2.setText("إظهار كلمة المرور")
        self.checkBox_3.setText("إظهار كلمة المرور")
        self.checkBox_4.setText("إظهار كلمة المرور")
        self.checkBox_5.setText("إظهار كلمة المرور")
        self.checkBox_6.setText("إظهار كلمة المرور")
        self.Admin_checkBox.setText("أجعله أدمن")
        self.pushButton_4.setText("أضافة مستخدم جديد")
        self.pushButton_3.setText("تعديل معلومات المستخدم")
        self.pushButton_17.setText("حذف معلومات مستخدم")
        self.pushButton_2.setText("حفظ")
        self.pushButton_5.setText("حفظ")
        self.pushButton_6.setText("تغيير الوضع")
        self.pushButton_7.setText("حفظ")
        self.pushButton.setText("إيجاد IP الخادم")
        self.server.setText("الخادم")
        self.setting_button.setText("الاعدادات")
        self.about.setText("من نحن")
        self.accounts_button.setText("الحسابات")
        self.label_6.setText("مدة النوم")
        self.label_8.setText("الكلمات المحظورة")
        self.label_5.setText("IP الخادم")
        self.label_4.setText("تغيير وضع البرنامج (مضئ / مظلم)")
        self.label_12.setText("تغيير لغة البرنامج")

    def insert_server_ip(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="M.M.M@mo206",
            database="logs_db"
        )
        self.cursor = self.db.cursor()
        server_ip = self.lineEdit_2.text()
        
        if server_ip:
            self.cursor.execute("INSERT INTO server_ip (serv_ip) VALUES (%s)", (server_ip,))
            self.db.commit()
            self.cursor.close()
            print("server done")
            self.statusBar().showMessage('IP Saved')
        else:
            self.statusBar().showMessage('Enter data')

    def add_forbidden_word(self):
        forbidden_word = self.lineEdit_3.text()
        hostname = socket.gethostname()
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="M.M.M@mo206",
            database="logs_db"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("INSERT INTO forbiddenwords (words) VALUES (%s)", (forbidden_word,))
        self.db.commit()
        self.cursor.close()
        print("done")
        self.lineEdit_3.clear()
        self.statusBar().showMessage('forbidden word Saved')
        
    def insert_sleeptime(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="M.M.M@mo206",
            database="logs_db"
        )
        self.cursor = self.db.cursor()
        sleeptime = self.spinBox.text()
        self.cursor.execute("INSERT INTO sleeptime (sleeptime) VALUES (%s)", (sleeptime,))
        self.db.commit()
        self.cursor.close()
        print("sleep time done")
        self.statusBar().showMessage('time Saved')
    
    def show_Info(self):
        self.tableWidget.setRowCount(0)
        self.db = MySQLdb.connect(
            host='localhost',
            user='root',
            password='M.M.M@mo206',
            database='logs_db')
        self.cur = self.db.cursor() 
        self.cur.execute('''SELECT pc_id,key_pressed, cpu_usage, memory_usage,timestamp FROM logs''')
        for row, data in enumerate(self.cur):
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column, item in enumerate(data):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))


    def start_server(self):
        app = Flask(__name__)
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="M.M.M@mo206",
            database="logs_db"
        )
        cursor = db.cursor()

        @app.route("/logs", methods=["POST"])
        def receive_logs():
            return self.handle_log_request()
        server_thread = Thread(target=lambda: app.run(host="0.0.0.0", port=5000))
        server_thread.daemon = True
        server_thread.start()

    def handle_log_request(self):
        try:
            data = request.get_json()
            pc_id = data["pc_id"]
            cpu_usage = data["cpu_usage"]
            memory_usage = data["memory_usage"]
            key_pressed = data["key_pressed"]

            db = MySQLdb.connect(
                host="localhost",
                user="root",
                password="M.M.M@mo206",
                database="logs_db"
            )
            cursor = db.cursor()

            cursor.execute("SELECT words FROM forbiddenwords")
            forbidden_words = [row[0].strip().lower() for row in cursor.fetchall()]

            is_forbidden = any(word in key_pressed.lower() for word in forbidden_words)

            if is_forbidden:
                alert_message = (
                    "Forbidden Word Detected!\n\n"
                    f"Person: {pc_id}\n"
                    f"Message: {key_pressed}"
                )
                self.alert_signal.emit(alert_message)

            cursor.execute("""
                INSERT INTO logs (pc_id, cpu_usage, memory_usage, key_pressed)
                VALUES (%s, %s, %s, %s)
            """, (pc_id, cpu_usage, memory_usage, key_pressed))
            db.commit()
            cursor.close()
            db.close()

            return {"message": "Logs saved successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500


    
    def show_passowrd(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_21.setEchoMode(QLineEdit.Normal)
        if self.checkBox_2.isChecked() == False :
            self.lineEdit_21.setEchoMode(QLineEdit.Password)

        if self.checkBox_3.isChecked():
            self.lineEdit_20.setEchoMode(QLineEdit.Normal)
        if self.checkBox_3.isChecked() == False :
            self.lineEdit_20.setEchoMode(QLineEdit.Password)
        
        if self.checkBox_4.isChecked():
            self.lineEdit_5.setEchoMode(QLineEdit.Normal)
        if self.checkBox_4.isChecked() == False :
            self.lineEdit_5.setEchoMode(QLineEdit.Password)
        
        if self.checkBox_5.isChecked():
            self.lineEdit_19.setEchoMode(QLineEdit.Normal)
        if self.checkBox_5.isChecked() == False :
            self.lineEdit_19.setEchoMode(QLineEdit.Password)
        
        if self.checkBox_6.isChecked():
            self.lineEdit_18.setEchoMode(QLineEdit.Normal)
        if self.checkBox_6.isChecked() == False :
            self.lineEdit_18.setEchoMode(QLineEdit.Password)
    
    def add_user(self):
        user_name = self.lineEdit_22.text()
        password1 = self.lineEdit_20.text()
        password2 = self.lineEdit_21.text()
        ISAdmin = self.Admin_checkBox.isChecked()
        username_exists = True
        if password1 == password2 :
            self.cur.execute('''SELECT UserName, Pass FROM accounts''')
            data = self.cur.fetchall()
            for row in data:
                if user_name == row[0]:
                    username_exists = False
                    QMessageBox.critical(self,"Problem" ,"The username already exists. Enter another username")
            if username_exists:
                    self.cur.execute('''INSERT INTO
                                        accounts(UserName , Pass , IsAdmin)
                                        VALUES(%s, %s, %s)''', (user_name, password2 , ISAdmin)
                                        )
                    self.statusBar().showMessage('تم أضافة المستخدم بنجاح')
                    self.lineEdit_22.clear()
                    self.lineEdit_20.clear()
                    self.lineEdit_21.clear()
                    self.db.commit()
        else:
            self.statusBar().showMessage('كلمة السر غير متطابقه')  

    def update_user(self):
        user_name = self.lineEdit_4.text()
        old_pass = self.lineEdit_5.text()
        new_pass1 = self.lineEdit_19.text()
        new_pass2 = self.lineEdit_18.text()
        sql = '''SELECT * FROM accounts '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data :
            if row[1] == user_name :
                if row[2] == old_pass :
                    if new_pass1 == new_pass2 :
                        self.cur.execute('''UPDATE accounts SET Pass = %s WHERE UserName = %s AND Pass = %s''',((new_pass2,user_name,row[2])))
                        self.db.commit()
                        self.statusBar().showMessage('تم تعديل بينات المستخدم بنجاح')
                        self.lineEdit_4.text()
                        self.lineEdit_5.text()
                        self.lineEdit_19.text()
                        self.lineEdit_18.text()
                    else:
                        self.statusBar().showMessage('كلمة السر غير متطابقه')
                else:
                    self.statusBar().showMessage('كلمة السر القديمه غير صحيحة')
            else:
                self.statusBar().showMessage('اسم المستخدم غير صحيح')

    def delete_user(self):
        user_name = self.lineEdit_24.text()
        password = self.lineEdit_23.text()
        sql = '''SELECT * FROM accounts '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data :
            if row[1] == user_name and row[2] == password :
                self.cur.execute('''DELETE  FROM accounts WHERE UserName = %s AND Pass = %s ''', (user_name,password))
                self.db.commit()
                self.statusBar().showMessage('Deleted')
                self.lineEdit_24.clear()
                self.lineEdit_23.clear()
