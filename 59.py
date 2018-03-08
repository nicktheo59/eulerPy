from time import time
import operator as o
s = time()

def XOR(a,b):
	assert type(a) == int and type(b) == int
	return o.xor(a,b)

def char_encode(k):
	"""['a','b'] -> [97,98] """
	print k
	return map(ord,k)


def ascii_decode(k):
	assert type(k) is list
	return ''.join(map(chr,k))

def XOR_cyclically(cipher,password):
	assert type(cipher) is list
	i = 0
	password_length = len(password)
	password_encode = char_encode(password)
	encoded_res = []
	for d in cipher:
		encoded_res.append(XOR(d,password_encode[i % password_length]))
		i += 1
	res = encoded_res
	return ascii_decode(res)



charset = 'abcdefghijklmnopqrstuvwxyz'
password_options = [x + y + z for x in charset for y in charset for z in charset]

cipher1 = open('cipher1.txt','r')

cipher1_array = cipher1.read().split(',')
cipher1_array[-1] = '73'
cipher1_array = map(int,cipher1_array)

messages = []
for opt in password_options:
	result = XOR_cyclically(cipher1_array,map(str,opt))
	if 'and' in result and 'the' in result and 'everything' in result:
		messages.append(result)

print sum(char_encode(map(str,messages[0])))


print time() - s