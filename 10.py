import sys
	
def countarr(jolts):
	paths = [1]
	for i in range(1, len(jolts)):
		p = paths[i-1]	
		j = i-2
		while j >= 0 and jolts[i] - jolts[j] <= 3:
			p += paths[j]
			j -= 1
		paths.append(p)

	return paths[-1]

jolts = []
ones = 0
threes = 1
for line in sys.stdin:
	jolts.append(int(line))

jolts.sort()

print(jolts)

i = 0
for j in jolts:
	if j-i == 1:
		ones += 1
	elif j-i == 3:
		threes +=1
	i = j
print(ones*threes)

jolts.insert(0,0)
jolts.append(max(jolts)+3)
print(countarr(jolts))