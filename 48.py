index = 1

total = 0

while index <= 1000:
	total += index**index
	index += 1
	print index
	
print total % 10**10
	