## NOTES ##
'''
1. add crop functionality
'''

## DEPENDENCIES ## 
import tkinter as tk
from PIL import Image, ImageTk

## DEFINITIONS ##

class seg7:

	def __init__(self, parent):
		self.parent = parent
		self.config = self.config()

		# generate list of graphics to load from file
		self.graphic_names = ['segA_on', 'segB_on', 'segC_on', 'segD_on',
			'segE_on', 'segF_on', 'segG_on', 'segA_off', 'segB_off', 
			'segC_off', 'segD_off', 'segE_off', 'segF_off', 'segG_off',
			'Grid']

		if self.config['use_DP']:
			self.graphic_names.extend(['segDP_on', 'segDP_off'])

		if self.config['use_CC']:
			self.graphic_names.extend(['segCC_on', 'segCC_off'])

		# generate dictionary of graphic names and their path
		self.path_roster = {}
		for name in self.graphic_names:
			path = './Graphics/' + name + '.png'
			self.path_roster[name] = path

		self.graphic_roster = self.loadgraphics(self.path_roster)
		
		# resize graphics
		if self.config['use_DP'] == False and self.config['use_CC'] == False:
			self.graphic_roster = self.batch_crop(self.graphic_roster, 0.83, 1)
		self.graphic_roster = self.batch_resize(self.graphic_roster, 
			width=self.config['width'], height=self.config['height'])
		self.graphic_dims = self.getdims(self.graphic_roster['segA_on'])

		# recolor graphics
		for name in self.graphic_names:
			if 'on' in name:
				graphic = self.graphic_roster[name]
				color = self.config['on_color']
				self.graphic_roster[name] = self.recolor(graphic, color)
			elif 'off' in name:
				graphic = self.graphic_roster[name]
				color = self.config['off_color']
				self.graphic_roster[name] = self.recolor(graphic, color)

		self.disp = tk.Canvas(self.parent, 
			width=self.graphic_dims[0], height=self.graphic_dims[1],
			bg=self.config['bg'], highlightthickness=0)

		self.graphic_roster = self.Image2PhotoImage(self.graphic_roster)







	def config(self, height=200, width=None, on_color=[204, 246, 250],
		off_color=[59, 56, 56], bg='black', use_DP=False, use_CC=False):
		config = {'height': height, 'width': width, 'on_color': on_color,
			'off_color': off_color, 'bg': bg, 'use_DP': use_DP,
			'use_CC': use_CC}
		return config
		

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
		cropped_graphic = graphic.crop((0, 0, graphic_dims[0]*w_ratio, graphic_dims[1]*h_ratio))
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
			height = int(width/aspect)
			newsize = (width, height)
			resized_graphic = graphic.resize(newsize)
		elif width == None and height != None:
			aspect = w/h
			width = int(height * aspect)
			newsize = (width, height)
			resized_graphic = graphic.resize(newsize)
		else:
			resized_graphic = graphic
		return resized_graphic


	def batch_resize(self, graphic_roster, width=None, height=None):
		graphic_names = list(graphic_roster.keys())
		for name in graphic_names:
			graphic = graphic_roster[name]
			graphic_roster[name] = self.resize(graphic, height, width)
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
			self.disp.create_image(0, 0, image=segA_on, anchor=tk.NW)
		else:
			segA_off = self.graphic_roster['segA_off']
			self.disp.create_image(0, 0, image=segA_off, anchor=tk.NW)

		if switches[1] == 1:
			segB_on = self.graphic_roster['segB_on']
			self.disp.create_image(0, 0, image=segB_on, anchor=tk.NW)
		else:
			segB_off = self.graphic_roster['segB_off']
			self.disp.create_image(0, 0, image=segB_off, anchor=tk.NW)

		if switches[2] == 1:
			segC_on = self.graphic_roster['segC_on']
			self.disp.create_image(0, 0, image=segC_on, anchor=tk.NW)
		else:
			segC_off = self.graphic_roster['segC_off']
			self.disp.create_image(0, 0, image=segC_off, anchor=tk.NW)

		if switches[3] == 1:
			segD_on = self.graphic_roster['segD_on']
			self.disp.create_image(0, 0, image=segD_on, anchor=tk.NW)
		else:
			segD_off = self.graphic_roster['segD_off']
			self.disp.create_image(0, 0, image=segD_off, anchor=tk.NW)

		if switches[4] == 1:
			segE_on = self.graphic_roster['segE_on']
			self.disp.create_image(0, 0, image=segE_on, anchor=tk.NW)
		else:
			segE_off = self.graphic_roster['segE_off']
			self.disp.create_image(0, 0, image=segE_off, anchor=tk.NW)

		if switches[5] == 1:
			segF_on = self.graphic_roster['segF_on']
			self.disp.create_image(0, 0, image=segF_on, anchor=tk.NW)
		else:
			segF_off = self.graphic_roster['segF_off']
			self.disp.create_image(0, 0, image=segF_off, anchor=tk.NW)

		if switches[6] == 1:
			segG_on = self.graphic_roster['segG_on']
			self.disp.create_image(0, 0, image=segG_on, anchor=tk.NW)
		else:
			segG_off = self.graphic_roster['segG_off']
			self.disp.create_image(0, 0, image=segG_off, anchor=tk.NW)

		if self.config['use_DP']:
			if DP == 1:
				segDP_on = self.graphic_roster['segDP_on']
				self.disp.create_image(0, 0, image=segDP_on, anchor=tk.NW)
			else:
				segDP_off = self.graphic_roster['segDP_off']
				self.disp.create_image(0, 0, image=segDP_off, anchor=tk.NW)

		if self.config['use_CC']:
			if CC == 1:
				segCC_on = self.graphic_roster['segCC_on']
				self.disp.create_image(0, 0, image=segCC_on, anchor=tk.NW)
			else:
				segCC_off = self.graphic_roster['segCC_off']
				self.disp.create_image(0, 0, image=segCC_off, anchor=tk.NW)

		Grid = self.graphic_roster['Grid']
		self.disp.create_image(0, 0, image=Grid, anchor=tk.NW)

		return self.disp


## EXECUTABLE ## 
root = tk.Tk()
root.title('pyVFD Test')

disp = seg7(root)
disp.control([1, 1, 1, 1, 1, 1, 1]).pack(side=tk.LEFT)

root.mainloop()






