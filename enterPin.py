import sys
import main
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class EnterPin(QWidget):

    _userPass = pyqtSignal(str)

    def __init__(self, parent):
        super(EnterPin, self).__init__(parent)
        self.baba = parent
        self._password = ""

        self.initUI(parent)

    def initUI(self, parent):
        parent.infoDisp.setText("Please enter your pin")
        parent.pinLabel.setVisible(True)
        parent.pinLine.setVisible(True)
        parent.pinLabel.setText("Enter your pin:")
        parent.resultDisp.setHidden(True)

    def keyPressEvent(self, event):
        if Qt.Key_0 <= event.key() <= Qt.Key_9:
            if len(self._password) < 4:
                self._password+=event.text()
                self.baba.pinLine.setText(len(self._password) * "*")
        elif event.key() in self.baba.otherKeys:
            if event.key() == Qt.Key_Enter:
                if len(self._password) == 4:
                    self._userPass.emit(self._password)
            elif event.key() == Qt.Key_Plus:
                self._password = ""
                self.baba.pinLine.clear()
            elif event.key() == Qt.Key_Minus:
                self.baba.reset()



"""def main():
    app = QApplication(sys.argv)
    win = EnterPin(None)
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()"""