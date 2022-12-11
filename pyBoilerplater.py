# Read in lines of input 

def readInputLines(inputFile): 
	inputLines = []
	with open(inputFile, 'r') as infile: 
		lines = infile.readlines() 
		for line in lines: 
			# print(line)
			inputLines.append(line)
	return inputLines



