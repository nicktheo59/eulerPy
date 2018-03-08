f = open( '/Users/neil/Documents/Programs/Python/ProjectEuler/67/triangle67.txt', 'r')

triangle = []

for line in f:
	line = line.translate(None,'\r\n')
	line = line.split(' ')
	line = [ int(i) for i in line ]
	triangle.append(line)

triangle.reverse()

for row in triangle:
	print row

def triangleValue(i,j):
	try:
		answer = triangle[i][j]
	except IndexError:
		return False
	return answer


def maxRouteToElement(i,j):
	if i % 10 == 0:
		print i
	if i == 0:
		return triangleValue(0,j)
	else:
		return max( triangleValue(i,j) + maxRouteToElement(i-1,j), triangleValue(i,j) + maxRouteToElement(i-1,j+1) )

print maxRouteToElement(10,0)


#print maxRouteToElement(99,47)
#print max( [ maxRouteToElement(99,j) for j in range(99) ] )




