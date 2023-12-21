## NOTES ##
'''

'''

## DEPENDENCIES ## 

import pyVFD
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
		micro = '0'
	else:
		micro = microseconds

	disp_hr1.clear()
	disp_hr2.clear()
	disp_min1.clear()
	disp_min2.clear()
	disp_sec1.clear()
	disp_sec2.clear()
	disp_micro.clear()

	disp_hr1.char(hr1).pack(side=tk.LEFT)
	disp_hr2.char(hr2, CC=1).pack(side=tk.LEFT)
	disp_min1.char(min1).pack(side=tk.LEFT)
	disp_min2.char(min2, CC=1).pack(side=tk.LEFT)
	disp_sec1.char(sec1).pack(side=tk.LEFT)
	disp_sec2.char(sec2, DP=1).pack(side=tk.LEFT)
	disp_micro.char(micro).pack(side=tk.LEFT)

	root.after(100, example_routine)

## EXECUTABLE ## 

root = tk.Tk()
root.title('pyVFD Example')

global_height=200

disp_hr1 = pyVFD.seg7(root, height=global_height)
disp_hr2 = pyVFD.seg7(root, height=global_height, use_CC=True)
disp_min1 = pyVFD.seg7(root, height=global_height)
disp_min2 = pyVFD.seg7(root, height=global_height, use_CC=True)
disp_sec1 = pyVFD.seg7(root, height=global_height)
disp_sec2 = pyVFD.seg7(root, height=global_height, use_DP=True)
disp_micro = pyVFD.seg7(root, height=global_height)

disp_hr1.char('off').pack(side=tk.LEFT)
disp_hr2.char('off').pack(side=tk.LEFT)
disp_min1.char('off').pack(side=tk.LEFT)
disp_min2.char('off').pack(side=tk.LEFT)
disp_sec1.char('off').pack(side=tk.LEFT)
disp_sec2.char('off').pack(side=tk.LEFT)
disp_micro.char('off').pack(side=tk.LEFT)

example_routine()

root.mainloop()

