from PyQt5 import QtWidgets, uic, QtCore
import os
from ui.PageFileTree import Ui_PageFileTree
from PyQt5.QtCore import pyqtSignal


class PageFileTree(QtWidgets.QWidget):
    pass_file_path = QtCore.pyqtSignal(str)
    pass_imdb_search_file = pyqtSignal(str)

    def __init__(self):
        super(PageFileTree, self).__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.ui = Ui_PageFileTree()
        self.ui.setupUi(self)

        self.ui.button_searchImDb.clicked.connect(self.searchOnImDb)

        # Filters
        self.filters = ['*.mp3', '*.mp4', '*.wav', '*.ogg', '*.flac', '*.mov']

        # Configure Model
        self.model = QtWidgets.QFileSystemModel()
        self.model.setNameFilters(self.filters)
        self.model.setNameFilterDisables(False)
        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        self.model.setRootPath('')
        self.ui.treeView_files.setModel(self.model)

        # Hide headers and columns
        for i in range(1, self.ui.treeView_files.model().columnCount()):
            self.ui.treeView_files.header().hideSection(i)

        self.ui.treeView_files.header().hide()

        # signals and slots
        self.ui.treeView_files.doubleClicked.connect(self.OnTreeViewDoubleClicked)

    def OnTreeViewDoubleClicked(self, qmi):
        if not self.model.hasChildren(qmi):
            self.pass_file_path.emit(self.model.filePath(qmi))

    def searchOnImDb(self):
        qmi = self.ui.treeView_files.selectionModel().selectedIndexes()[0]
        file_name = os.path.basename(self.model.filePath(qmi))
        self.pass_imdb_search_file.emit(file_name)

