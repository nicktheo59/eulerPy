total1 = 0

index = 1
while index <= 100:
	total1 += index**2
	print total1
	index += 1
	
print total1

total = (total1 - 0.25*(100**2)*(101**2))

print total