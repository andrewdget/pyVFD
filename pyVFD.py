## NOTES ##
'''
1. need to add method for passing canvas options to pyVFD/VFD (.config())
2. need to add method for setting display size based on desired width/height
	(maintain aspect ratio)
3. develop method for changing display/off colors
4. look at create_image anchor location as user option (w/ default selection)
5. fix gaps in graphic. 

'''

## DEPENDENCIES ## 
import tkinter as tk
from PIL import ImageTk, Image

## DEFINITIONS ##
class pyVFD:
	def __init__(self, parent):
		self.parent = parent

		self.segA_on = tk.PhotoImage(file='./Graphics/Modified/MsegA_on.png')
		self.segA_off = tk.PhotoImage(file='./Graphics/Modified/MsegA_off.png')

		self.segB_on = tk.PhotoImage(file='./Graphics/Modified/MsegB_on.png')
		self.segB_off = tk.PhotoImage(file='./Graphics/Modified/MsegB_off.png')

		self.segC_on = tk.PhotoImage(file='./Graphics/Modified/MsegC_on.png')
		self.segC_off = tk.PhotoImage(file='./Graphics/Modified/MsegC_off.png')

		self.segD_on = tk.PhotoImage(file='./Graphics/Modified/MsegD_on.png')
		self.segD_off = tk.PhotoImage(file='./Graphics/Modified/MsegD_off.png')

		self.segE_on = tk.PhotoImage(file='./Graphics/Modified/MsegE_on.png')
		self.segE_off = tk.PhotoImage(file='./Graphics/Modified/MsegE_off.png')

		self.segF_on = tk.PhotoImage(file='./Graphics/Modified/MsegF_on.png')
		self.segF_off = tk.PhotoImage(file='./Graphics/Modified/MsegF_off.png')

		self.segG_on = tk.PhotoImage(file='./Graphics/Modified/MsegG_on.png')
		self.segG_off = tk.PhotoImage(file='./Graphics/Modified/MsegG_off.png')

		self.Grid = tk.PhotoImage(file='./Graphics/Modified/MGrid.png')

		self.VFD(self.parent)

	def VFD(self, parent):
		self.object = tk.Canvas(self.parent, width=130, height=230, bg='black', highlightthickness=0)
		return self.object

	def switch(self, switch):

		if switch[0] == 1:
			self.object.create_image(0, 0, image=self.segA_on, anchor=tk.NW)
		else:
			self.object.create_image(0, 0, image=self.segA_off, anchor=tk.NW)

		if switch[1] == 1:
			self.object.create_image(0, 0, image=self.segB_on, anchor=tk.NW)
		else:
			self.object.create_image(0, 0, image=self.segB_off, anchor=tk.NW)

		if switch[2] == 1:
			self.object.create_image(0, 0, image=self.segC_on, anchor=tk.NW)
		else:
			self.object.create_image(0, 0, image=self.segC_off, anchor=tk.NW)

		if switch[3] == 1:
			self.object.create_image(0, 0, image=self.segD_on, anchor=tk.NW)
		else:
			self.object.create_image(0, 0, image=self.segD_off, anchor=tk.NW)

		if switch[4] == 1:
			self.object.create_image(0, 0, image=self.segE_on, anchor=tk.NW)
		else:
			self.object.create_image(0, 0, image=self.segE_off, anchor=tk.NW)

		if switch[5] == 1:
			self.object.create_image(0, 0, image=self.segF_on, anchor=tk.NW)
		else:
			self.object.create_image(0, 0, image=self.segF_off, anchor=tk.NW)

		if switch[6] == 1:
			self.object.create_image(0, 0, image=self.segG_on, anchor=tk.NW)
		else:
			self.object.create_image(0, 0, image=self.segG_off, anchor=tk.NW)

		self.object.create_image(0, 0, image=self.Grid, anchor=tk.NW)

		return self.object

	def char(self, char):
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

		self.object = self.switch(LUT[char])
		return self.object

	def clear(self):
		self.object.delete('all')
		return self.object

	def bgcolor(r, g, b):
		segs = [
			'segA_off',
			'segB_off',
			'segC_off',
			'segD_off',
			'segE_off',
			'segF_off',
			'segG_off'
			]

		for tgt in segs:
			path = './Graphics/Modified/M' + tgt + '.png'
			seg = Image.open(path)

			o_r, o_g, o_b, a = seg.split()

			n_r = o_r.point(lambda i: r)
			n_g = o_g.point(lambda i: g)
			n_b = o_b.point(lambda i: b)

			new_seg = Image.merge('RGBA', (n_r, n_g, n_b, a))
			new_seg.save(path)

	def fgcolor(r, g, b):
		segs = [
			'segA_on',
			'segB_on',
			'segC_on',
			'segD_on',
			'segE_on',
			'segF_on',
			'segG_on'
			]

		for tgt in segs:
			path = './Graphics/Modified/M' + tgt + '.png'
			seg = Image.open(path)

			o_r, o_g, o_b, a = seg.split()

			n_r = o_r.point(lambda i: r)
			n_g = o_g.point(lambda i: g)
			n_b = o_b.point(lambda i: b)

			new_seg = Image.merge('RGBA', (n_r, n_g, n_b, a))
			new_seg.save(path)


	def resize(factor):
		graphic_list = [
			'./Graphics/segA_on.png',
			'./Graphics/segA_off.png',
			'./Graphics/segB_on.png',
			'./Graphics/segB_off.png',
			'./Graphics/segC_on.png',
			'./Graphics/segC_off.png',
			'./Graphics/segD_on.png',
			'./Graphics/segD_off.png',
 			'./Graphics/segE_off.png',
			'./Graphics/segF_on.png',
			'./Graphics/segF_off.png',
			'./Graphics/segG_on.png',
			'./Graphics/segG_off.png',
			'./Graphics/Grid.png'
			]

		for graphic in graphic_list:
			im = Image.open(graphic)
			[w, h] = im.size
			new_size = (int(float(w)*factor), int(float(h)*factor))
			resized_im = im.resize(new_size)

			root_dir = graphic.split('s/')
			new_dir = root_dir[0] + 's/Modified/M' + root_dir[1]

			resized_im.save(new_dir)

## EXECUTABLE ## 
