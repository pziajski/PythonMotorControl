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
        MainWindow.resize(795, 340)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.eStopBN = QtGui.QPushButton(self.centralwidget)
        self.eStopBN.setGeometry(QtCore.QRect(50, 210, 701, 81))
        self.eStopBN.setObjectName(_fromUtf8("eStopBN"))
        self.updateBN = QtGui.QPushButton(self.centralwidget)
        self.updateBN.setGeometry(QtCore.QRect(50, 120, 341, 80))
        self.updateBN.setObjectName(_fromUtf8("updateBN"))
        self.cwBN = QtGui.QPushButton(self.centralwidget)
        self.cwBN.setGeometry(QtCore.QRect(400, 120, 171, 80))
        self.cwBN.setObjectName(_fromUtf8("cwBN"))
        self.speedBar = QtGui.QScrollBar(self.centralwidget)
        self.speedBar.setGeometry(QtCore.QRect(400, 40, 321, 34))
        self.speedBar.setOrientation(QtCore.Qt.Horizontal)
        self.speedBar.setObjectName(_fromUtf8("speedBar"))
        self.ccwBN = QtGui.QPushButton(self.centralwidget)
        self.ccwBN.setGeometry(QtCore.QRect(579, 120, 171, 80))
        self.ccwBN.setObjectName(_fromUtf8("ccwBN"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 321, 34))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Motor Control", None))
        self.eStopBN.setText(_translate("MainWindow", "Emergency Stop", None))
        self.updateBN.setText(_translate("MainWindow", "Update", None))
        self.cwBN.setText(_translate("MainWindow", "CW", None))
        self.ccwBN.setText(_translate("MainWindow", "CCW", None))
        self.label.setText(_translate("MainWindow", "Motor Speed: 0%", None))

