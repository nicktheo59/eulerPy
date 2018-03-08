f = open('/Users/neil/Documents/Programs/Python/ProjectEuler/51/42/words.txt', 'r')

def isTriangle(word):
	assert type(word) is str
	triangle_numbers = [i*(i+1)/2 for i in range(1,50)]
	value_of = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(1,27)))
	total = 0
	for letter in word:
		total += value_of[letter]
	return total in triangle_numbers

word_array = f.read().split('","')

word_array[0] = 'A'
word_array[1785] = 'YOUTH'

triangle_words = [word for word in word_array if isTriangle(word)]

print len(triangle_words)







