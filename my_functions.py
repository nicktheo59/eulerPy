
def productIsPandigital(a,b):
	"""(39,186) -> True (39*186 = 7254)"""
	assert type(a) is int and type(b) is int, "Inputs must be integers"
	number_string = str(a) + str(b) + str(a*b)
	if len(number_string) != 9:
		return False
	the_set = set(number_string)
	return the_set == set('123456789')

def isPandigital(n):
	"""1234567890 -> True"""
	assert type(n) is int, "Input must be integers"
	if len(str(n)) != 10:
		return False
	the_set = set(str(n))
	return the_set == set('0123456789')


def integerToDigitList(integer):
	"""123 -> [1,2,3]"""
	assert type(integer) is int
	return [int(x) for x in str(integer)]

def tupleToInt(the_tuple):
	"""(1,2,3) -> 123"""
	assert type(the_tuple) is tuple
	number_string = ''
	for i in the_tuple:
		number_string += str(i)
	return int(number_string)

def primes_sieve(limit):
	"""primes_sieve(20) -> [2, 3, 5, 7, 11, 13, 17, 19]"""
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes