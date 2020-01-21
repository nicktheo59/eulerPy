from decimal import *

getcontext().prec = 50

for num in range(1,1000):
	x = len(set(list(str(Decimal(1)/Decimal(num)))))
	print num, x


