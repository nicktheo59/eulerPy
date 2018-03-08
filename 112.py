def is_descending(n):
	""" Returns True or False

	>>> is_descending(321) 
	True

	>>> is_descending(123)
	False

	>>> is_descending(222)
	True

	>>> is_descending(5)
	True

	"""
	assert type(n) is int
	if len(str(n)) == 1:
		return True
	elif int(str(n)[-1]) <= int(str(n)[-2]):
		return is_descending(int(str(n)[:-1]))
	else:
		return False



def is_ascending(n):
	""" Returns True or False

	>>> is_ascending(123)
	True

	>>> is_ascending(222)
	True

	>>> is_ascending(321)
	False

	>>> is_ascending(12532)
	False
	"""
	assert type(n) is int
	if len(str(n)) == 1:
		return True
	elif int(str(n)[0]) <= int(str(n)[1]):
		return is_ascending(int(str(n)[1:]))
	else:
		return False



def is_Bouncy(n):
	""" Returns True or False

	>>> is_Bouncy(123)
	False

	>>> is_Bouncy(321)
	False

	>>> is_Bouncy(142)
	True

	>>> is_Bouncy(23345)
	False

	>>> is_Bouncy(2344564)
	True

	"""
	return not (is_ascending(n) or is_descending(n))


Bouncy_numbers = []
k = 0
percentage_Bouncy = 0

while percentage_Bouncy < 99:
	print k
	k += 1
	if is_Bouncy(k):
		Bouncy_numbers.append(k)
	percentage_Bouncy = len(Bouncy_numbers) * 100 / k

print k


# def calculate_Bouncy_numbers_up_to(n):
# 	""" Returns a percentage

# 	>>> calculate_Bouncy_ratio_up_to(538)
# 	50

# 	>>> calculate_Bouncy_ratio_up_to(21780)
# 	90

# 	"""
# 	if n == 1:
# 		return []
# 		if is_Bouncy(k):
# 			Bouncy_numbers.append(k)
# 	return Bouncy_numbers

# calculate_Bouncy_ratio_up_to(n+1) = calculate_Bouncy_ratio_up_to(n) /




if __name__ == '__main__':
    import doctest
    doctest.testmod()