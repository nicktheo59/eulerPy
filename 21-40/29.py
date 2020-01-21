dict = { }

for a in range(2,101):
	for b in range(2,101):
		dict[a**b] = 1
	
	
print len(dict)

	