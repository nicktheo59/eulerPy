import itertools as it

permutationsList = list(it.permutations(range(10), 10))

#num = int(''.join(map(str,numList)))

def FormNumber(numberTuple):
	return int(''.join(map(str,numberTuple)))
	
#print FormNumber((1,2,3))
	

	
	
numberList = (map(FormNumber, permutationsList))

numberList.sort()

print numberList[999999]
	