rows = 'ABCDEFGHI'
cols = '123456789'
def askInput():
	vals = input("Enter Sudoku: ")
	while len(vals) != 81:
		vals = input("given sudoku not 9X9! Enter Sudoku again: ")
	return vals
def cross(a,b):
	return [x+y for x in a for y in b]
def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
def grid_values(values):
	for k, v in values.items():
		if v == '.':
			values[k] = '123456789'
	return values
def eliminate(values):
	stalled = False
	while not stalled:
		solved_sudoku = len([box for box in values.keys() if len(values[box])==1])
		for k, v in values.items():
			if len(v)==1:
				for everypeers in all_setsOfPeers:
					if k in everypeers:
						for box in everypeers:
							if k != box:
								values[box] = values[box].replace(v, '')
		solved_sudokuNew = len([box for box in values.keys() if len(values[box])==1])
		stalled  = solved_sudoku ==solved_sudokuNew
		if len([box for box in values if len(values[box])==0]):
			return False
	return values
def validSudoku(values):
	if values != False:
		display(values)
	else:
		print("It is not a valid sudoku")
		values=askInput()
		values = dict(zip(boxes, values))
		values = grid_values(values)
		values = eliminate(values)
		values = validSudoku(values)
	return values
# def resonStalled(values):
# 	secondMin = None
# 	for k, v in values.items():
# 		if 
boxes = cross(rows, cols)
row_peers = [[r+c for c in cols] for r in rows]
col_peers = [[r+c for r in rows] for c in cols]
box_peers = [[k+t for k in r for t in c] for r in ('ABC', 'DEF', 'GHI') for c in ('123','456','789')]
all_setsOfPeers = row_peers + col_peers + box_peers
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
# 4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......
givenSudoku = askInput()
sudokuDict = dict(zip(boxes, givenSudoku))
sudokuDict = grid_values(sudokuDict)
sudokuDict = eliminate(sudokuDict)
sudokuDict = validSudoku(sudokuDict)
#check for long number in bo