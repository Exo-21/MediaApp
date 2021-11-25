import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


from view.MainWindow import MainWindow

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()


