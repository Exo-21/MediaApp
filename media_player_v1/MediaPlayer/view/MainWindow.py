from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialogButtonBox
import os
from ui.MainWindow import Ui_MainWindow
import ui.rc
from store import Store
from db import data_manager


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui.label_title_bar_top.installEventFilter(self)

        self.file = "../ui/styles/default.qss"
        with open(self.file, "r") as fh:
            self.setStyleSheet(fh.read())

        self.pages = {
            "FileTree": {
                'page': self.ui.page_filetree,
                'button': 'btn_page_filetree'
            },
            "Home": {
                'page': self.ui.page_home,
                'button': 'btn_page_home'
            },
            "Player": {
                'page': self.ui.page_player,
                'button': 'btn_page_player'
            },
            "Register": {
                'page': self.ui.page_register,
                'button': 'btn_page_register'
            },
            "Login": {
                'page': self.ui.page_login,
                'button': 'btn_page_login'
            },
            "Data": {
                'page': self.ui.page_data,
                'button': 'btn_page_data'
            },
            "Imdb": {
                'page': self.ui.page_imdb,
                'button': 'btn_page_imdb'
            }
        }

        self.user = None

        self.ui.btn_close.clicked.connect(self.OnClose)
        self.ui.btn_minimize.clicked.connect(self.OnMinimize)
        self.ui.btn_toggle_menu.clicked.connect(self.ToggleMenu)

        self.ui.btn_page_filetree.clicked.connect(lambda: self.ChangePage("FileTree"))
        self.ui.btn_page_home.clicked.connect(lambda: self.ChangePage("Home"))
        self.ui.btn_page_player.clicked.connect(lambda: self.ChangePage("Player"))
        self.ui.btn_page_login.clicked.connect(lambda: self.ChangePage("Login"))
        self.ui.btn_page_register.clicked.connect(lambda: self.ChangePage("Register"))
        self.ui.btn_page_data.clicked.connect(lambda: self.ChangePage("Data"))
        self.ui.btn_page_imdb.clicked.connect(lambda: self.ChangePage("Imdb"))

        self.ui.page_login.pass_user.connect(self.setUser)
        self.ui.page_filetree.pass_file_path.connect(self.ui.page_player.open_file_tree)
        self.ui.page_filetree.pass_imdb_search_file.connect(self.search_imdb_by_file_name)
        self.ui.page_register.register_successful.connect(lambda: self.ChangePage("Login"))

        self.ui.page_home.ui.buttonLogout.clicked.connect(self.logout)

        self.show()

    def addToPlaylist(self, filepath):
        self.ui.page_player.open_file_tree(filepath)
        self.ChangePage("Player")

    def setUser(self, user):
        Store.setUser(user)
        self.ChangePage("Home")
        self.ui.btn_page_data.setVisible(True)
        self.ui.btn_page_login.setVisible(False)
        self.ui.btn_page_register.setVisible(False)
        self.ui.page_home.ui.buttonLogout.setVisible(True)

    def logout(self):
        Store.setUser(None)
        self.ChangePage("Home")
        self.ui.btn_page_data.setVisible(False)
        self.ui.btn_page_login.setVisible(True)
        self.ui.btn_page_register.setVisible(True)
        self.ui.page_home.ui.buttonLogout.setVisible(False)

    def OnClose(self):
        QtCore.QCoreApplication.exit(0)

    def OnMinimize(self):
        self.showMinimized()

    def OnMaximizeRestore(self):
        self.showMaximized()

    def ToggleMenu(self):
        width = self.ui.frame_left_menu.width()
        defaultWidth = 70
        toggleWidth = 200

        if width == defaultWidth:
            toggleWidth = 200
        else:
            toggleWidth = 70

        self.animation = QtCore.QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(toggleWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def ChangePage(self, page):
        self.ui.stackedWidget_pages.setCurrentWidget(self.pages[page]['page'])
        self.selectMenu(self.pages[page]['button'])
        if Store.currentUser:
            if not data_manager.DataManager.isUserSignedIn(Store.currentUser['_id'], Store.currentUser['token']):
                self.logout()


    def selectMenu(self, btn_name):
        for w in self.ui.frame_left_menu.findChildren(QtWidgets.QPushButton):
            if w.objectName() == btn_name:
                select = w.styleSheet() + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
                w.setStyleSheet(select)
            else:
                deselect = w.styleSheet().replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
                w.setStyleSheet(deselect)

    def search_imdb_by_file_name(self, file_name):
        self.ui.page_imdb.search_by_file_name(file_name)
        self.ChangePage('Imdb')

