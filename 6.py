import sys

sets = []
s = 0
for line in sys.stdin:
	
	if len(line.strip()) == 0:
		print(sets)
		if len(sets) > 1:		
			s += len(set.intersection(*sets))
		else:
			s += len(sets[0])
		sets = []

	s1 = set()
	for c in line.strip():
		s1.add(c)
	if len(s1) > 0:
		sets.append(s1)
		
	
	#print(qs)

print(s)

