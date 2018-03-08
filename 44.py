from time import time
from itertools import *

def up_to_n_Pen(n):
	return [i*(3*i - 1)/2 for i in range(1,n)]

Pen_list = up_to_n_Pen(1000)

pairs = combinations(Pen_list,2)

for pair in pairs:
	if pair[1] - pair[0] in Pen_list and pair[1] + pair[0] in Pen_list:
		print pair



		