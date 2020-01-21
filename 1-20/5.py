count = 1

for number in range(99999999):
	if number % 2 != 0 or number % 3 != 0 or number % 4 != 0 or number % 5 != 0 or number % 6 != 0 or number % 7 != 0 or number % 8 != 0 or number % 9 != 0 or number % 10 != 0 or number % 11 != 0 or number % 12 != 0 or number % 13 != 0 or number % 14 != 0 or number % 15 != 0 or number % 16 != 0 or number % 17 != 0 or number % 18 != 0 or number % 19 != 0 or number % 20 != 0:
		pass
	else:
		print number
	count += 1
	if count % 10000 == 0:
		print `((count*100)/99999999)` + '% complete'
		
#Should be 232792560