import sys

accumulator = 0
instructions = []
for instruction in sys.stdin:
	instructions.append(instruction.split())

i = 0
seen = set()
while True:
	if i == len(instructions):
		break
	com = instructions[i][0]
	val = int(instructions[i][1])
	seen.add(i)
	if com == "nop":
		i+=1
	elif com == "acc":
		accumulator += val
		i += 1
	elif com == "jmp":
		if i + val in seen:
			i+=1
		else:
			i += val

print(accumulator)

