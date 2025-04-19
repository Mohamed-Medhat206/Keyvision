import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from login_page import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico")) 
    login_ui = Login()
    login_ui.show()
    sys.exit(app.exec_())
