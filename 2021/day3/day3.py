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
totalBits = len(inputLines[0])-1
# print(totalBits, inputLines[0])
# gammaBits = [] 
# for i in range(totalBits):
# 	zeroNum = 0
# 	oneNum = 0 
# 	for line in inputLines:
# 		if line[i] == '0': 
# 			zeroNum += 1
# 		else: 
# 			oneNum += 1
# 	if zeroNum > oneNum: 
# 		gammaBits.append('0')
# 	else: 		
# 		gammaBits.append('1')
# 
# epsBits = []
# for digit in gammaBits: 
# 	if digit == '0': 
# 		epsBits.append('1') 
# 	else: 
# 		epsBits.append('0')
# 
# print(gammaBits) 
# print(epsBits)
# 
# gamma = int(''.join(gammaBits), 2)
# eps = int(''.join(epsBits), 2)
# 
# print(gamma*eps)
 
# Part 2
def findNums(bit, position, lines):
	''' 
	Given lines of binary nums, remove 
	nums that don't meet criteria and return 
	''' 
	ret = []
	for line in lines: 
		if line[position] == bit: 
			ret.append(line)
	return ret

def mostCommon(lines, position): 
	''' 
	Finds the most common bit at the given position
	for each line and returns that bit
	''' 
	
	zeroNum = 0
	oneNum = 0
	for line in lines:
		if line[position] == '0':
			zeroNum += 1
		else: 
			oneNum += 1			
	if zeroNum > oneNum:
		return '0'
	else: 
		return '1'	

def leastCommon(lines, position): 
	''' 
	Finds the least common bit at the given position
	for each line and returns that bit
	''' 
	
	zeroNum = 0
	oneNum = 0
	for line in lines:
		if line[position] == '0':
			zeroNum += 1
		else: 
			oneNum += 1			
	if oneNum < zeroNum:
		return '1'
	else: 
		return '0'	
	
oxyLines = inputLines.copy()
position = 0
while position < totalBits:
	mcBit = mostCommon(oxyLines, position)
	oxyLines = findNums(mcBit, position, oxyLines)
	position += 1
	if len(oxyLines) == 1: 
		break
	
print(oxyLines) 
		
co2Lines = inputLines.copy()
position = 0
while position < totalBits:
	lcBit = leastCommon(co2Lines, position)
	co2Lines = findNums(lcBit, position, co2Lines)
	position += 1
	if len(co2Lines) == 1: 
		break
	
print(co2Lines) 
	
oxyInt = int(oxyLines[0][:-1], 2)
co2Int = int(co2Lines[0][:-1], 2) 
print(oxyInt, co2Int) 
print(oxyInt*co2Int)
