def integerToDigitList(integer):
	assert type(integer) is int
	return [x for x in str(integer)]

def computeConcatenatedProduct(integer,number_tuple_length):
	assert type(integer) is int
	assert type(number_tuple_length) is int
	number_tuple = tuple(range(1,number_tuple_length + 1))
	concatenatedProduct = []
	for i in number_tuple:
		concatenatedProduct += integerToDigitList(integer*i)
	return int(''.join(concatenatedProduct))


def isRightNumber(number):
	return set(str(number)) == set('123456789') and len(str(number)) == 9

right_numbers = [computeConcatenatedProduct(i,j) for i in range(1,10000) for j in range(1,5) if isRightNumber(computeConcatenatedProduct(i,j))]

print right_numbers

