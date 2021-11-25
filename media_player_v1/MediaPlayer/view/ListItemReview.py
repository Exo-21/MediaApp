from PyQt5 import QtWidgets, uic, QtCore
import os
from ui.ListItemReview import Ui_ReviewListItem
from store import Store
from db import data_manager
from PyQt5.QtCore import pyqtSignal


class ListItemReview(QtWidgets.QWidget):
    pass_review_to_edit = pyqtSignal(object)

    def __init__(self, review):
        super(ListItemReview, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_ReviewListItem()
        self.ui.setupUi(self)

        self.ui.button_remove.clicked.connect(self.removeReview)
        self.ui.button_edit.clicked.connect(self.editReview)

        self.review = review

        self.ui.title_value.setText(review['title'])

        dateText = ''
        if type(review['date']) is QtCore.QDate:
            dateText = review['date'].toString("YYYY-mm-dd")
        else:
            dateText = review['date'].strftime("%Y/%m/%d")

        self.ui.date_value.setText(dateText)
        self.ui.review_value.setText(review['review'])
        self.userId = review['userId']
        self.id = review['_id']

        self.ui.horizontalWidget_controls.setVisible(False)
        if Store.currentUser:
            if review['userId'] == Store.currentUser['_id']:
                self.ui.horizontalWidget_controls.setVisible(True)

    def removeReview(self):
        data_manager.DataManager.removeReview(self.id)
        self.deleteLater()

    def editReview(self):
        self.pass_review_to_edit.emit(self.review)
