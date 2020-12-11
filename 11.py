import sys
from copy import copy,deepcopy

dirs = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]]

#counting neighbours for part 2
def countneighbours2(board, row, cell):
    n = 0

    for d in dirs:
    	dr = deepcopy(d)
    	while inbounds(board,row,cell,dr):
    		if board[row + dr[0]][cell + dr[1]] == "#":
    			n += 1
    			break
    		elif board[row + dr[0]][cell+dr[1]] == "L":
    			break
    		dr[0] += d[0]
    		dr[1] += d[1]
  
    return n


def inbounds(board,row,cell,d):
	return ((0 <= row + d[0] < len(board)) and (0 <= cell + d[1] < len(board[row])))


#counting neighbours for part 1
def countneighbours(board, row, cell):
    n = 0

    for d in dirs:
    	if inbounds(board,row,cell,d):
    		if board[row + d[0]][cell + d[1]] == "#":
    			n += 1
    return n


def update(state):
	new = []
	for row in range(len(state)):
		r = []
		for cell in range(len(state[row])):
			if state[row][cell] == ".":
				r.append(".")
				continue

			n = countneighbours2(state,row,cell)
			if state[row][cell] == "L" and n == 0:
				r.append("#")
			elif state[row][cell] == "#" and n > 4:
				r.append("L")
			else:
				r.append(state[row][cell])
		new.append(r)
	return new


grid = []

for line in sys.stdin:
	grid.append([c for c in str(line.strip())])


nums = 0
state = grid
while True:
	nums +=1
	new = update(deepcopy(state))
	if new == state:
		break

	state = deepcopy(new)

c = 0
for row in state:
	for cell in row:
		if cell == "#":
			c += 1

print(c)