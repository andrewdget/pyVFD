## NOTES ##
'''

'''

## EXECUTABLE ## 

seg7_LUT = {
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


seg16_LUT = {
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
