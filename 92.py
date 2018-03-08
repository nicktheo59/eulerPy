from time import time
s = time()


# def add_square_of_digits(n):
# 	res = 0
# 	for c in str(n):
# 		res += int(c)**2
# 	return res

# bucket = []

# d = {89:89, 1:1}

# for k in range(1,10):
# 	print d
# 	if k not in d:
# 		print k
# 		j = k
# 		chain = []
# 		while j not in d:
# 			chain.append(j)
# 			j = add_square_of_digits(j)
# 		for c in chain:
# 			d[c] = d[j]
# print d 

def SquareSum(n):
    k = 0
    while n:
        m = n % 10
        n = n/10
        k = k + m*m
    return k

def Compute(ndigits):
    def Recurse(n):
        if not d.has_key(n):
            d[n] = Recurse(SquareSum(n))
        return d[n]
    max = 10**ndigits
    d = {1:1, 89:89}
    for i in range(1, 9*9*ndigits+1):
        Recurse(i)
    count = {1:0, 89:0}
    ss = {}
    us = {}
    sums = {}
    for i in range(0,10):
        ss[i] = i * i
        us[i] = 1
        sums[i*i] = i
    
    m = 10
    while m < max:
        vs = us.keys()
        lus = us.copy()
        for i in range(1, 10):
            n = i * m
            for v in vs:
                k = ss[i] + ss[v]
                if not sums.has_key(k):
                    sums[k] = n + v
                    us[n+v] = lus[v]
                    ss[n+v] = k
                else:
                    us[sums[k]] = us[sums[k]] + lus[v]
        m = m * 10
    del us[0]
    for i,n in us.items():
        k = d[ss[i]]
        count[k] = count[k] + n
    return count[89]

print Compute(9)









# for i in range(1,10000000):
# 	print i
# 	j = i
# 	while j != 1 and j != 89:
# 		j = add_square_of_digits(j)
# 	if j == 89:
# 		bucket.append(i)

# print len(bucket)


print time() - s