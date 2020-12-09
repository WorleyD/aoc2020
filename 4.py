import sys
from collections import defaultdict
from functools import reduce

ecs = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
vs = set(["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

count = set()
tot = 0
def verify(d):
	for rp in d:
		p = [rp[0:3], rp[4:]] 
		#print(p)
		if p[0] == "":
			continue
		#print(p)
		#print(p[0], ":", p[1])
		if p[0] == "byr" and not (1920 <= int(p[1]) <= 2002):
			return False
		if p[0] == "iyr" and not (2010 <= int(p[1]) <= 2020):
			#print(p)
			return False
		if p[0] == "eyr" and not (2020 <= int(p[1]) <= 2030):
			
			return False
		if p[0] == "hgt":
			h = p[1][-2:]
			#print(h)
			if h != "cm" and h != "in":
				return False
			if h == "cm" and not (150 <= int(p[1][:-2]) <= 193):

				return False
			if h == "in" and not (59 <= int(p[1][:-2]) <= 76):

				return False

		if p[0] == "hcl" and p[1][0] != "#":
			#print(p)
			#print(p[1][0])
			return False 
		if p[0] == "hcl" and len(p[1]) != 7:
			#print(p)
			return False
		if p[0] == "hcl": 
			#print(p[1][1:])
			for c in p[1][1:]:
				if c not in vs:
					#print(p[1])
					return False
		if p[0] == "ecl" and p[1] not in ecs:
			#print(p[1])
			return False 
		if p[0] == "pid" and len(p[1]) != 9:
			#print(p)
			#print(p[0], p[1])
			return False
		if p[0] == "pid" and not p[1].isnumeric():
			return False
		if p[0] != "pid" and p[0] != "ecl" and p[0] != "hcl" and p[0] != "hgt" and p[0] != "eyr" and p[0] != "iyr" and p[0] != "byr" and p[0] != "cid":
			return False
	return True



valid = 0
passports = []
person = []
d = set([])
for line in sys.stdin:
	person.append(line.strip().split(" "))
	if len(line.strip()) == 0:
		passports.append(reduce(lambda n, m: n + m, person, []))
		person = []


candidates = []
required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for index, passport in enumerate(passports):
    if len(set([key[0:3] for key in passport]).intersection(required)) >= len(required):
        candidates.append(index)

print(candidates)
for p in candidates:
	if verify(passports[p]):
		print(passports[p])
		valid += 1

print(valid)
