import sys
from PySide6.QtWidgets import QApplication
from controller.login_controller import LoginController

if __name__== "__main__":
    app = QApplication(sys.argv)

    login = LoginController()
    login.show()

    sys.exit(app.exec())

    #adm@gmail.com
    #123
