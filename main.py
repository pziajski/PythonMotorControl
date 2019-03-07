from tkinter import *
import LabJackPython
import ue9

# LabJack initialation
# myUE9 = ue9.UE9(ethernet = True, ipAddress = "10.32.89.")
# myUE9.getCalibrationData()

# state variables

# states include True(Clockwise) and False(Counter Clockwise)
motorDirection = True

# functions
def updateSetSpeedLB(var):
    setPercentLB['text'] = str(speedSlider.get()) + " %"

def toggleDirectionButtons():
    global motorDirection
    if motorDirection:
        cwButton['state'] = NORMAL
        ccwButton['state'] = DISABLED
        motorDirection = False
    else:
        ccwButton['state'] = NORMAL
        cwButton['state'] = DISABLED
        motorDirection = True

# form creation and details
form = Tk()
form.title('Motor Control System')
form.geometry("511x231")
form.resizable(0,0)

# label creation
curSpeedLB = Label(form, text = "Current Motor Speed:")
setSpeedLB = Label(form, text = "Set Motor Speed:")
curPercentLB = Label(form, text = "0 %")
setPercentLB = Label(form, text = "0 %")
directionLB = Label(form, text = "Motor Direction:")

# button creation
updateButton = Button(form, text = "Update Settings", height = 3, width = 35)
stopButton = Button(form, text = "Emergency Stop", height = 3, width = 35)
cwButton = Button(form, text = "Clockwise", height = 3, width = 20, state = DISABLED, command = toggleDirectionButtons)
ccwButton = Button(form, text = "Counter Clockwise", height = 3, width = 20, command = toggleDirectionButtons)

# slider creation
speedSlider = Scale(form, from_ = 0, to = 100, orient = HORIZONTAL, showvalue = 0, length = 200, command = updateSetSpeedLB)

# UI layout
curSpeedLB.grid()
curSpeedLB.place(x = 11, y = 17)

curPercentLB.grid()
curPercentLB.place(x = 130, y = 17)

setSpeedLB.grid()
setSpeedLB.place(x = 180, y = 17)

setPercentLB.grid()
setPercentLB.place(x = 274, y = 17)

directionLB.grid()
directionLB.place(x = 325, y = 17)

updateButton.grid()
updateButton.place(x = 26, y = 102)

stopButton.grid()
stopButton.place(x = 26, y = 158)

cwButton.grid()
cwButton.place(x = 335, y = 46)

ccwButton.grid()
ccwButton.place(x = 335, y = 102)

speedSlider.grid()
speedSlider.place(x = 50, y = 46)

form.mainloop()