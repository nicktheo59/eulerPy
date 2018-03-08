from itertools import *

perms = permutations('1234567890',10)
fails = []
primes = [2,3,5,7,11,13,17]
perms = map(''.join,perms)


for num in perms:
	for i in range(7):
			if int(num[i+1:i+4]) % primes[i] != 0:
				fails.append(int(num))


print sum(set(map(int,perms)) - set(fails))