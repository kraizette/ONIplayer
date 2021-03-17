from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl

from ui.interface import Ui_Form

class Player(QtWidgets.QWidget):
    def __init__(self, interface):
        super().__init__()
        interface.setupUi(self)

        # interface = Ui_Form() #experemental

        self.interface = interface

        self.pause = True

        self.setFixedSize(self.size())

        self.setWindowTitle("ONI Player")

        self.configureLoadButton()

        self.configurePlayButton()

        self.configureNextButton()

        self.configurePreviousButton()

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


        # if filename != '':
        #     self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        #     self.playBtn.setEnabled(True)
