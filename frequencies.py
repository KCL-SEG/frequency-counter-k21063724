"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):    
	items = [str(item) for item in items]
	keys = set(list(items))

	frequencies = { key : 0 for key in keys}

	for item in items:
		frequencies[item]+=1

	return frequencies

if __name__ == '__main__':
	res = frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4'])
	print(res)