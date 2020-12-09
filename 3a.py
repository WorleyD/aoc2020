import sys

grid = []
trees1 = 0
trees2 = 0
trees3 = 0
trees4 = 0
for line in sys.stdin:
	grid.append(line[:-1])


posx = 0
posy = 0
while posx < len(grid[0]) and posy < len(grid):
	if grid[posy][posx] == "#":
		trees1 += 1
	posx = (posx + 1) % len(grid[0])
	posy += 1

posx = 0
posy = 0
while posx < len(grid[0]) and posy < len(grid):
	if grid[posy][posx] == "#":
		trees2 += 1
	posx = (posx + 5) % len(grid[0])
	posy += 1

posx = 0
posy = 0
while posx < len(grid[0]) and posy < len(grid):
	if grid[posy][posx] == "#":
		trees3 += 1
	posx = (posx + 7) % len(grid[0])
	posy += 1


posx = 0
posy = 0
while posx < len(grid[0]) and posy < len(grid):
	if grid[posy][posx] == "#":
		trees4 += 1
	posx = (posx + 1) % len(grid[0])
	posy += 2

print(trees4*trees3*trees2*trees1*294)