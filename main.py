import sys
import enterPin, homeMenu, withdraw, selectAmt, otherAmt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from ui_files import mainFrame

class Main(QMainWindow, mainFrame.Ui_MainWindow):

    opt_0 = pyqtSignal()
    opt_1 = pyqtSignal()
    opt_2 = pyqtSignal()
    opt_3 = pyqtSignal()
    opt_4 = pyqtSignal()
    opt_5 = pyqtSignal()
    opt_6 = pyqtSignal()
    opt_7 = pyqtSignal()
    opt_8 = pyqtSignal()

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.otherKeys = [Qt.Key_Enter,Qt.Key_Plus,Qt.Key_Minus]
        self._state = 0

        self.reset()
        #self.opt_1.connect(self.on_btn_1_clicked)
        #self.opt_2.connect(self.on_btn_2_clicked)
        #self.opt_3.connect(self.on_btn_3_clicked)
        #self.opt_4.connect(self.on_btn_4_clicked)
        #self.opt_5.connect(self.on_btn_5_clicked)
        #self.opt_6.connect(self.on_btn_5_clicked)
        #self.opt_7.connect(self.on_btn_7_clicked)
        #self.opt_8.connect(self.on_btn_8_clicked)
        #self.opt_0.connect(self.on_btn_0_clicked)

        #self.passwordLine.setAttribute(Qt.WA_TranslucentBackground)

    def clearUI(self):
        for item in self.findChildren(QLabel):
            item.clear()

    def askPin(self):
        self.clearUI()
        self.wid = enterPin.EnterPin(self)
        self.wid._userPass[str].connect(self.checkPass)
        #qApp.setActiveWindow(wid)
        self.wid.grabKeyboard()

    def showHome(self):
        self.clearUI()
        self.home = homeMenu.Menu(self)
        self.home.withdraw.connect(self.withdraw)
        #self.home.inquiry.connect(self.inquiry)
        #self.home.changePin.connect(self.changePin)
        #self.home.rechargeAcc.connect(self.rechargeAcc)
        self.home.grabKeyboard()
        self._state = 1

    def wait(self):
        time = QTimer()
        if self._state == 0:
            time.singleShot(4000, self.showHome)
        self.clearUI()
        self.infoDisp.setText("Please wait while your transaction is processing")

    def reset(self):
        self.setupUi(self)
        self.pinLine.setHidden(True)
        self.pinLabel.setVisible(False)
        self.frame.grabKeyboard()

    def State1(self):
        if self._state == 1:
            for child in self.frame.children():
                child.clear()
            self.option_5.setText("Withdraw")
            self.option_6.setText("Inquiry")
            self.option_7.setText("Change PIN")
            self.option_8.setText("Recharge account")

    def keyPressEvent(self, event):
        if Qt.Key_0 <= event.key() <= Qt.Key_9 or event.key() in self.otherKeys:
            if self._state == 0:
                self.askPin()
            """self.key = event.key()
            if self.key == Qt.Key_1:
                self.opt_1.emit()
            elif self.key == Qt.Key_2:
                self.opt_2.emit()
            elif self.key == Qt.Key_3:
                self.opt_3.emit()
            elif self.key == Qt.Key_4:
                self.opt_4.emit()
            elif self.key == Qt.Key_5:
                self.opt_5.emit()
            elif self.key == Qt.Key_7:
                self.opt_7.emit()
            elif self.key == Qt.Key_7:
                self.opt_7.emit()
            elif self.key == Qt.Key_8:
                self.opt_8.emit()
            elif self.key == Qt.Key_0:
                self.opt_0.emit()"""


    @pyqtSlot(str)
    def checkPass(self, password):
        self.wid.destroy(True)
        self.clearUI()
        if password == "1234":
            self.wait()

    @pyqtSlot()
    def withdraw(self):
        self.home.destroy(True)
        self.clearUI()
        self.withdraw = withdraw.Withdraw(self)
        self.withdraw.accountType.connect(self.chooseAmt)
        self.withdraw.grabKeyboard()

    @pyqtSlot()
    def chooseAmt(self):
        self.withdraw.destroy(True)
        self.clearUI()
        self.select = selectAmt.SelectAmt(self)
        self.select.other.connect(self.showOther)
        self.select.grabKeyboard()

    @pyqtSlot()
    def showOther(self):
        self.select.destroy(True)
        self.clearUI()
        self.resultDisp.setText("dafdadfa")
        self.otherAmtView = otherAmt.OtherAmt(self)
        self.otherAmtView.grabKeyboard()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()