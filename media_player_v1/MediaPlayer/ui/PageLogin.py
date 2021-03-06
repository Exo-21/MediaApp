# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PageLogin(object):
    def setupUi(self, PageLogin):
        PageLogin.setObjectName("PageLogin")
        PageLogin.resize(569, 463)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(PageLogin.sizePolicy().hasHeightForWidth())
        PageLogin.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PageLogin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(PageLogin)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_username = QtWidgets.QLabel(PageLogin)
        self.label_username.setObjectName("label_username")
        self.verticalLayout.addWidget(self.label_username)
        self.login_Username = QtWidgets.QLineEdit(PageLogin)
        self.login_Username.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    height: 40px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.login_Username.setPlaceholderText("")
        self.login_Username.setObjectName("login_Username")
        self.verticalLayout.addWidget(self.login_Username)
        self.label_password = QtWidgets.QLabel(PageLogin)
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)
        self.login_Password = QtWidgets.QLineEdit(PageLogin)
        self.login_Password.setMinimumSize(QtCore.QSize(0, 20))
        self.login_Password.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    height: 40px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.login_Password.setPlaceholderText("")
        self.login_Password.setObjectName("login_Password")
        self.verticalLayout.addWidget(self.login_Password)
        self.label = QtWidgets.QLabel(PageLogin)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.login_Button = QtWidgets.QPushButton(PageLogin)
        self.login_Button.setObjectName("login_Button")
        self.verticalLayout.addWidget(self.login_Button)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 7)

        self.retranslateUi(PageLogin)
        QtCore.QMetaObject.connectSlotsByName(PageLogin)

    def retranslateUi(self, PageLogin):
        _translate = QtCore.QCoreApplication.translate
        PageLogin.setWindowTitle(_translate("PageLogin", "Form"))
        self.label_title.setText(_translate("PageLogin", "Login"))
        self.label_username.setText(_translate("PageLogin", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_password.setText(_translate("PageLogin", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.login_Button.setText(_translate("PageLogin", "Login"))
