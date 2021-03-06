# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1332, 636)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.timeSlider = QtWidgets.QSlider(Form)
        self.timeSlider.setGeometry(QtCore.QRect(230, 580, 1081, 22))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(20, 10, 131, 41))
        self.loadButton.setObjectName("loadButton")
        self.videoInformation = QtWidgets.QTextBrowser(Form)
        self.videoInformation.setGeometry(QtCore.QRect(160, 10, 1151, 41))
        self.videoInformation.setStyleSheet("")
        self.videoInformation.setObjectName("videoInformation")
        self.colorView = QtWidgets.QGraphicsView(Form)
        self.colorView.setGeometry(QtCore.QRect(20, 60, 642, 482))
        self.colorView.setObjectName("colorView")
        self.dephView = QtWidgets.QGraphicsView(Form)
        self.dephView.setGeometry(QtCore.QRect(670, 60, 642, 482))
        self.dephView.setObjectName("dephView")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 560, 191, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.previousFrameButton = QtWidgets.QPushButton(self.splitter)
        self.previousFrameButton.setStyleSheet("border-image: url(:/icons/back.png);")
        self.previousFrameButton.setText("")
        self.previousFrameButton.setObjectName("previousFrameButton")
        self.playButton = QtWidgets.QPushButton(self.splitter)
        self.playButton.setStyleSheet("border-image: url(:/icons/play.png);")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.nextFrameButton = QtWidgets.QPushButton(self.splitter)
        self.nextFrameButton.setStyleSheet("border-image: url(:/icons/next.png);")
        self.nextFrameButton.setText("")
        self.nextFrameButton.setObjectName("nextFrameButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loadButton.setText(_translate("Form", "Load"))
from ui import images_rc
