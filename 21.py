import itertools as it


    
def divisorsSum(n):
    SumOfDivisors=0
    for i in range(1,n):
        if n%i==0:      #finds the divisors
            divisor=i
            SumOfDivisors += divisor
    return SumOfDivisors
   

def isAmicable((x,y)):
	if divisorsSum(x) == y and divisorsSum(y) == x:
		return True
	else:
		return False
		
print isAmicable((284,220))

i = 0
result = [ ]
for x in range(1,10000):
	y = divisorsSum(x)
	if divisorsSum(y) == x and y != x:
		result += (x,y)
	i += 1
	print i
		
print sum(set(result))
	
	