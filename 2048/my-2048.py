from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QApplication,
)
from PyQt5.QtGui import QPalette, QColor

# Only needed for access to command line arguments
import sys
import random


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        self.setWindowTitle("he")

        if color == None:
            color = random.choice(
                (
                    "red",
                    "blue",
                    "green",
                    "orange",
                    "brown",
                    "gray",
                    "yellow",
                    "purple",
                )
            )

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        self.setMinimumWidth(10)
        self.setMinimumHeight(10)


class Box(Color):
    def __init__(self, mainWindow, *args, **kwargs):
        super(Box, self).__init__("blue", *args, **kwargs)

    def setValue(self, value):
        self.value = value


class BoxArea(Color):
    def __init__(self, mainWindow, *args, **kwargs):
        super(BoxArea, self).__init__("lightgray", *args, **kwargs)

        self.mainWindow = mainWindow

    def resizeEvent(self, a0):
        self.mainWindow.boxAreaSizeEvent(a0)

        # width, height = a0.size().width() // self.size, a0.size().height() // self.size

        # for row in range(self.size):
        #     for column in range(self.size):
        #         box = self.boxes.get((row, column))
        #         if box:
        #             box.setGeometry(QRect(row * width, column * height, width, height))

        return super().resizeEvent(a0)


# Subclass QMainWindow to customise your application's main window


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("2048")

        self.size = 5

        # main layout
        mainLayout = QVBoxLayout()

        cmdLayout = QHBoxLayout()
        self.boxArea = BoxArea(self)

        mainLayout.addLayout(cmdLayout)
        mainLayout.addWidget(boxArea)

        # cmd layout
        self.scoreLabel = QLabel("Score: ")
        self.scoreValue = QLabel("0")
        self.newGame = QPushButton("New Game")

        cmdLayout.addWidget(self.scoreLabel)
        cmdLayout.addWidget(self.scoreValue)
        cmdLayout.addWidget(self.newGame)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    def boxAreaSizeEvent(self, a0):
        width, height = a0.size().width() // self.size, a0.size().height() // self.size

        # for row in range(self.size):
        #     for column in range(self.size):
        #         box = self.boxes.get((row, column))
        #         if box:
        #             box.setGeometry(QRect(row * width, column * height, width, height))

    def initBoxes(self, size):
        self.size = size
        self.boxMatrix = {}
        self.boxes = [Box(self.boxArea) for i in range(self.size * self.size)]

    def randomPickBox(self):
        locationList = (
            (row, column)
            for column in range(self.size)
            for row in range(self.size)
            if not self.boxMatrix.get((row, column))
        )
        if not locationList:
            return False

        location = random.choice(locationList)
        box = self.boxes.pop()
        box.setValue(2)
        self.boxMatrix.set(location, box)

    def appearBox(self, box: Box, location: tuple):
        box.setValue(2)
        self.boxMatrix.set(location, box)
        self.addAnimition()

    def disappearBox(self, location):
        pass

    def addAnimition(self):
        pass


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
