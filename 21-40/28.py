g = lambda x: 4*(x**2) - 7*(x) + 4

sum = 0

for x in range(2,502):
	sum += g(x)
	
print 1 + 4*sum
