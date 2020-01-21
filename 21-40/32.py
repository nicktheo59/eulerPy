def isPandigital(a,b):
	assert type(a) is int and type(b) is int, "Inputs must be integers"
	number_string = str(a) + str(b) + str(a*b)
	if len(number_string) != 9:
		return False
	the_set = set(number_string)
	return the_set == set('123456789')

print isPandigital(39,186)

final_list = [a*b for a in range(1,5000) for b in range(1,5000) if isPandigital(a,b)]

print set(final_list)
print sum(set(final_list))