#Make an empty list of lengths
#for each number under a million
#	Make an empty list
#	add number to list
#	while number != 1
#		if number is even:
#			number = number/2
#		else:
#			number = 3*number + 1
#		add number to list
#	
#

lengths = { }
for start in range(1,1000000):
	number = start
	seq = [ ]
	seq.append(number)
	while number != 1:
		if number % 2 == 0:
			number = number/2
		else:
			number = 3*number + 1
		seq.append(number)
	lengths[start] = len(seq)

answer = 1
max_value = 1	
for entry in lengths:
	if lengths[entry] > max_value:
		max_value = lengths[entry]
		answer = entry

print answer , max_value
#	
#
