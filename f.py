from functools import reduce
import re

passports = []
person = []

# form a list with every passport
with open("day4/data.txt") as file:
    for row in file:
        person.append(row.strip().split(" "))
        if len(row.strip()) == 0:
            passports.append(reduce(lambda n, m: n + m, person, []))
            person = []

# list the indices of all passports that contain every requisite field
candidates = []
required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for index, passport in enumerate(passports):
    if len(set([key[0:3] for key in passport]).intersection(required)) >= len(required):
        candidates.append(index)

# regex to check for hex and decimal numbers
def matchhex(text: str, search=re.compile(r'[^a-f0-9.]').search):
    return not bool(search(text))

def matchdec(text: str, search=re.compile(r'[^0-9.]').search):
    return not bool(search(text))

# check that the requisite fields are valid
def validate(passport: list):
    pport = {}
    for field in passport:
        pport[field[0:3]] = field[4:]
    c = 0

    if len(pport["byr"]) == len(pport["iyr"]) == len(pport["eyr"]) == 4:
        if "1920" <= pport["byr"] <= "2002":
            c += 1

        if "2010" <= pport["iyr"] <= "2020":
            c += 1

        if "2020" <= pport["eyr"] <= "2030":
            c += 1

    if pport["hgt"][-2:] == "cm" and \
        "150" <= pport["hgt"][:-2] <= "193":
        c += 1

    elif pport["hgt"][-2:] == "in" and \
        "59" <= pport["hgt"][:-2] <= "76":
        c += 1

    if pport["hcl"][0] == "#" and \
        matchhex(pport["hcl"][1:]) and len(pport["hcl"][1:]) == 6:
        c += 1

    if matchdec(pport["pid"]) and len(pport["pid"]) == 9:
        c += 1

    if pport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        c += 1

    return "fuck yeah" if c == 7 else "fuck no"

valid = 0
tot = 0
count = set()
for index in candidates:
    if validate(passports[index]) == "fuck yeah":
        print(passports[index])
        valid += 1
        count.add(tot)
    tot +=1

print(f"the number of actually valid passports is {valid}.")
print(count)
print(len(candidates))