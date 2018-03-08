import math
from time import time
s = time()

factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def digit_factorial_sum(n):
	res = 0
	for d in str(n):
		res += factorials[int(d)]
	return res

d = {1:1, 145:1}

for k in range(1,1000000):
	print k
	if not k in d:
		j = k
		chain = []
		while j not in d and j not in chain:
			chain.append(j)
			j = digit_factorial_sum(j)
		# print chain
		if j in chain:
			dup = chain.index(j)
			# print 'dup: ', dup
			cycle_length = len(chain) - dup
			# print 'cycle_length: ', cycle_length
			# print range(len(chain))
			for c in range(len(chain)):
				if c < dup:
					d[chain[c]] = len(chain[c:dup]) + cycle_length
				else:
					d[chain[c]] = cycle_length
		elif j in d:
			extra = d[j]
			# print extra
			for c in range(len(chain)):
				d[chain[c]] = len(chain[c:]) + extra

		else:
			"Strange exception"

i = 0
for v in d.values():
	if v == 60:
		i += 1

print i




print time() - s
