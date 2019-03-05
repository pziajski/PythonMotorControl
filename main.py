import LabJackPython
import ue9
from PyQt4 import QtCore, QtGui
from gui import Ui_MainWindow

# LabJack initialation
# myUE9 = ue9.UE9(ethernet = true, ipAddress = "10.32.89.")
# myUE9.getCalibrationData()

class Window(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		# buttons
		self.ui.updateBN.clicked.connect(self.updateValues)
		# self.ui.eStopBN.clicked.connect()
		# scroll bar
		self.ui.speedBar.setMinimum(0)
		self.ui.speedBar.setMaximum(100)
		self.ui.speedBar.sliderMoved.connect(self.updateSpeedLB)
		self.ui.speedBar.sliderReleased.connect(self.updateSpeedLB)
		# rotation
		self.ui.cwBN.setEnabled(False)
		self.ui.cwBN.clicked.connect(self.changeRotation)
		self.ui.ccwBN.clicked.connect(self.changeRotation)
	
	def updateValues(self):
		self.updateSpeedLB()

	def updateSpeedLB(self):
		# updates value to label beside bar on release
		self.ui.label.setText("Motor Speed: " + str(self.ui.speedBar.value())+ "%")

	def changeRotation(self):
		if self.ui.cwBN.isEnabled():
			self.ui.cwBN.setEnabled(False)
			self.ui.ccwBN.setEnabled(True)
		else:
			self.ui.cwBN.setEnabled(True)
			self.ui.ccwBN.setEnabled(False)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())