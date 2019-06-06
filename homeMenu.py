__author__ = 'habeeb'

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Menu(QWidget):

    withdraw = pyqtSignal()
    inquiry = pyqtSignal()
    changePin = pyqtSignal()
    rechargeAcc = pyqtSignal()

    def __init__(self, parent):
        super(Menu, self).__init__(parent)

        self.baba = parent

        self.initUI(parent)

    def initUI(self, parent):
        parent.pinLabel.setVisible(False)
        parent.pinLine.setVisible(False)
        parent.option_5.setText("Withdraw")
        parent.option_6.setText("Inquiry")
        parent.option_7.setText("Change PIN")
        parent.option_8.setText("Recharge account")

    def keyPressEvent(self, event):
        if Qt.Key_0 <= event.key() <= Qt.Key_9:
            if event.key() == Qt.Key_5:
                self.withdraw.emit()
            elif event.key() == Qt.Key_6:
                self.inquiry.emit()
            elif event.key() == Qt.Key_7:
                self.changePin.emit()
            elif event.key() == Qt.Key_8:
                self.rechargeAcc.emit()
        elif event.key() in self.baba.otherKeys:
            if event.key() == Qt.Key_Cancel:
                self.baba.reset()