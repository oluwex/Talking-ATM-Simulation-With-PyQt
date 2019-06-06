__author__ = 'habeeb'

import selectAmt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Withdraw(QWidget):

    accountType = pyqtSignal()

    def __init__(self, parent):
        super(Withdraw, self).__init__(parent)

        self.initUI(parent)

    def initUI(self, parent):
        parent.option_6.setText("Current")
        parent.option_7.setText("Savings")

    def keyPressEvent(self, event):
        if Qt.Key_0 <= event.key() <= Qt.Key_9:
            if event.key() == Qt.Key_6 or event.key() == Qt.Key_7:
                self.accountType.emit()
        elif event.key() in self.baba.otherKeys:
            if event.key() == Qt.Key_Cancel:
                self.baba.reset()
