import sys
import os
from PyQt5 import QtWidgets, uic

__dir__ = os.path.dirname(__file__)

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi(__dir__ + "/mainwindow.ui")
window.show()
app.exec()
