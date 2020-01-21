import itertools

number_choices = itertools.permutations([1,2,3,4,5,6,7,8,9],3)

def digit(a,b):
	return int(str(a) + str(b))
#c, o_1, o_2 = triple
def curious_test(c, o_1, o_2):
	if float(digit(c,o_1)) / digit(c,o_2) == float(o_1) / o_2:
		print str(c), str(o_1) + "/" + str(c), str(o_2)
		return True
	elif float(digit(o_1,c)) / digit(c,o_2) == float(o_1) / o_2:
		print str(o_1), str(c) + "/" + str(c), str(o_2)
		return True
	elif float(digit(c,o_1)) / digit(o_2,c) == float(o_1) / o_2:
		print str(c), str(o_1) + "/" + str(o_2), str(c)
		return True
	elif float(digit(o_1,c)) / digit(o_2,c) == float(o_1) / o_2:
		print str(o_1), str(c) + "/" + str(o_2), str(c)
		return True
	else:
		return False

for triple in number_choices:
	c, o_1, o_2 = triple
	if curious_test(c, o_1, o_2):
		print curious_test(c, o_1, o_2)


if __name__ == '__main__':
	import doctest
	doctest.testmod()