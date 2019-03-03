from tkinter import *
from LabJackPython import *

# variable
motorSpeed = IntVar()

# function definitions
def toggleStates():
	state = str(emrgStop['state'])
	if state == 'active':
		emrgStop.configure(state = 'disabled')
		sysReset.configure(state = 'normal')
	if state == 'disabled':
		emrgStop.configure(state = 'normal')
		sysReset.configure(state = 'disabled')

# gui initiation
form = Tk()
form.title("Motor Control System")
form.geometry("700x400")

# gui elements
emrgStop = Button(form, text = "Emergency Stop", height = 3, width = 15, command = toggleStates)
sysReset = Button(form, text = "System Reset", state = 'disabled', height = 3, width = 15, command = toggleStates)
speedScaler = Scale(form, from_= 0, to = 100, orient = HORIZONTAL, variable = motorSpeed)

# aranging elements
emrgStop.grid(row = 2, column = 1)
sysReset.grid(row = 2, column = 2)
speedScaler.grid(row = 1, column = 1)

form.mainloop()