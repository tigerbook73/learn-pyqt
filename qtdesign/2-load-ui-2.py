import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


__dir__ = os.path.dirname(os.path.realpath(__file__))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(__dir__ + "/mainwindow.ui", self)

        pixmap = QtGui.QPixmap(__dir__ + "/IMG_1.jpg")
        self.picture.setScaledContents(True)
        self.picture.setPixmap(pixmap)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
