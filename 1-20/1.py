index = 1
answer = 0
while index <= 999:
	if index % 3 == 0 or index % 5 == 0:
		answer += index
	index += 1
print answer
	