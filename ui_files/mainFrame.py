# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\ATM\ui_files\mainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 628)
        MainWindow.setStyleSheet("QFrame{\n"
"background-color: ;\n"
"font-family: calibri;\n"
"color: yellow;\n"
"font-size: 25px\n"
"/*border: 1px solid;\n"
"border-radius: 20px;*/\n"
"}\n"
"\n"
"QLabel{\n"
"border:1px solid;\n"
"border-radius: none;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: none\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 40, 701, 531))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(3)
        self.frame.setObjectName("frame")
        self.infoDisp = QtWidgets.QLabel(self.frame)
        self.infoDisp.setGeometry(QtCore.QRect(46, 10, 611, 111))
        self.infoDisp.setText("")
        self.infoDisp.setTextFormat(QtCore.Qt.RichText)
        self.infoDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.infoDisp.setWordWrap(True)
        self.infoDisp.setObjectName("infoDisp")
        self.resultDisp = QtWidgets.QLabel(self.frame)
        self.resultDisp.setGeometry(QtCore.QRect(160, 160, 401, 81))
        self.resultDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.resultDisp.setObjectName("resultDisp")
        self.option_1 = QtWidgets.QLabel(self.frame)
        self.option_1.setGeometry(QtCore.QRect(0, 150, 251, 51))
        self.option_1.setTextFormat(QtCore.Qt.RichText)
        self.option_1.setObjectName("option_1")
        self.option_5 = QtWidgets.QLabel(self.frame)
        self.option_5.setGeometry(QtCore.QRect(450, 150, 251, 51))
        self.option_5.setTextFormat(QtCore.Qt.RichText)
        self.option_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.option_5.setObjectName("option_5")
        self.option_6 = QtWidgets.QLabel(self.frame)
        self.option_6.setGeometry(QtCore.QRect(450, 250, 251, 51))
        self.option_6.setTextFormat(QtCore.Qt.RichText)
        self.option_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.option_6.setObjectName("option_6")
        self.option_7 = QtWidgets.QLabel(self.frame)
        self.option_7.setGeometry(QtCore.QRect(450, 350, 251, 51))
        self.option_7.setTextFormat(QtCore.Qt.RichText)
        self.option_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.option_7.setObjectName("option_7")
        self.option_8 = QtWidgets.QLabel(self.frame)
        self.option_8.setGeometry(QtCore.QRect(450, 450, 251, 51))
        self.option_8.setTextFormat(QtCore.Qt.RichText)
        self.option_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.option_8.setObjectName("option_8")
        self.option_2 = QtWidgets.QLabel(self.frame)
        self.option_2.setGeometry(QtCore.QRect(0, 250, 251, 51))
        self.option_2.setTextFormat(QtCore.Qt.RichText)
        self.option_2.setObjectName("option_2")
        self.option_3 = QtWidgets.QLabel(self.frame)
        self.option_3.setGeometry(QtCore.QRect(0, 350, 251, 51))
        self.option_3.setTextFormat(QtCore.Qt.RichText)
        self.option_3.setObjectName("option_3")
        self.option_4 = QtWidgets.QLabel(self.frame)
        self.option_4.setGeometry(QtCore.QRect(0, 450, 251, 51))
        self.option_4.setTextFormat(QtCore.Qt.RichText)
        self.option_4.setObjectName("option_4")
        self.pinLabel = QtWidgets.QLabel(self.frame)
        self.pinLabel.setGeometry(QtCore.QRect(54, 381, 211, 81))
        self.pinLabel.setText("")
        self.pinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pinLabel.setObjectName("pinLabel")
        self.pinLine = QtWidgets.QLabel(self.frame)
        self.pinLine.setEnabled(False)
        self.pinLine.setGeometry(QtCore.QRect(270, 390, 211, 71))
        self.pinLine.setText("")
        self.pinLine.setObjectName("pinLine")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(60, 170, 81, 81))
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(60, 270, 81, 81))
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(60, 370, 81, 81))
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(60, 470, 81, 81))
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(900, 170, 81, 81))
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(900, 270, 81, 81))
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(900, 370, 81, 81))
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(900, 470, 81, 81))
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resultDisp.setText(_translate("MainWindow", "Please insert card to start transaction"))
        self.option_1.setText(_translate("MainWindow", "1"))
        self.option_5.setText(_translate("MainWindow", "5"))
        self.option_6.setText(_translate("MainWindow", "6"))
        self.option_7.setText(_translate("MainWindow", "7"))
        self.option_8.setText(_translate("MainWindow", "8"))
        self.option_2.setText(_translate("MainWindow", "2"))
        self.option_3.setText(_translate("MainWindow", "3"))
        self.option_4.setText(_translate("MainWindow", "4"))

