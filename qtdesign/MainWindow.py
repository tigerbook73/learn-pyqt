# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 654)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setBaseSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.picture = QtWidgets.QLabel(self.splitter)
        self.picture.setEnabled(True)
        self.picture.setMaximumSize(QtCore.QSize(400, 800))
        self.picture.setBaseSize(QtCore.QSize(800, 600))
        self.picture.setFrameShape(QtWidgets.QFrame.Box)
        self.picture.setFrameShadow(QtWidgets.QFrame.Plain)
        self.picture.setLineWidth(2)
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.description = QtWidgets.QPlainTextEdit(self.splitter)
        self.description.setFrameShape(QtWidgets.QFrame.Box)
        self.description.setFrameShadow(QtWidgets.QFrame.Plain)
        self.description.setLineWidth(2)
        self.description.setObjectName("description")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.picture.setText(_translate("MainWindow", "Picture"))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", "="))
        self.pushButton_3.setText(_translate("MainWindow", ">"))