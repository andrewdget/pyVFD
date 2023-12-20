## NOTES ##
'''

'''

## DEPENDENCIES ## 
import tkinter as tk
from PIL import Image

## DEFINITIONS ##

class pyVFD:
	def __init__(self):
		pass

	class seg7:
		''' 
		CONFIG:
			-Height
			-Width
			-fgcolor
			-bgcolor
			-use_DP
			-use_CC
		'''

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
			self.graphic_roster = self.batch_resize(self.graphic_roster, 
				width=self.config['width'], height=self.config['height'])

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

			self.graphic_roster['segA_on'].show()



		def config(self, height=None, width=None, on_color=[204, 246, 250],
			off_color=[59, 56, 56], use_DP=False, use_CC=False):
			config = {'height': height, 'width': width, 'on_color': on_color,
				'off_color': off_color, 'use_DP': use_DP, 'use_CC': use_CC}
			return config
			

		def loadgraphics(self, path_roster):
			graphic_names = list(path_roster.keys())
			graphic_roster = {}
			for name in graphic_names:
				path = path_roster[name]
				graphic = Image.open(path)
				graphic_roster[name] = graphic
			return graphic_roster


		def resize(self, graphic, width=None, height=None):
			[w, h] = graphic.size
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


	# class seg16:
	# 	def __init__():
	# 		pass

## EXECUTABLE ## 
root = tk.Tk()
root.title('pyVFD Test')

pyVFD.seg7(root)

root.mainloop()

# aspect = 2/3
# print(aspect)

# width = 100
# height = width/aspect
# print(height)
# print(width)

# print()

# print(aspect)
# height = 100
# width = height * aspect
# print(height)
# print(width)
