## NOTES ##
'''

'''

## DEPENDENCIES ## 
# import pyVFD
from pyVFD import * # !!!!! Change this
import tkinter as tk
import datetime
import time

## DEFINITIONS ##

def example_routine():
	current = datetime.datetime.now()
	hours = str(current.hour)
	minutes = str(current.minute)
	seconds = str(current.second)
	microseconds = str(round(current.microsecond*10**-5))

	if len(hours) == 1:
		hr1 = '0'
		hr2 = hours
	else:
		hr1 = hours[0]
		hr2 = hours[1]

	if len(minutes) == 1:
		min1 = '0'
		min2 = minutes
	else:
		min1 = minutes[0]
		min2 = minutes[1]

	if len(seconds) == 1:
		sec1 = '0'
		sec2 = seconds
	else:
		sec1 = seconds[0]
		sec2 = seconds[1]

	if microseconds == '10':
		micro = 0
	else:
		micro = microseconds

	dhr1.clear()
	dhr2.clear()
	dmin1.clear()
	dmin2.clear()
	dsec1.clear()
	dsec2.clear()
	dmicro.clear()

	dhr1.char(hr1).pack(side=tk.LEFT)
	dhr2.char(hr2).pack(side=tk.LEFT)
	dmin1.char(min1).pack(side=tk.LEFT)
	dmin2.char(min2).pack(side=tk.LEFT)
	dsec1.char(sec1).pack(side=tk.LEFT)
	dsec2.char(sec2).pack(side=tk.LEFT)
	dmicro.char(micro).pack(side=tk.LEFT)

	root.after(100, function=example_routine())


## EXECUTABLE ## 

root = tk.Tk()
root.title('pyVFD Example')

# pyVFD.resize(0.09)

dhr1 = pyVFD(root)
dhr2 = pyVFD(root)
dmin1 = pyVFD(root)
dmin2 = pyVFD(root)
dsec1 = pyVFD(root)
dsec2 = pyVFD(root)
dmicro = pyVFD(root)

dhr1.char('off').pack(side=tk.LEFT)
dhr2.char('off').pack(side=tk.LEFT)
dmin1.char('off').pack(side=tk.LEFT)
dmin2.char('off').pack(side=tk.LEFT)
dsec1.char('off').pack(side=tk.LEFT)
dsec2.char('off').pack(side=tk.LEFT)
dmicro.char('off').pack(side=tk.LEFT)

example_routine()

root.mainloop()


