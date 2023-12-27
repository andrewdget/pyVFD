## NOTES ##
'''

'''

## DEPENDENCIES ## 

from Utils import *
from tkinter import Canvas, NW

## DEFINITIONS ##

class seg7:

	def __init__(self, parent, width=None, height=None, 
		on_color=[204, 246, 250], off_color=[59, 56, 56], bg='black',
		use_DP=False, use_CC=False):

		self.parent = parent
		self.width = width
		self.height = height
		self.on_color = on_color
		self.off_color = off_color
		self.bg = bg
		self.use_DP = use_DP
		self.use_CC = use_CC

		# generate list of graphics to load from file
		self.graphic_names = ['segA_on', 'segB_on', 'segC_on', 'segD_on',
			'segE_on', 'segF_on', 'segG_on', 'segA_off', 'segB_off', 
			'segC_off', 'segD_off', 'segE_off', 'segF_off', 'segG_off',
			'Grid']

		if self.use_DP:
			self.graphic_names.extend(['segDP_on', 'segDP_off'])

		if self.use_CC:
			self.graphic_names.extend(['segCC_on', 'segCC_off'])

		# generate dictionary of graphic names and their path
		self.path_roster = {}
		for name in self.graphic_names:
			path = './Graphics/seg7/' + name + '.png'
			self.path_roster[name] = path

		self.graphic_roster = loadgraphics(self.path_roster)
		
		# resize graphics
		if self.use_DP == False and self.use_CC == False:
			self.graphic_roster = batch_crop(self.graphic_roster, 0.83, 1)
		self.graphic_roster = batch_resize(self.graphic_roster, 
			width=self.width, height=self.height)
		self.graphic_dims = getdims(self.graphic_roster['Grid'])

		# recolor graphics
		for name in self.graphic_names:
			if 'on' in name:
				graphic = self.graphic_roster[name]
				color = self.on_color
				self.graphic_roster[name] = recolor(graphic, color)
			elif 'off' in name:
				graphic = self.graphic_roster[name]
				color = self.off_color
				self.graphic_roster[name] = recolor(graphic, color)

		self.disp = Canvas(self.parent, 
			width=self.graphic_dims[0], height=self.graphic_dims[1],
			bg=self.bg, highlightthickness=0)

		self.graphic_roster = Image2PhotoImage(self.graphic_roster)


	def control(self, switches, DP=None, CC=None):
		if switches[0] == 1:
			segA_on = self.graphic_roster['segA_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segA_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[1] == 1:
			segB_on = self.graphic_roster['segB_on']
			self.disp.create_image(0, 0, image=segB_on, anchor=NW)
		else:
			segB_off = self.graphic_roster['segB_off']
			self.disp.create_image(0, 0, image=segB_off, anchor=NW)

		if switches[2] == 1:
			segC_on = self.graphic_roster['segC_on']
			self.disp.create_image(0, 0, image=segC_on, anchor=NW)
		else:
			segC_off = self.graphic_roster['segC_off']
			self.disp.create_image(0, 0, image=segC_off, anchor=NW)

		if switches[3] == 1:
			segD_on = self.graphic_roster['segD_on']
			self.disp.create_image(0, 0, image=segD_on, anchor=NW)
		else:
			segD_off = self.graphic_roster['segD_off']
			self.disp.create_image(0, 0, image=segD_off, anchor=NW)

		if switches[4] == 1:
			segE_on = self.graphic_roster['segE_on']
			self.disp.create_image(0, 0, image=segE_on, anchor=NW)
		else:
			segE_off = self.graphic_roster['segE_off']
			self.disp.create_image(0, 0, image=segE_off, anchor=NW)

		if switches[5] == 1:
			segF_on = self.graphic_roster['segF_on']
			self.disp.create_image(0, 0, image=segF_on, anchor=NW)
		else:
			segF_off = self.graphic_roster['segF_off']
			self.disp.create_image(0, 0, image=segF_off, anchor=NW)

		if switches[6] == 1:
			segG_on = self.graphic_roster['segG_on']
			self.disp.create_image(0, 0, image=segG_on, anchor=NW)
		else:
			segG_off = self.graphic_roster['segG_off']
			self.disp.create_image(0, 0, image=segG_off, anchor=NW)

		if self.use_DP:
			if DP == 1:
				segDP_on = self.graphic_roster['segDP_on']
				self.disp.create_image(0, 0, image=segDP_on, anchor=NW)
			else:
				segDP_off = self.graphic_roster['segDP_off']
				self.disp.create_image(0, 0, image=segDP_off, anchor=NW)

		if self.use_CC:
			if CC == 1:
				segCC_on = self.graphic_roster['segCC_on']
				self.disp.create_image(0, 0, image=segCC_on, anchor=NW)
			else:
				segCC_off = self.graphic_roster['segCC_off']
				self.disp.create_image(0, 0, image=segCC_off, anchor=NW)

		Grid = self.graphic_roster['Grid']
		self.disp.create_image(0, 0, image=Grid, anchor=NW)

		return self.disp


	def char(self, char, DP=None, CC=None):
		LUT = {
			'off': [0,0,0,0,0,0,0],

			'A': [1,1,1,0,1,1,1],
			'B': [0,0,1,1,1,1,1],
			'C': [1,0,0,1,1,1,0],
			'D': [0,1,1,1,1,0,1],
			'E': [1,0,0,1,1,1,1],
			'F': [1,0,0,0,1,1,1],
			'G': [1,0,1,1,1,1,0],
			'H': [0,0,1,0,1,1,1],
			'I': [0,0,0,0,1,1,0],
			'J': [0,1,1,1,1,0,0],
			'K': [1,0,1,0,1,1,1],
			'L': [0,0,0,1,1,1,0],
			'M': [1,0,1,0,1,0,0],
			'N': [1,1,1,0,1,1,0],
			'O': [1,1,1,1,1,1,0],
			'P': [1,1,0,0,1,1,1],
			'Q': [1,1,1,0,0,1,1],
			'R': [1,1,0,0,1,1,0],
			'S': [1,0,1,1,0,1,1],
			'T': [0,0,0,1,1,1,1],
			'U': [0,1,1,1,1,1,0],
			'V': [0,1,1,1,0,1,0],
			'W': [0,1,0,1,0,1,0],
			'X': [0,1,1,0,1,1,1],
			'Y': [0,1,1,1,0,1,1],
			'Z': [1,1,0,1,0,0,1],

			'0': [1,1,1,1,1,1,0],
			'1': [0,1,1,0,0,0,0],
			'2': [1,1,0,1,1,0,1],
			'3': [1,1,1,1,0,0,1],
			'4': [0,1,1,0,0,1,1],
			'5': [1,0,1,1,0,1,1],
			'6': [1,0,1,1,1,1,1],
			'7': [1,1,1,0,0,0,0],
			'8': [1,1,1,1,1,1,1],
			'9': [1,1,1,1,0,1,1]
			}

		self.disp = self.control(LUT[char], DP, CC)
		return	self.disp


	def clear(self):
		self.disp.delete('all')
		return self.disp


class seg16:

	def __init__(self, parent, width=None, height=None, 
		on_color=[204, 246, 250], off_color=[59, 56, 56], bg='black',
		use_DP=False, use_CC=False):

		self.parent = parent
		self.width = width
		self.height = height
		self.on_color = on_color
		self.off_color = off_color
		self.bg = bg
		self.use_DP = use_DP
		self.use_CC = use_CC

		# generate list of graphics to load from file
		self.graphic_names = ['segA1_on', 'segA2_on', 'segB_on', 'segC_on',
			'segD1_on', 'segD2_on', 'segE_on', 'segF_on', 'segG1_on',
			'segG2_on', 'segH_on', 'segI_on', 'segJ_on', 'segK_on', 'segL_on',
			'segM_on', 'segA1_off', 'segA2_off', 'segB_off', 'segC_off',
			'segD1_off', 'segD2_off', 'segE_off', 'segF_off', 'segG1_off',
			'segG2_off', 'segH_off', 'segI_off', 'segJ_off', 'segK_off',
			'segL_off', 'segM_off', 'Grid']

		if self.use_DP:
			self.graphic_names.extend(['segDP_on', 'segDP_off'])

		if self.use_CC:
			self.graphic_names.extend(['segCC_on', 'segCC_off'])

		# generate dictionary of graphic names and their path
		self.path_roster = {}
		for name in self.graphic_names:
			path = './Graphics/seg16/' + name + '.png'
			self.path_roster[name] = path

		self.graphic_roster = loadgraphics(self.path_roster)

		# resize graphics
		if self.use_DP == False and self.use_CC == False:
			self.graphic_roster = batch_crop(self.graphic_roster, 0.83, 1)
		self.graphic_roster = batch_resize(self.graphic_roster, 
			width=self.width, height=self.height)
		self.graphic_dims = getdims(self.graphic_roster['Grid'])

		# recolor graphics
		for name in self.graphic_names:
			if 'on' in name:
				graphic = self.graphic_roster[name]
				color = self.on_color
				self.graphic_roster[name] = recolor(graphic, color)
			elif 'off' in name:
				graphic = self.graphic_roster[name]
				color = self.off_color
				self.graphic_roster[name] = recolor(graphic, color)

		self.disp = Canvas(self.parent, 
			width=self.graphic_dims[0], height=self.graphic_dims[1],
			bg=self.bg, highlightthickness=0)

		self.graphic_roster = Image2PhotoImage(self.graphic_roster)


	def control(self, switches, DP=None, CC=None):
		if switches[0] == 1:
			segA_on = self.graphic_roster['segA1_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segA1_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[1] == 1:
			segA_on = self.graphic_roster['segA2_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segA2_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)	

		if switches[2] == 1:
			segA_on = self.graphic_roster['segB_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segB_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[3] == 1:
			segA_on = self.graphic_roster['segC_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segC_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[4] == 1:
			segA_on = self.graphic_roster['segD1_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segD1_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[5] == 1:
			segA_on = self.graphic_roster['segD2_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segD2_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[6] == 1:
			segA_on = self.graphic_roster['segE_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segE_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[7] == 1:
			segA_on = self.graphic_roster['segF_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segF_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[8] == 1:
			segA_on = self.graphic_roster['segG1_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segG1_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[9] == 1:
			segA_on = self.graphic_roster['segG2_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segG2_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[10] == 1:
			segA_on = self.graphic_roster['segH_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segH_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[11] == 1:
			segA_on = self.graphic_roster['segI_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segI_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[12] == 1:
			segA_on = self.graphic_roster['segJ_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segJ_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[13] == 1:
			segA_on = self.graphic_roster['segK_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segK_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[14] == 1:
			segA_on = self.graphic_roster['segL_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segL_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if switches[15] == 1:
			segA_on = self.graphic_roster['segM_on']
			self.disp.create_image(0, 0, image=segA_on, anchor=NW)
		else:
			segA_off = self.graphic_roster['segM_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=NW)

		if self.use_DP:
			if DP == 1:
				segDP_on = self.graphic_roster['segDP_on']
				self.disp.create_image(0, 0, image=segDP_on, anchor=NW)
			else:
				segDP_off = self.graphic_roster['segDP_off']
				self.disp.create_image(0, 0, image=segDP_off, anchor=NW)

		if self.use_CC:
			if CC == 1:
				segCC_on = self.graphic_roster['segCC_on']
				self.disp.create_image(0, 0, image=segCC_on, anchor=NW)
			else:
				segCC_off = self.graphic_roster['segCC_off']
				self.disp.create_image(0, 0, image=segCC_off, anchor=NW)

		Grid = self.graphic_roster['Grid']
		self.disp.create_image(0, 0, image=Grid, anchor=NW)

		return self.disp


	def char(self, char, DP=None, CC=None):
		LUT = {
			'off': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

			'A': [1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0],
			'B': [1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0],
			'C': [1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
			'D': [1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0],
			'E': [1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
			'F': [1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
			'G': [1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0],
			'H': [0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0],
			'I': [1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0],
			'J': [0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
			'K': [0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1],
			'L': [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
			'M': [0,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0],
			'N': [0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1],
			'O': [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
			'P': [1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0],
			'Q': [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
			'R': [1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
			'S': [1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0],
			'T': [1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0],
			'U': [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
			'V': [0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0],
			'W': [0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1],
			'X': [0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1],
			'Y': [0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0],
			'Z': [1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0],

			'a': [0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0],
			'b': [0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0],
			'c': [0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
			'd': [0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0],
			'e': [0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0],
			'f': [0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0],
			'g': [1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0],
			'h': [0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0],
			'i': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
			'j': [0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0],
			'k': [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
			'l': [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0],
			'm': [0,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0],
			'n': [0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0],
			'o': [0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0],
			'p': [1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0],
			'q': [1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0],
			'r': [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
			's': [1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0],
			't': [0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0],
			'u': [0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0],
			'v': [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
			'w': [0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1],
			'x': [0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1],
			'y': [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
			'z': [0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0],

			'0': [1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0],
			'1': [0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0],
			'2': [1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0],
			'3': [1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0],
			'4': [0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0],
			'5': [1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0],
			'6': [1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
			'7': [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
			'8': [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
			'9': [1,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0],
			}

		self.disp = self.control(LUT[char], DP, CC)
		return self.disp


	def clear(self):
		self.disp.delete('all')
		return self.disp


## EXECUTABLE ## 

