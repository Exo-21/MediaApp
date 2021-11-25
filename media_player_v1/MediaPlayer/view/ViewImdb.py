import urllib.request

from PyQt5 import QtWidgets
import os
from ui.ViewImdb import Ui_View_Imdb
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class ViewImdb(QtWidgets.QWidget):
    pass_review_to_edit = pyqtSignal(object)

    def __init__(self, data):
        super(ViewImdb, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_View_Imdb()
        self.ui.setupUi(self)
        
        self.ui.value_fullTitle.setText(data["Title"])
        self.ui.value_type.setText(data["Type"])
        self.ui.value_year.setText(data["Year"])

        try:
            url_data = urllib.request.urlopen(data["Poster"]).read()
            pixmap = QPixmap()
            pixmap.loadFromData(url_data)
            self.ui.label_image.setPixmap(pixmap)
        except Exception as e:
            self.ui.label_image.setText("Invalid image")

        self.ui.value_releaseDate.setText(data["Released"])
        self.ui.value_runtimeMins.setText(data["Runtime"])
        self.ui.value_plot.setText(data["Plot"])
        self.ui.value_awards.setText(data["Awards"])
        self.ui.value_directors.setText(data["Director"])
        self.ui.value_writers.setText(data["Writer"])
        self.ui.value_stars.setText(data["Actors"])
        self.ui.value_genres.setText(data["Genre"])
        self.ui.value_boxOffice.setText(data.get('BoxOffice'))
        self.ui.value_languages.setText(data["Language"])
        self.ui.value_contentRating.setText(data["Rated"])
        self.ui.value_imdbRating.setText(data["imdbRating"])
        self.ui.value_imdbRatingVotes.setText(data["imdbVotes"])