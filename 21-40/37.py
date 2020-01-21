#!/usr/bin/python

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

prime_list = primes(1000000)


def is_right_truncatable(n):
	""" Returns True or False

	>>> is_right_truncatable(3797)
	True

	>>> is_right_truncatable(79)
	True

	>>> is_right_truncatable(97)
	False
	"""
	assert type(n) is int
	if len(str(n)) == 1:
		return n in prime_list
	elif n in prime_list:
		return is_right_truncatable(int(str(n)[:-1]))
	else:
		return False

def is_left_truncatable(n):
	""" Returns True or False

	>>> is_left_truncatable(3797)
	True

	>>> is_left_truncatable(97)
	True

	>>> is_left_truncatable(79)
	False

	>>> is_left_truncatable(28)
	False
	"""
	assert type(n) is int
	if len(str(n)) == 1:
		return n in prime_list
	elif n in prime_list:
		return is_left_truncatable(int(str(n)[1:]))
	else:
		return False

def both_truncatable(n):
	""" Returns True or False

	>>> both_truncatable(3797)
	True

	>>> both_truncatable(797)
	True

	>>> both_truncatable(268)
	False

	"""
	return is_left_truncatable(n) and is_right_truncatable(n)


truncatable_primes = []
for k in prime_list:
	print k
	if both_truncatable(k):
		truncatable_primes.append(k)
	if len(truncatable_primes) == 15:
		break

print truncatable_primes





if __name__ == '__main__':
	import doctest
	doctest.testmod()

