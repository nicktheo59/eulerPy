answer_list = [ ] 
count = 1
for number in range(1,1000000):
	digit_list = list( str( number ) )
	digit_sum5 = 0
	for i in digit_list:
		digit_sum5 += int(i)**5
	if digit_sum5 == number:	
		answer_list.append( number )
	count += 1
	if count % 100000 == 0:
		print count

print answer_list
print sum(answer_list)
	