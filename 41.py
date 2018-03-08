from time import time

s = time()

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]



def is_pandigital(n):
	return set(str(n)) == set(''.join([str(k) for k in range(1,len(str(n)) + 1)]))

primes_list = primes(100000000)
primes_list.reverse()

print "\n\n\n\n\n\n"
for prime in primes_list:
	if is_pandigital(prime):
		print prime
		break

print time() - s
