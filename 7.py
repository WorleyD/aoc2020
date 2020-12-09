import sys

bags = {}

def look(bag, seen):
	if "shiny gold" in bags[bag]:
		return True
	for inner in bags[bag]:
		if inner == "no other":
			continue
		if inner not in seen:
			seen.add(inner)
			if look(inner, seen):
				return True
	return False

seen = set("shiny gold")

for line in sys.stdin:
	bag, contents = line.strip().split("contain")
	bag = bag[:-6]
	
	contents = contents[1:-1].split(",")
	#print(contents)
	c = []
	for con in contents:
		s = con.strip()
		#print(s)
		if s[0].isnumeric():
			#print(s[1:-4].strip())
			c.append(s[1:-4].strip())
		else:
			c.append(s[:-4].strip())

	bags[bag] = c

count = 0
for bag in bags:
	seen = set()
	if look(bag, seen):
		count+=1
print(count)




