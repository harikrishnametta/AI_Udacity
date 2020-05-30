rows = 'ABCDEFGHI'
cols = '123456789'
def cross(a,b):
	return [x+y for x in a for y in b]
boxes = cross(rows, cols)

print(boxes)