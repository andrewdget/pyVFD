## NOTES ##
'''

'''

## DEPENDENCIES ## 
from tkinter import Canvas, NW
from PIL import Image, ImageTk

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
			path = './Graphics/' + name + '.png'
			self.path_roster[name] = path

		self.graphic_roster = self.loadgraphics(self.path_roster)
		
		# resize graphics
		if self.use_DP == False and self.use_CC == False:
			self.graphic_roster = self.batch_crop(self.graphic_roster, 0.83, 1)
		self.graphic_roster = self.batch_resize(self.graphic_roster, 
			width=self.width, height=self.height)
		self.graphic_dims = self.getdims(self.graphic_roster['segA_on'])

		# recolor graphics
		for name in self.graphic_names:
			if 'on' in name:
				graphic = self.graphic_roster[name]
				color = self.on_color
				self.graphic_roster[name] = self.recolor(graphic, color)
			elif 'off' in name:
				graphic = self.graphic_roster[name]
				color = self.off_color
				self.graphic_roster[name] = self.recolor(graphic, color)

		self.disp = Canvas(self.parent, 
			width=self.graphic_dims[0], height=self.graphic_dims[1],
			bg=self.bg, highlightthickness=0)

		self.graphic_roster = self.Image2PhotoImage(self.graphic_roster)
		

	def loadgraphics(self, path_roster):
		graphic_names = list(path_roster.keys())
		graphic_roster = {}
		for name in graphic_names:
			path = path_roster[name]
			graphic = Image.open(path)
			graphic_roster[name] = graphic
		return graphic_roster


	def getdims(self, graphic):
		[w, h] = graphic.size
		graphic_dims = [w, h]
		return graphic_dims


	def crop(self, graphic, w_ratio, h_ratio):
		graphic_dims = self.getdims(graphic)
		cropped_graphic = graphic.crop((0, 0, graphic_dims[0]*w_ratio,
			graphic_dims[1]*h_ratio))
		return cropped_graphic


	def batch_crop(self, graphic_roster, w_ratio, h_ratio):
		graphic_names = list(graphic_roster.keys())
		for name in graphic_names:
			graphic = graphic_roster[name]
			graphic_roster[name] = self.crop(graphic, w_ratio, h_ratio)
		return graphic_roster


	def resize(self, graphic, width=None, height=None):
		[w, h] = self.getdims(graphic)
		if width != None and height != None:
			newsize = (width, height)
			resized_graphic = graphic.resize(newsize)
		elif width != None and height == None:
			aspect = w/h
			new_height = int(width/aspect)
			newsize = (width, new_height)
			resized_graphic = graphic.resize(newsize)
		elif width == None and height != None:
			aspect = w/h
			new_width = int(height * aspect)
			newsize = (new_width, height)
			resized_graphic = graphic.resize(newsize)
		else:
			resized_graphic = graphic
		return resized_graphic


	def batch_resize(self, graphic_roster, width=None, height=None):
		graphic_names = list(graphic_roster.keys())
		for name in graphic_names:
			graphic = graphic_roster[name]
			graphic_roster[name] = self.resize(graphic, width, height)
		return graphic_roster


	def recolor(self, graphic, color):
		[r, g, b, alpha] = graphic.split()
		red = r.point(lambda i: color[0])
		green = g.point(lambda i: color[1])
		blue = b.point(lambda i: color[2])
		recolored_graphic = Image.merge('RGBA', (red, green, blue, alpha))
		return recolored_graphic


	def batch_recolor(self, graphic_roster, color):
		graphic_names = list(graphic_roster.keys())
		for name in graphic_names:
			graphic = graphic_roster[name]
			graphic_roster[name] = self.recolor(graphic, color)
		return graphic_roster


	def Image2PhotoImage(self, graphic_roster):
		graphic_names = list(graphic_roster.keys())
		for name in graphic_names:
			graphic_roster[name] = ImageTk.PhotoImage(graphic_roster[name])
		return graphic_roster


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

			'a': [1,1,1,0,1,1,1],
			'b': [0,0,1,1,1,1,1],
			'c': [1,0,0,1,1,1,0],
			'd': [0,1,1,1,1,0,1],
			'e': [1,0,0,1,1,1,1],
			'f': [1,0,0,0,1,1,1],
			'g': [1,0,1,1,1,1,0],
			'h': [0,0,1,0,1,1,1],
			'i': [0,0,0,0,1,1,0],
			'j': [0,1,1,1,1,0,0],
			'k': [1,0,1,0,1,1,1],
			'l': [0,0,0,1,1,1,0],
			'm': [1,0,1,0,1,0,0],
			'n': [1,1,1,0,1,1,0],
			'o': [1,1,1,1,1,1,0],
			'p': [1,1,0,0,1,1,1],
			'q': [1,1,1,0,0,1,1],
			'r': [1,1,0,0,1,1,0],
			's': [1,0,1,1,0,1,1],
			't': [0,0,0,1,1,1,1],
			'u': [0,1,1,1,1,1,0],
			'v': [0,1,1,1,0,1,0],
			'w': [0,1,0,1,0,1,0],
			'x': [0,1,1,0,1,1,1],
			'y': [0,1,1,1,0,1,1],
			'z': [1,1,0,1,0,0,1],

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


## EXECUTABLE ## 
# root = tk.Tk()
# root.title('pyVFD Test')

# disp = seg7(root, height=200, use_CC=True)
# disp.char('off', CC=0).pack(side=tk.LEFT)

# root.mainloop()

