from tkinter import *
import tkinter.messagebox
import LabJackPython
import ue9

class PythonMotorControl:
    # variables
    motorDirection = True # states refer to Clockwise(True) and Counter Clockwise(False)
    dutyCycle = 0 # duty cycle is stored so that motor information can be displayed on the GUI
    timeValue = 0

    def __init__(self, master):
        self.master = form
        form.title('Motor Control System')
        form.geometry("511x231")
        form.resizable(0,0)
        
        self.dutyCycleLB = Label(form, text = "Desired Duty Cycle:")
        self.dutyCyclePercentLB = Label(form, text = "0 %")
        self.directionLB = Label(form, text = "Motor Direction:")
        self.updateButton = Button(form, text = "Update Settings", height = 3, width = 35)
        self.stopButton = Button(form, text = "Emergency Stop", height = 3, width = 35)
        self.cwButton = Button(form, text = "Clockwise", height = 3, width = 20, state = DISABLED, command = self.toggleDirectionButtons)
        self.ccwButton = Button(form, text = "Counter Clockwise", height = 3, width = 20, command = self.toggleDirectionButtons)
        self.speedSlider = Scale(form, from_ = 0, to = 100, orient = HORIZONTAL, showvalue = 0, length = 200, command = self.updateDutyCyleLB)

        # UI layout
        self.dutyCycleLB.grid()
        self.dutyCycleLB.place(x = 11, y = 17)
        self.dutyCyclePercentLB.grid()
        self.dutyCyclePercentLB.place(x = 120, y = 17)
        self.directionLB.grid()
        self.directionLB.place(x = 325, y = 17)
        self.updateButton.grid()
        self.updateButton.place(x = 26, y = 102)
        self.stopButton.grid()
        self.stopButton.place(x = 26, y = 158)
        self.cwButton.grid()
        self.cwButton.place(x = 335, y = 46)
        self.ccwButton.grid()
        self.ccwButton.place(x = 335, y = 102)
        self.speedSlider.grid()
        self.speedSlider.place(x = 50, y = 46)
    
    def updateDutyCyleLB(self, var): # var is the value of the slider that is given when the slider is moved
        self.dutyCyclePercentLB['text'] = str(var) + " %"

    # toggles the directional buttons's state so that each button cannot be pressed more than once
    def toggleDirectionButtons(self):
        if self.motorDirection:
            self.cwButton['state'] = NORMAL
            self.ccwButton['state'] = DISABLED
            self.motorDirection = False
        else:
            self.ccwButton['state'] = NORMAL
            self.cwButton['state'] = DISABLED
            self.motorDirection = True

    # prompts the user if the onboard stop is pressed
    def manualResetPressed(self):
        tkinter.messagebox.showinfo("Attention", "Manual reset has been attempted")

if __name__ == "__main__":  
    form = Tk()
    PythonMotorControl(form)
    form.mainloop()

    """
    # LabJack initialation
    myUE9 = ue9.UE9(ethernet = True, ipAddress = "10.32.89.110")
    myUE9.getCalibrationData()
    myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 52000)
    """