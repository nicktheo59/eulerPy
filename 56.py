def digitalSum(number):
	numberList = [ int(i) for i in str(number) ]
	return sum(numberList)

maxDigitalSum = 0

for number in [ a**b for a in range(1,100) for b in range(1,100) ]:
	currentSum = digitalSum(number)
	if currentSum > maxDigitalSum:
		maxDigitalSum = currentSum

print maxDigitalSum

