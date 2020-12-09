import sys

vals = []
for i in sys.stdin:
	vals.append(int(i))

vals.sort()

for i in range(len(vals)):
	for j in range(i, len(vals)):
		for k in range(j,len(vals)): 	
			if vals[i] + vals[j] + vals[k] == 2020:
				print(vals[i]*vals[j]*vals[k])
			if vals[i] + vals[k] + vals[k] >= 2020:
				continue

		if vals[i] + vals[j] > 2020: 
			continue