## NOTES ##
'''

'''

## DEPENDENCIES ## 


## DEFINITIONS ##

def seg_tool(ctl):
	switches = []
	segs = list(ctl.keys())
	for i in range(len(segs)):
		seg = segs[i]
		ans = ctl[seg]
		switches.append(ans)
	print('Segment Switches:')
	print(str(switches).replace(' ', ''))

## EXECUTABLE ##
seg7_ctl = {
	'a': 1,
	'b': 1,
	'c': 1,
	'd': 1,
	'e': 1,
	'f': 1,
	'g': 1,

} 
seg_tool(seg7_ctl)

seg16_ctl = {
	'a1': 1,
	'a2': 1,
	'b':  1,
	'c':  1,
	'd1': 0,
	'd2': 1,
	'e':  0,
	'f':  1,
	'g1': 1,
	'g2': 1,
	'h':  0,
	'i':  0,
	'j':  0,
	'k':  0,
	'l':  0,
	'm':  0
}
seg_tool(seg16_ctl)