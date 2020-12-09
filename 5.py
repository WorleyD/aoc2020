import sys

m = 0

vals = set([])
for line in sys.stdin:
	rhigh = 127
	rlow = 0
	for c in line[:7]:
		mid = (rhigh - rlow)//2
		#print(mid)
		if c == "F":
			rhigh = rlow + mid
		if c == "B":
			rlow = rhigh - mid

	chigh = 7
	clow = 0
	#print(line[7:])
	for c in line[7:]:
		mid = (chigh - clow)//2
		#print(mid)
		if c == "L":
			chigh = clow + mid
		if c == "R":
			clow = chigh - mid

	val = rhigh*8 + chigh
	vals.add(val)
	if val > m:
		m = val

for i in range(1022):
	if i+1 in vals and i-1 in vals and i not in vals:
		print(i)

