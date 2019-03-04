# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(795, 484)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.emergGB = QtGui.QGroupBox(self.centralwidget)
        self.emergGB.setGeometry(QtCore.QRect(420, 40, 341, 301))
        self.emergGB.setObjectName(_fromUtf8("emergGB"))
        self.eStopBN = QtGui.QPushButton(self.emergGB)
        self.eStopBN.setGeometry(QtCore.QRect(50, 90, 251, 81))
        self.eStopBN.setObjectName(_fromUtf8("eStopBN"))
        self.sResetBN = QtGui.QPushButton(self.emergGB)
        self.sResetBN.setGeometry(QtCore.QRect(50, 180, 251, 81))
        self.sResetBN.setObjectName(_fromUtf8("sResetBN"))
        self.motorGB = QtGui.QGroupBox(self.centralwidget)
        self.motorGB.setGeometry(QtCore.QRect(40, 40, 341, 401))
        self.motorGB.setObjectName(_fromUtf8("motorGB"))
        self.speedBar = QtGui.QScrollBar(self.motorGB)
        self.speedBar.setGeometry(QtCore.QRect(40, 120, 241, 31))
        self.speedBar.setOrientation(QtCore.Qt.Horizontal)
        self.speedBar.setObjectName(_fromUtf8("speedBar"))
        self.label = QtGui.QLabel(self.motorGB)
        self.label.setGeometry(QtCore.QRect(20, 70, 291, 34))
        self.label.setObjectName(_fromUtf8("label"))
        self.sMotorBN = QtGui.QPushButton(self.motorGB)
        self.sMotorBN.setGeometry(QtCore.QRect(40, 280, 251, 81))
        self.sMotorBN.setObjectName(_fromUtf8("sMotorBN"))
        self.cwBN = QtGui.QPushButton(self.motorGB)
        self.cwBN.setGeometry(QtCore.QRect(40, 180, 121, 91))
        self.cwBN.setObjectName(_fromUtf8("cwBN"))
        self.ccwBN = QtGui.QPushButton(self.motorGB)
        self.ccwBN.setGeometry(QtCore.QRect(170, 180, 121, 91))
        self.ccwBN.setObjectName(_fromUtf8("ccwBN"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Motor Control", None))
        self.emergGB.setTitle(_translate("MainWindow", "Emergency Control", None))
        self.eStopBN.setText(_translate("MainWindow", "Emergency Stop", None))
        self.sResetBN.setText(_translate("MainWindow", "System Reset", None))
        self.motorGB.setTitle(_translate("MainWindow", "Motor Control", None))
        self.label.setText(_translate("MainWindow", "Motor Speed: 0%", None))
        self.sMotorBN.setText(_translate("MainWindow", "Start Motor", None))
        self.cwBN.setText(_translate("MainWindow", "CW", None))
        self.ccwBN.setText(_translate("MainWindow", "CCW", None))

