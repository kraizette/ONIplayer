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
        self.interface = interface

        # interface = Ui_Form() #experemental

        self.setFixedSize(self.size())

        self.setWindowTitle("ONI Player")

        self.configureLoadButton()

        self.configurePlayButton()


        self.show()

    def configureLoadButton(self):
        self.interface.loadButton.clicked.connect(self.loadfile)

    def configurePlayButton(self):
        self.interface.playButton.setEnabled(False)


    def loadfile(self):
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video")
        self.interface.videoInformation.setText(filename)

        # if filename != '':
        #     self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        #     self.playBtn.setEnabled(True)
