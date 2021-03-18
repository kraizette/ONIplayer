from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QBasicTimer

from ui.interface import Ui_Form
from oniconverter import getVideo

class Player(QtWidgets.QWidget):
    def __init__(self, interface):
        super().__init__()
        interface.setupUi(self)

        # interface = Ui_Form() #experemental

        self.timer = QBasicTimer()

        self.interface = interface
        self.tick = 0
        self.framesColor = []
        self.framesDepth = []
        self.filename = ''

        self.setFixedSize(self.size())
        self.setWindowTitle("ONI Player")

        self.configureLoadButton()
        self.configurePlayButton()
        self.configureNextButton()
        self.configurePreviousButton()

        self.configureTimeSlider()

        scene = QtWidgets.QGraphicsScene()
        self.pixmap = QtWidgets.QGraphicsPixmapItem()
        scene.addItem(self.pixmap)
        interface.colorView.setScene(scene)

        # scene2 = QtWidgets.QGraphicsScene()
        # self.pixmap2 = QtWidgets.QGraphicsPixmapItem()
        # scene2.addItem(self.pixmap2)
        # interface.dephView.setScene(scene2)

        self.framesColor.clear()
        # self.framesDepth.clear()

        # self.framesColor, self.framesDepth = getVideo()

        self.show()

    # ---------------------------------------------------------
    #
    # Configure
    #
    # ---------------------------------------------------------

    # Configure "Load" button
    def configureLoadButton(self) -> None:
        self.interface.loadButton.clicked.connect(self.loadEvent)

    # Configure "Play"/"Pause" button
    def configurePlayButton(self) -> None:
        self.interface.playButton.setEnabled(False)
        self.interface.playButton.clicked.connect(self.playEvent)

    # Configure "Next" button
    def configureNextButton(self) -> None:
        self.interface.nextFrameButton.setEnabled(False)
        self.interface.nextFrameButton.clicked.connect(self.nextEvent)

    # Configure "Previous" button
    def configurePreviousButton(self) -> None:
        self.interface.previousFrameButton.setEnabled(False)
        self.interface.previousFrameButton.clicked.connect(self.previousEvent)

    # Configure time slider
    def configureTimeSlider(self) -> None:
        self.interface.timeSlider.setEnabled(False)
        self.interface.timeSlider.sliderReleased.connect(self.sliderEvent)
        self.interface.timeSlider.sliderPressed.connect(self.sliderEvent)
        self.interface.timeSlider.sliderMoved.connect(self.sliderEvent)

    # ---------------------------------------------------------
    #
    # Events
    #
    # ---------------------------------------------------------

    # Event on "Load" button push
    def loadEvent(self) -> None:
        self.loadfile()
        self.interface.videoInformation.setText(self.filename)
        self.interface.playButton.setEnabled(True)
        self.interface.nextFrameButton.setEnabled(True)
        self.interface.previousFrameButton.setEnabled(True)
        self.interface.timeSlider.setEnabled(True)

        self.framesColor = [
            "1 (1).jpg", "1 (2).jpg",
            "1 (3).jpg", "1 (4).jpg",
            "1 (5).jpg", "1 (1).jpg",
            "1 (2).jpg", "1 (3).jpg",
            "1 (4).jpg", "1 (5).jpg",
            "1 (1).jpg", "1 (2).jpg",
            "1 (3).jpg", "1 (4).jpg",
            "1 (5).jpg", "1 (1).jpg",
            "1 (2).jpg", "1 (3).jpg",
            "1 (4).jpg", "1 (5).jpg",
        ]

        self.interface.timeSlider.setRange(0, len(self.framesColor) - 1)

        self.loadFrame()

    # Event on "Play"/"Pause" button push
    def playEvent(self) -> None:

        # Pause event
        if self.timer.isActive():
            self.timer.stop()
            self.interface.playButton.setStyleSheet('QPushButton{border-image:url(ui/play.png)}')
            self.interface.nextFrameButton.setEnabled(True)
            self.interface.previousFrameButton.setEnabled(True)

        # Play event
        else:
            self.interface.playButton.setStyleSheet('QPushButton{border-image:url(ui/pause.png)}')
            self.timer.start(28, self)
            self.interface.nextFrameButton.setEnabled(False)
            self.interface.previousFrameButton.setEnabled(False)
            self.tickEvent(False)
            self.loadFrame()

    # Event on "Next" button push
    def nextEvent(self) -> None:
        self.tickEvent(False)
        self.loadFrame()

    # Event on "Previous" button push
    def previousEvent(self) -> None:
        self.tickEvent(True)
        self.loadFrame()

    # Event on timer tick
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        self.tickEvent(False)
        self.loadFrame()

    # Tick change
    def tickEvent(self, reverse: bool) -> None:
        if reverse:
            self.tick -= 1
            if self.tick < 0:
                self.tick = 0
            self.interface.timeSlider.setValue(self.tick)
        else:
            self.tick += 1
            if self.tick >= len(self.framesColor):
                self.tick = 0
                self.playEvent()
            self.interface.timeSlider.setValue(self.tick)

    # Slider event
    def sliderEvent(self) -> None:
        self.tick = self.interface.timeSlider.value()
        self.loadFrame()


    # ---------------------------------------------------------
    #
    # Functions
    #
    # ---------------------------------------------------------

    # Load file from explorer
    def loadfile(self) -> None:
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video")

    # Load frame to widget
    def loadFrame(self) -> None:
        input_image = self.framesColor[self.tick]
        # input_depth = self.framesDepth[self.tick]
        bytesPerLine = 3 * 640
        y = self.interface.colorView.height()
        x = self.interface.colorView.width()
        # qImg = QtGui.QImage(input_image.data, x, y, bytesPerLine, QtGui.QImage.Format_RGB888)
        qImg = QtGui.QImage(x, y,  QtGui.QImage.Format_RGB888)
        qImg.load(self.framesColor[self.tick])
        qImg.scaled(x, y, Qt.KeepAspectRatio)
        # qImg2 = QtGui.QImage(input_depth.data, x, y, bytesPerLine, QtGui.QImage.Format_Indexed8)
        pixmap01 = QtGui.QPixmap.fromImage(qImg)
        pixmap01.scaled(x, y, Qt.IgnoreAspectRatio)
        # pixmap02 = QtGui.QPixmap.fromImage(qImg2)

        # self.pixmap2.setPixmap(pixmap02)
        self.pixmap.setPixmap(pixmap01)