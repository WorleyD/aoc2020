import sys
from math import sin, cos, tan, radians, degrees

locx = 0 
locy = 0

wayx,wayy = 10,1 #represents offset from ship
waydir = degrees(tan(wayy/wayx))


cdir = 0

for line in sys.stdin:
	l = line.strip()
	d,step = l[0],int(l[1:])
	
	if d == "N":
		wayy += step
	elif d == "S":
		wayy -= step
	elif d == "E":
		wayx += step
	elif d == "W":
		wayx -= step
	elif d == "L":
		s = sin(radians(step))
		c = cos(radians(step))
		wayx,wayy = wayx*c - wayy*s, wayx*s + wayy*c

	elif d == "R":
		s = sin(radians(360 - step))
		c = cos(radians(360 - step))
		wayx,wayy = wayx*c - wayy*s, wayx*s + wayy*c
		
	elif d == "F":
		locx += step*wayx
		locy += step*wayy

print(abs(locx) + abs(locy))
