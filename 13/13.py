db = open('/Users/neil/Documents/Programs/Python/ProjectEuler/13/13.txt' , 'r')

sum = 0

for line in db:
	sum += int(line)
	
print sum