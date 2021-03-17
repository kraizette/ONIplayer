from PyQt5 import QtWidgets
import sys
from openni import openni2

from ui.interface import Ui_Form
from player import Player


app = QtWidgets.QApplication(sys.argv)

player = QtWidgets.QWidget()

playerUI = Ui_Form()

player = Player(playerUI)

sys.exit(app.exec_())