from tkinter import *
import LabJackPython
import ue9

# LabJack initialation
# myUE9 = ue9.UE9(ethernet = True, ipAddress = "10.32.89.")
# myUE9.getCalibrationData()

form = Tk()
form.title('Motor Control System')
form.geometry("511x231")
form.resizable(0,0)

# label creation
label1 = Label(form, text = "Motor Speed:")
label2 = Label(form, text = "0 %")
label3 = Label(form, text = "Motor Direction:")

# button creation
updateButton = Button(form, text = "Update Settings", height = 52, width = 280)
stopButton = Button(form, text = "Emergency Stop", height = 52, width = 280)
cwButton = Button(form, text = "Clockwise", height = 52, width = 138)
ccwButton = Button(form, text = "Counter Clockwise", height = 52, width = 138)

# slider creation
speedSlider = Scale(form, from_ = 0, to = 100, orient = HORIZONTAL)

# UI layout

form.mainloop()