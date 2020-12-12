import sys
from math import sin, cos, radians

locx = 0 
locy = 0
cdir = 0
for line in sys.stdin:
	l = line.strip()
	d,step = l[0],int(l[1:])
	
	if d == "N":
		locy += step
	elif d == "S":
		locy -= step
	elif d == "E":
		locx += step
	elif d == "W":
		locx -= step
	elif d == "L":
		cdir = (cdir + step) % 360
	elif d == "R":
		cdir = (cdir - step) % 360
	elif d == "F":
		locx += step*cos(radians(cdir))
		locy += step*sin(radians(cdir))

print(abs(locx) + abs(locy))
