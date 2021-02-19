import sys
from PyQt5 import QtWidgets, uic, QtGui

from qtdesign.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        transform = QtGui.QTransform().rotate(-90)
        pixmap = QtGui.QPixmap("IMG_1.jpg")
        pixmap = pixmap.transformed(transform)
        self.picture.setScaledContents(True)
        self.picture.setPixmap(pixmap)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
