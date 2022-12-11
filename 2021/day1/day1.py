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
for i in range(len(inputLines)):
	inputLines[i] = int(inputLines[i])

# Part 1
curNum = inputLines[0]
count = 0
for num in inputLines[1:]: 
	if num > curNum: 	
		count += 1
	curNum = num

# print(count) 

# Part 2
print('computing' + str(inputLines[:3]))
curSum = sum(inputLines[:3])
count = 0
for i in range(len(inputLines[1:-1])):
	print('computing' + str(inputLines[i:i+3]))
	newSum = sum(inputLines[i:i+3])
	if newSum > curSum:
		count += 1
	curSum = newSum

print(count)
