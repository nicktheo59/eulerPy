import math

def NCR(n,r):
	ans = (math.factorial(n))/((math.factorial(n-r))*(math.factorial(r)))
	return ans
	
list = [ NCR(n,r) for n in range(1,101) for r in range(1,101) if n >= r and NCR(n,r) > 1000000]

print len(list)