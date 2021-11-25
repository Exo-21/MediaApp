from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import os
from ui.PageLogin import Ui_PageLogin
from db import data_manager


class PageLogin(QtWidgets.QWidget):
    pass_user = pyqtSignal(object)

    def __init__(self):
        super(PageLogin, self).__init__()


        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_PageLogin()
        self.ui.setupUi(self)
        self.ui.login_Button.clicked.connect(self.loginfunction)
        self.ui.login_Password.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        username = self.ui.login_Username.text()
        password = self.ui.login_Password.text()

        user = data_manager.DataManager.login(username, password)
        self.pass_user.emit(user)

