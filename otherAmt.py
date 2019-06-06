from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class OtherAmt(QWidget):

    cashed = pyqtSignal()

    def __init__(self, parent):
        super(OtherAmt, self).__init__(parent)

        self.baba = parent

        self.amount = ""

        self.initUI(parent)

    def initUI(self, parent):
        parent.infoDisp.setText("Enter the amount in denominations of 1000")
        parent.resultDisp.setVisible(True)
        parent.resultDisp.setText("0000.00")

    def keyPressEvent(self, event):
        if Qt.Key_0 <= event.key() <= Qt.Key_9:
            if len(self.amount) < 5:
                self.amount+=event.text()
                self.baba.resultDisp.setText(self.amount)
        elif event.key() in self.baba.otherKeys:
            if event.key() == Qt.Key_Enter:
                if (float(self.amount) % 1000) > 0.0:
                    self.baba.resultDisp.setText("Enter amount in denomination of 1000")
                    self.amount = ""
                    self.baba.resultDisp.setText("0000.00")
                else:
                    self.cashed.emit()
            elif event.key() == Qt.Key_Plus:
                self.amount = ""
                self.baba.resultDisp.setText("0000.00")
            elif event.key() == Qt.Key_Cancel:
                self.baba.reset()
