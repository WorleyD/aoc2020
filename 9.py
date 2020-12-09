import sys

nums = []
allnums = []

i = 0
for line in sys.stdin:
	n = int(line)
	allnums.append(n)
	#print(nums)
	if i >= 25:
		flag = False
		for j in range(len(nums)):
			if flag:
				break
			for k in range(j+1,len(nums)):
				if nums[j] + nums[k] == n:
					print(j,k,n)
					flag = True
					break

		if not flag:
			secret = n
			print(n)
			break
		nums.pop()

	nums.insert(0,n)
	
	i += 1
	

for i in range(len(allnums)):
	for j in range(i, len(allnums)):
		if sum(allnums[i:j]) == secret:
			print(min(allnums[i:j]) + max(allnums[i:j]))
			sys.exit()
