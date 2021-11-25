import PyQt5
from PyQt5.QtCore import QAbstractListModel, Qt

class ModelPlaylist(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(ModelPlaylist, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()