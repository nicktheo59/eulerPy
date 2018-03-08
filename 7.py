PRIMES = [ 2 ]
NON_PRIMES = [ 1 ]

import math
set = range(2,110000)

count = 0

for number in set:
	count += 1
	if any( number % prime == 0 and prime <= math.sqrt(number) for prime in PRIMES ):
		NON_PRIMES += [number]
	else:
		PRIMES += [number]
	if count % 10000 == 0:
		print count
		


print PRIMES[10001]
#print NON_PRIMES