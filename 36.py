
def IsPallindromic( number ):
	number = str(number)
	if len(number) == 0 or len(number) == 1:
		return True
	elif number[0] == number[-1]:
		return IsPallindromic( number[1:-1] )
	else:
		return False
		
print IsPallindromic( 13111 )

sum = 0
i = 0
for num in range(1000000):
	if IsPallindromic( num ) == True and IsPallindromic( bin(num)[2:]) == True:
		sum += num
	i += 1
	print i
	
print sum


		