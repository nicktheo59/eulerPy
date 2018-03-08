from time import time
s = time()

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


prime_list = primes(10000)

for p in prime_list:
	differences = [k - p for k in prime_list if k - p > 0]
	for d in differences:
		if p + d in prime_list and p + 2*d in prime_list and set(str(p)) == set(str(p+d)) and set(str(p+d)) == set(str(p+2*d)):
			print p, p + d, p + 2*d


print time() - s