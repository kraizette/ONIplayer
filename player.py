from PyQt5 import QtWidgets, QtGui
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl

from ui.interface import Ui_Form
from oniconverter import getVideo

class Player(QtWidgets.QWidget):
    def __init__(self, interface):
        super().__init__()
        interface.setupUi(self)

        # interface = Ui_Form() #experemental


        self.interface = interface

        self.tick = 0

        self.pause = True

        self.setFixedSize(self.size())

        self.setWindowTitle("ONI Player")

        self.configureLoadButton()

        self.configurePlayButton()

        self.configureNextButton()

        self.configurePreviousButton()


        scene = QtWidgets.QGraphicsScene()
        self.pixmap = QtWidgets.QGraphicsPixmapItem()
        scene.addItem(self.pixmap)
        interface.colorView.setScene(scene)


        scene2 = QtWidgets.QGraphicsScene()
        self.pixmap2 = QtWidgets.QGraphicsPixmapItem()
        scene2.addItem(self.pixmap2)
        interface.dephView.setScene(scene2)

        self.framesColor = []
        self.framesDepth = []
        self.framesColor.clear()
        self.framesDepth.clear()
        self.framesColor, self.framesDepth = getVideo()

        self.play()

        self.show()

    def configureLoadButton(self):
        self.interface.loadButton.clicked.connect(self.loadfile)

    def configurePlayButton(self):
        self.interface.playButton.setEnabled(False)
        self.interface.playButton.clicked.connect(self.playevent)

    def configureNextButton(self):
        self.interface.nextFrameButton.setEnabled(False)

    def configurePreviousButton(self):
        self.interface.previousFrameButton.setEnabled(False)

    def loadfile(self):
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video")
        self.interface.videoInformation.setText(filename)
        self.interface.playButton.setEnabled(True)
        self.interface.nextFrameButton.setEnabled(True)
        self.interface.previousFrameButton.setEnabled(True)

    def playevent(self):
        if self.pause == True:
            self.interface.playButton.setText("Pause")
            self.pause = False
            self.interface.nextFrameButton.setEnabled(False)
            self.interface.previousFrameButton.setEnabled(False)

        else:
            self.interface.playButton.setText("Play")
            self.pause = True
            self.interface.nextFrameButton.setEnabled(True)
            self.interface.previousFrameButton.setEnabled(True)

    def play(self):
        if self.tick >= len(self.framesColor):
            self.tick = 0
        input_image = self.framesColor[self.tick]
        input_depth = self.framesDepth[self.tick]
        bytesPerLine = 3 * 640
        y = self.interface.colorView.height()
        x = self.interface.colorView.width()
        qImg = QtGui.QImage(input_image.data, x, y, bytesPerLine, QtGui.QImage.Format_RGB888)
        qImg2 = QtGui.QImage(input_depth.data, x, y, bytesPerLine, QtGui.QImage.Format_Indexed8)
        pixmap01 = QtGui.QPixmap.fromImage(qImg)
        pixmap02 = QtGui.QPixmap.fromImage(qImg2)
        self.tick += 1
        self.pixmap2.setPixmap(pixmap02)
        self.pixmap.setPixmap(pixmap01)

        # if filename != '':
        #     self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        #     self.playBtn.setEnabled(True)
