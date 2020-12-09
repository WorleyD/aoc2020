import sys

ct = 0
for line in sys.stdin:
	rnge, let, pwd = line.split()
	low,high = [int(x) for x in rnge.split("-")]
	l = let[0]
	if (pwd[low-1] == l and pwd[high-1] != l) or (pwd[low-1] != l and pwd[high-1] == l):
		ct += 1

print(ct) 