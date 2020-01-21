def fib(n): # write Fibonacci series up to n
	fiblist = [ ]
	a, b = 0, 1
	while b < n:
		fiblist.append(b),
		a, b = b, a+b
	return fiblist
        
print fib(4000000)

sum = 0
for number in fib(4000000):
	if number % 2 == 0:
		sum += number
		
print sum