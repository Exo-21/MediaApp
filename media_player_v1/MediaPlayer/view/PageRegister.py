from PyQt5 import QtWidgets, uic
import os
from ui.PageRegister import Ui_PageRegister
from db import data_manager
from PyQt5.QtCore import pyqtSignal


class PageRegister(QtWidgets.QWidget):
    register_successful = pyqtSignal()

    def __init__(self):
        super(PageRegister, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_PageRegister()
        self.ui.setupUi(self)
        self.ui.register_Button.clicked.connect(self.registerfunction)
        self.ui.register_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.register_Confirm_Password.setEchoMode(QtWidgets.QLineEdit.Password)

    def registerfunction(self):
        username = self.ui.register_Username.text()
        password = self.ui.register_Password.text()
        password2 = self.ui.register_Confirm_Password.text()
        email = self.ui.register_Email.text()

        if password == password2:
            if data_manager.DataManager.register(email, username, password):
                self.register_successful.emit()
        else:
            pass


