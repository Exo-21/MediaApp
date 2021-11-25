from PyQt5 import QtWidgets, uic
import os
from ui.PageHome import Ui_PageHome


class PageHome(QtWidgets.QWidget):
    def __init__(self):
        super(PageHome, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_PageHome()
        self.ui.setupUi(self)

        self.ui.buttonLogout.setVisible(False)