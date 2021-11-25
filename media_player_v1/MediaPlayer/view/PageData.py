from PyQt5 import QtWidgets, QtCore
import os
from ui.PageData import Ui_PageData
from PyQt5.QtWidgets import QListWidgetItem
from db import data_manager
from store import Store
from view.ListItemReview import ListItemReview


class PageData(QtWidgets.QWidget):

    def __init__(self):
        super(PageData, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_PageData()
        self.ui.setupUi(self)
        self.ui.confirm_Button.clicked.connect(self.onConfirm)
        self.ui.tabWidget.currentChanged.connect(self.tabChanged)
        self.loadReviews()

        self.mode = 'add'
        self.editId = None

    def loadReviews(self):

        for i in reversed(range(self.ui.scrollArea_layout.count())):
            self.ui.scrollArea_layout.itemAt(i).widget().deleteLater()

        reviews = data_manager.DataManager.loadReviews()
        for review in reviews:
            # review['_id'], review['title'], review['date'], review['review'], review['userId']
            myItem = ListItemReview(review)
            myItem.pass_review_to_edit.connect(self.openReviewToEdit)
            self.ui.scrollArea_layout.addWidget(myItem)

    def onConfirm(self):
        review = {
            'title': self.ui.data_title.text(),
            'date': self.ui.data_date.date(),
            'review': self.ui.data_review.text()
        }
        if self.mode == 'add':
            result = data_manager.DataManager.addReview(review['title'], review['date'], review['review'], Store.currentUser['_id'])
            if result:
                review['_id'] = result.inserted_id
                review['userId'] = Store.currentUser['_id']
                myItem = ListItemReview(review)
                myItem.pass_review_to_edit.connect(self.openReviewToEdit)
                self.ui.scrollArea_layout.addWidget(myItem)
        elif self.mode == 'edit':
            if self.editId:
                reviewObj = data_manager.DataManager.editReview(self.editId, review['title'], review['date'], review['review'])
                print(reviewObj)


    def tabChanged(self, index):
        tabText = self.ui.tabWidget.tabText(index)
        if tabText == "Data":
            self.ui.add_Button.setVisible(True)
            self.loadReviews()
            self.ui.data_title.setText('')
            self.ui.data_review.setText('')
            self.ui.data_date.setDate(QtCore.QDate())
            self.editId = None
            self.mode = 'add'
        elif tabText == "Input":
            self.ui.add_Button.setVisible(False)

    def openReviewToEdit(self, review):
        self.ui.tabWidget.setCurrentWidget(self.ui.input_tab)
        self.ui.data_title.setText(review['title'])
        self.ui.data_date.setDate(review['date'])
        self.ui.data_review.setText(review['review'])
        self.editId = review['_id']
        self.mode = 'edit'



