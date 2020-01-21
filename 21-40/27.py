



# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
 
def isPrime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
def quadratic(n,a,b):
	answer = n**2 + a*n + b
	return answer
	
def primeSequence(a,b):
	n = 0
	prime_list = [ ]
	while isPrime(quadratic(n,a,b)) == True:
		prime_list += [quadratic(n,a,b)]
		n += 1
	return prime_list




results_dict = { }
a_b_list = [ (a,b) for a in range(-1000,1000) for b in range(-1000,1000) ]
for pair in a_b_list:
	a,b = pair[0],pair[1]
	results_dict[pair] = len(primeSequence(a,b))
		
for ans in results_dict.keys():
	if results_dict[ans] == 71:
		print ans
		