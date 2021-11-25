from PyQt5 import QtWidgets
import os
from ui.PagePlayer import Ui_PagePlayer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from model.ModelPlaylist import ModelPlaylist
from PyQt5.QtCore import QUrl


class PagePlayer(QtWidgets.QWidget):
    def __init__(self):
        super(PagePlayer, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_PagePlayer()
        self.ui.setupUi(self)

        try:
            self.player = QMediaPlayer()
            self.playlist = QMediaPlaylist()
            self.player.setPlaylist(self.playlist)
            self.player.setVideoOutput(self.ui.mediaplayer)

            self.player.error.connect(self.errorhandler)
            self.ui.previousButton.clicked.connect(lambda: self.playlist.setCurrentIndex(self.playlist.currentIndex()-1))
            self.ui.nextButton.clicked.connect(lambda: self.playlist.setCurrentIndex(self.playlist.currentIndex()+1))
            self.ui.playButton.clicked.connect(self.player.play)
            self.ui.pauseButton.clicked.connect(self.player.pause)
            self.ui.stopButton.clicked.connect(self.player.stop)
            self.ui.volumeSlider.valueChanged.connect(self.player.setVolume)
            self.ui.timeSlider.valueChanged.connect(self.player.setPosition)
            self.player.durationChanged.connect(self.updateDuration)
            self.player.positionChanged.connect(self.updatePosition)
            self.ui.addMediaButton.clicked.connect(self.open_file)

            self.model = ModelPlaylist(self.playlist)
            self.ui.listView_playlist.setModel(self.model)
            self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
            selection_model = self.ui.listView_playlist.selectionModel()
            selection_model.selectionChanged.connect(self.playlist_selection_changed)
        except Exception as e:
            print(e)

    def open_file(self):
        try:
            path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "mp3 Audio (*.mp3);mp4 Video (*.mp4);Movie files (*.mov);All files (*.*)")

            if path:
                self.playlist.addMedia(
                    QMediaContent(
                        QUrl.fromLocalFile(path)
                    )
                )
                self.model.layoutChanged.emit()
        except Exception as e:
            print(e)

    def open_file_tree(self, filepath):
        try:
            if filepath:
                self.playlist.addMedia(
                    QMediaContent(
                        QUrl.fromLocalFile(filepath)
                    )
                )
                self.model.layoutChanged.emit()
        except Exception as e:
            print(e)

    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.ui.listView_playlist.setCurrentIndex(ix)

    def errorhandler(self):
        pass

    def updateDuration(self, duration):
        self.ui.timeSlider.setMaximum(duration)

        if duration > 0:
            self.ui.totalTimeLabel.setText(self.hhmmss(duration))

    def updatePosition(self, position):
        if position >= 0:
            self.ui.currentTimeLabel.setText(self.hhmmss(position))

        self.ui.timeSlider.blockSignals(True)
        self.ui.timeSlider.setValue(position)
        self.ui.timeSlider.blockSignals(False)

    def hhmmss(self, ms):
        # s = 1000
        # m = 60000
        # h = 3600000
        s = round(ms / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))
