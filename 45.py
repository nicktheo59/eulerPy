from bisect import bisect_left
from time import time

s = time()

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end


def nth_Tri(n):
	return [i*(i+1)/2 for i in range(1,n)]

def nth_Pen(n):
	return [i*(3*i-1)/2 for i in range(1,n)]

def nth_Hex(n):
	return [i*(2*i - 1) for i in range(1,n)]

a = nth_Tri(100000)
b = nth_Hex(100000)
c = nth_Pen(100000)




for k in a:
	if binary_search(b,k) != -1 and binary_search(c,k) != -1:
		print k


print time() - s