# Read in lines of input 

def readInputLines(inputFile): 
	inputLines = []
	with open(inputFile, 'r') as infile: 
		lines = infile.readlines() 
		for line in lines: 
			# print(line)
			inputLines.append(line)
	return inputLines

inputLines = readInputLines('input')

# Part 1
hor = 0 
depth = 0
for line in inputLines: 
	command, val = line.split(' ') 
	if command == 'forward':
		hor += int(val)
	elif command == 'down':
		depth += int(val)
	elif command == 'up': 
		depth -= int(val)
	else: 
		print('INVALID COMMAND', command) 
	
print(str(hor), str(depth))

print(hor*depth)

# Part 2
aim = 0
hor = 0
depth = 0
for line in inputLines: 
	command, val = line.split(' ') 
	if command == 'forward':
		hor += int(val)
		depth += aim*int(val)
	elif command == 'down':
		aim += int(val)
	elif command == 'up': 
		aim -= int(val)
	else: 
		print('INVALID COMMAND', command) 
	

print(hor*depth)
