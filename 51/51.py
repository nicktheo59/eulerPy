import time
import itertools
import math

start = time.time()

# f = open( '/Users/neil/Documents/Programs/Python/ProjectEuler/51/primes-to-100k.txt', 'r')

# prime_list = []

# for line in f:
# 	line = line.translate(None,'\r\n')
# 	prime_list.append(int(line))

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


prime_list = primes(10000)




def findReplacementSpaces(number):
	options = []
	number_length = len(str(number))
	for i in range(1,number_length):
		for choice in itertools.combinations(range(number_length),i):
			options.append(choice)
	return options


def generatePrimeFamily(number,replacement_spaces):
	number_list = [ int(i) for i in str(number) ]
	prime_family = []
	for x in range(10):
		family_member = number_list
		for space in replacement_spaces:
			family_member[space] = x
		family_member = int(''.join(map(str,family_member)))
		if family_member in prime_list:
			prime_family.append(family_member)

	return prime_family
			
			
def isPrimeInList(prime,prime_list):

	temporary_prime_list = prime_list

	middle = int(math.ceil(len(temporary_prime_list)/2))
	
	if len(prime_list) < 5:
		if prime in prime_list:
			return True
		else:
			return False

	if prime == prime_list[middle]:
		return True

	if prime > prime_list[middle]:
		temporary_prime_list = temporary_prime_list[middle:]
		return isPrimeInList(prime,temporary_prime_list)

	if prime < prime_list[middle]:
		temporary_prime_list = temporary_prime_list[:middle]
		return isPrimeInList(prime,temporary_prime_list)

		




print isPrimeInList(4234521,prime_list)

print time.time() - start

otherstart = time.time()

if 34253 in prime_list:
	print True
else:
	print False

print time.time() - otherstart


# for prime in prime_list:
# 	possible_replacement_spaces = findReplacementSpaces(prime)
# 	for replacement_space in possible_replacement_spaces:
# 		prime_family = generatePrimeFamily(prime,replacement_space)
# 		if len(prime_family) == 8:
# 			print prime
# 			break





			










