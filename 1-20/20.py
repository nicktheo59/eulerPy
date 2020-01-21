def factorial(n):
    f = 1
    while (n > 0):
        f = f * n
        n = n - 1
    return f
    
number = factorial(100)

list1 = list(str(number))

list2 = [ ]

for num in list1:
	list2.append(int(num))
	
print sum(list2)
