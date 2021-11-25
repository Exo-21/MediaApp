from PyQt5 import QtWidgets, QtCore
import os
from ui.PageImdb import Ui_PageImdb
from PyQt5.QtWidgets import QListWidgetItem
from db import data_manager
from store import Store
from view.ViewImdb import ViewImdb
import re
from requests import get

from view.ListItemReview import ListItemReview


class PageImdb(QtWidgets.QWidget):

    def __init__(self):
        super(PageImdb, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_PageImdb()
        self.ui.setupUi(self)

        self.ui.button_search.clicked.connect(self.search_by_title)

    def search_by_file_name(self, file_name):
        for i in reversed(range(self.ui.scrollArea_layout.count())):
            self.ui.scrollArea_layout.itemAt(i).widget().deleteLater()

        data = self.get_data_by_file_name(file_name)
        myItem = ViewImdb(data)
        self.ui.scrollArea_layout.addWidget(myItem)

    def get_data_by_file_name(self, file_name):
        file_name = ' '.join(file_name.split('.')[:-1])
        new_title = ''
        for x in file_name.split(' '):
            y = re.search("^S[0-9]+E[0-9]+", x.upper())
            if y:
                break
            new_title += f"{x} "

        new_title = new_title[:-1]

        request_url = f"https://www.omdbapi.com/?apikey=146fc09d&s={new_title}"
        data = get(request_url).json()
        movieId = data['Search'][0]['imdbID']
        request_url = f"https://www.omdbapi.com/?apikey=146fc09d&i={movieId}"
        data = get(request_url).json()
        return data

    def search_by_title(self):
        title = self.ui.lineEdit_search.text()
        request_url = f"https://www.omdbapi.com/?apikey=146fc09d&s={title}"
        data = get(request_url).json()

        for movie in data['Search']:
            movieId = movie['imdbID']
            movie_url = f"https://www.omdbapi.com/?apikey=146fc09d&i={movieId}"
            movie_data = get(movie_url).json()
            myItem = ViewImdb(movie_data)
            self.ui.scrollArea_layout.addWidget(myItem)
