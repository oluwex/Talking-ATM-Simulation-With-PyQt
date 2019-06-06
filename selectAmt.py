__author__ = 'habeeb'

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class SelectAmt(QWidget):

    amt500 = pyqtSignal()
    amt1000 = pyqtSignal()
    amt3000 = pyqtSignal()
    amt10k = pyqtSignal()
    amt15k = pyqtSignal()
    amt20k = pyqtSignal()
    other = pyqtSignal()

    def __init__(self, parent):
        super(SelectAmt, self).__init__(parent)

        self.initUI(parent)

    def initUI(self, parent):
        parent.infoDisp.setText("Select an amount")
        parent.option_1.setText("500")
        parent.option_2.setText("1000")
        parent.option_3.setText("3000")
        parent.option_4.setText("5000")
        parent.option_5.setText("10000")
        parent.option_6.setText("15000")
        parent.option_7.setText("20000")
        parent.option_8.setText("Other")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_8:
            self.other.emit()