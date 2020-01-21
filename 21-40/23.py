import math
import itertools

def findDivisorsOf(n):
	divisors = []
	for i in range( 1, int(math.floor(math.sqrt(n))) + 1 ):
		if n%i == 0:
			divisors += [i,n/i]
	return set(divisors)


def divisorSum(n):
	return sum(findDivisorsOf(n)) - n

def isAbundant(n):
	return divisorSum(n) > n


abundants = [ i for i in range(1,30000) if isAbundant(i)]

sum = 0
for n in range(1,28126):
	if not any( (n-a in abundants) for a in abundants):
		sum += n

print sum


# can_be_written_as_sum_of_two_abundants = {}

# comb = itertools.combinations(abundants,2)

# while True:
# 	try:
# 		temp = comb.next()
# 	except StopIteration:
# 		break
# 	the_sum = sum(temp)
# 	can_be_written_as_sum_of_two_abundants[the_sum] = 1

# print can_be_written_as_sum_of_two_abundants

# cannot_be_written_as_sum_of_two_abundants = set(range(1,28124)) - set(can_be_written_as_sum_of_two_abundants)

# print sum(cannot_be_written_as_sum_of_two_abundants)





