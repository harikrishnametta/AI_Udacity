rows = 'ABCDEFGHI'
cols = '123456789'
def cross(a,b):
	return [x+y for x in a for y in b]
boxes = cross(rows, cols)
row_peers = [[r+c for c in cols] for r in rows]
col_peers = [[r+c for r in rows] for c in cols]
box_peers = [[k+t for k in r for t in c] for r in ('ABC', 'DEF', 'GHI') for c in ('123','456','789')]
all_setsOfPeers = row_peers + col_peers + box_peers
print(all_setsOfPeers)