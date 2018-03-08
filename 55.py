from time import time
s = time()

def is_palindrome(n):
	 n = str(n)
	 if len(n) == 1:
	 	return True
	 if len(n) == 2:
	 	return n[0] == n[1]
	 if n[0] == n[-1]:
	 	return is_palindrome(n[1:-1])
	 else:
	 	return False


def add_reverse(n):
	n = str(n)
	rev_n = n[::-1]
	return int(n) + int(rev_n)

L_numbers = []


def is_Lychrel(n):
	n = add_reverse(n)
	i = 2
	while not is_palindrome(n) and i < 50:
		n = add_reverse(n)
		i += 1
	if i >= 50:
		return True
	else:
		return False

for k in range(1,10000):
	if is_Lychrel(k):
		L_numbers.append(k)


print len(L_numbers)
print time() - s