import sys

bags = {}

def countbag(bag):
	count = 0
	if bags[bag][0][1].strip() == "no other":
		return count

	print(bag)
	print(bags[bag])

	bs = bags[bag]
	print(bs)
	for inner in bs:
		print(inner)
		count += (inner[0] + inner[0]*countbag(inner[1]))
	return count

for line in sys.stdin:
	bag, contents = line.strip().split("contain")
	bag = bag[:-6]
	contents = contents[1:-1].split(",")	

	cons = []
	for c in contents:
		if c.strip()[0].isnumeric():
			cons.append((int(c.strip()[0]), c.strip()[1:-4].strip()))
		else:
			cons.append((0, c.strip()[:-4]))
	bags[bag] = cons



print(bags)
print(countbag("shiny gold"))
