from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        self.setMinimumWidth(100)
        self.setMinimumHeight(100)


# Subclass QMainWindow to customise your application's main window


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("2048")

        masterArea = QVBoxLayout()
        cmdArea = QHBoxLayout()

        boxArea = Color("gray")
        boxArea.setFixedWidth(500)
        boxArea.setFixedHeight(500)

        masterArea.setStretchFactor()
        masterArea.addLayout(cmdArea)
        masterArea.addWidget(boxArea)

        cmdArea.addWidget(QLabel("Score: "))
        cmdArea.addWidget(QLabel("1024"))
        cmdArea.addWidget(QPushButton("New Game"))

        self.size = 4

        # for row in range(self.size):
        #     for column in range(self.size):
        #         boxArea.addWidget(Color("red"))

        # masterArea.addLayout(cmdArea)
        # masterArea.setContentsMargins(0, 0, 0, 0)
        # masterArea.setSpacing(20)

        # masterArea.addWidget(Color("green"))

        widget = QWidget()
        # widget.setFixedWidth(500)
        # widget.setFixedHeight(500)
        widget.setLayout(masterArea)
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()


# Your application won't reach here until you exit and the event
# loop has stopped.
