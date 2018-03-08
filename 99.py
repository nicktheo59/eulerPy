import math
import re
from time import time
s = time()

base_file = open('base_exp.txt','r')

Max_num = 0
line_num = 1
i = 0
for line in base_file:
	i += 1
	line1 = line.split(',')
	line1[0] = int(line1[0])
	line1[1] = int(re.search('\d*',line1[1]).group())
	trial = line1[1] * math.log(line1[0])
	if trial > Max_num:
		Max_num = trial
		line_num = i

print Max_num, line_num


	
# print type(re.search('\d*', '1242343\n').group())



print time() - s