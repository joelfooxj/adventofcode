# Read in lines of input 

def readInputLines(inputFile): 
	inputLines = []
	with open(inputFile, 'r') as infile: 
		lines = infile.readlines() 
		for line in lines: 
			# print(line)
			inputLines.append(line)
	return inputLines

def removeLB(inputLines): 
	ret = []
	for line in inputLines: 
		ret.append(line[:-1])
	return ret

inputLines = readInputLines('testInput')
inputLines = removeLB(inputLines)
obj = []
currLines = []
for line in inputLines:
	if line == '': 
		obj.append(currLines) 
		currLines = []
	else: 
		currLines.append(line)

if currLines: 
	obj.append(currLines) 

# print(obj)

randomNums = obj[0]
print(randomNums) 

matrices = obj[1:]

print(matrices[0])
temp = []
for matrix in matrices: 
	# transform into array of array of {num:marked}
	tempMat = []
	for line in matrix: 
		splitLine = line.split(' ')
		list(filter(' ').__ne__, splitLine
		row = [int(num) for num in line.strip().split(' ')]
	tempMap.append(row)
	print(tempMap) 
	temp.append(tempMap)
	

# For each randNum, mark off on each board 
# After each mark, check if the board fulfills winning condition 
# winning condition is -> one row or column full 
# sum all unmarked nums on that board with the winning number 


