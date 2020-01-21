def int_to_list(number):
	return [int(x) for x in str(number)]

def factorial(number):
	assert number >= 0
	if number == 0:
		return 1
	else:
		return number*factorial(number - 1)

def isCurious(n):
	digitFactorialSum = 0
	for i in int_to_list(n):
		digitFactorialSum += factorial(i)
	if n == digitFactorialSum:
		return True
	else:
		return False

total = 0
for i in range(100000):
	if isCurious(i) == True:
		total += i

print total - 3

