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
	hr = str(format(current.hour, '02d'))
	mn = str(format(current.minute, '02d'))
	se = str(format(current.second, '02d'))
	mi = str(round(current.microsecond*10**-5))

	# clear display so it can be changed
	d_hr1.clear()
	d_hr2.clear()
	d_min1.clear()
	d_min2.clear()
	d_sec1.clear()
	d_sec2.clear()
	d_mic.clear()

	# update and pack display into root
	d_hr1.char(hr[0]).pack(side=tk.LEFT)
	d_hr2.char(hr[1], CC=1).pack(side=tk.LEFT)
	d_min1.char(mn[0]).pack(side=tk.LEFT)
	d_min2.char(mn[1], CC=1).pack(side=tk.LEFT)
	d_sec1.char(se[0]).pack(side=tk.LEFT)
	d_sec2.char(se[1], DP=1).pack(side=tk.LEFT)
	d_mic.char(mi[0]).pack(side=tk.LEFT)

	root.after(100, example_routine)

## EXECUTABLE ## 

root = tk.Tk()
root.title('pyVFD Example')

gh=200

# build displays
d_hr1 = pyVFD.seg7(root, height=gh, off_color=[51,0,0], on_color=[255,0,0])
d_hr2 = pyVFD.seg7(root, height=gh, off_color=[51,25,0], on_color=[255,128,0],
	 use_CC=True)
d_min1 = pyVFD.seg7(root, height=gh, off_color=[51,51,0], on_color=[255,255,0])
d_min2 = pyVFD.seg7(root, height=gh, off_color=[25,51,0], on_color=[128,255,0],
	use_CC=True)
d_sec1 = pyVFD.seg7(root, height=gh, off_color=[0,51,51], on_color=[0,255,255])
d_sec2 = pyVFD.seg7(root, height=gh, off_color=[25,0,51], on_color=[127,0,255],
	use_DP=True)
d_mic = pyVFD.seg7(root, height=gh, off_color=[32,32,32], on_color=[255,255,255])

# set initial condition
d_hr1.char('off').pack(side=tk.LEFT)
d_hr2.char('off').pack(side=tk.LEFT)
d_min1.char('off').pack(side=tk.LEFT)
d_min2.char('off').pack(side=tk.LEFT)
d_sec1.char('off').pack(side=tk.LEFT)
d_sec2.char('off').pack(side=tk.LEFT)
d_mic.char('off').pack(side=tk.LEFT)

example_routine()

root.mainloop()
