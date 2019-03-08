from tkinter import *
import tkinter.messagebox
import LabJackPython
import ue9

# functions
def calcTimeValue(duty, time):
    time = ((duty * 65536) / 100) - 65536

def updateDutyCyleLB(duty):
    dutyCyclePercentLB['text'] = str(speedSlider.get()) + " %"
    duty = speedSlider.get()

def toggleDirectionButtons(var):
    if var:
        cwButton['state'] = NORMAL
        ccwButton['state'] = DISABLED
        var = False
    else:
        ccwButton['state'] = NORMAL
        cwButton['state'] = DISABLED
        var = True

def manualResetPressed():
    tkinter.messagebox.showinfo("Attention", "Manual reset has been attempted")

if __name__ == "__main__":
    # variables
    motorDirection = True # states refer to Clockwise(True) and Counter Clockwise(False)
    dutyCycle = 0
    timeValue = 0
    
    # form creation and details
    form = Tk()
    form.title('Motor Control System')
    form.geometry("511x231")
    form.resizable(0,0)

    # UI elements
    dutyCycleLB = Label(form, text = "Desired Duty Cycle:")
    dutyCyclePercentLB = Label(form, text = "0 %")
    directionLB = Label(form, text = "Motor Direction:")
    updateButton = Button(form, text = "Update Settings", height = 3, width = 35)
    stopButton = Button(form, text = "Emergency Stop", height = 3, width = 35)
    cwButton = Button(form, text = "Clockwise", height = 3, width = 20, state = DISABLED, command = toggleDirectionButtons(motorDirection))
    ccwButton = Button(form, text = "Counter Clockwise", height = 3, width = 20, command = toggleDirectionButtons(motorDirection))
    speedSlider = Scale(form, from_ = 0, to = 100, orient = HORIZONTAL, showvalue = 0, length = 200, command = updateDutyCyleLB(dutyCycle))

    # UI layout
    dutyCycleLB.grid()
    dutyCycleLB.place(x = 11, y = 17)
    dutyCyclePercentLB.grid()
    dutyCyclePercentLB.place(x = 120, y = 17)
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

    """
    # LabJack initialation
    myUE9 = ue9.UE9(ethernet = True, ipAddress = "10.32.89.110")
    myUE9.getCalibrationData()
    myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 52000)
    """

    form.mainloop()