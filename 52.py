for x in range(100000,1000000):
	if len(str(x)) == 6 and len(str(2*x)) == 6 and len(str(3*x)) == 6 and len(str(4*x)) == 6 and len(str(5*x)) == 6 and len(str(6*x)) == 6:
		print(x,2*x,3*x,4*x,5*x,6*x)