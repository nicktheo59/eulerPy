import re
from time import time
s = time()

matrix_file = open('matrix.txt','r')

# for line in matrix_file:
# 	print line.split(',')

matrix = []

for line in matrix_file:
	row1 = line.split(',')
	row2 = []
	for k in row1:
		row2.append(int(re.search('\d*',k).group()))
	matrix.append(row2)


min_matrix = []
for k in range(80):
	min_matrix.append([0] * 80)

def calculate_min_matrix_slot(i,j):
	if i == 0 and j == 0:
		min_matrix[i][j] = matrix[i][j]
	elif i == 0:
		min_matrix[i][j] = min_matrix[i][j-1] + matrix[i][j]
	elif j == 0:
		min_matrix[i][j] = min_matrix[i-1][j] + matrix[i][j]
	else:
		min_matrix[i][j] = min(min_matrix[i][j-1],min_matrix[i-1][j]) + matrix[i][j]

calculate_min_matrix_slot(0,0)
calculate_min_matrix_slot(1,0)
calculate_min_matrix_slot(0,1)
calculate_min_matrix_slot(1,1)
print min_matrix[0][0], min_matrix[1][0], min_matrix[0][1], min_matrix[1][1]

for i in range(80):
	for j in range(80):
		calculate_min_matrix_slot(i,j)


print min_matrix[-1][-1]

