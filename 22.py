import re


file1 = open( '/Users/neil/Temporary/projecteuler22.txt' , 'r' )

#print file1.read()
list1 = re.findall( '"\w+"', file1.read() )
list2 = [ ]
for name in list1:
	list2 += [name[1:-1]]
	
list2.sort()

def NameScore(name):
	score = 0
	alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for letter in name:
		score += (alp.index(letter) + 1)
	return score

totalScore = 0 	
i = 1
for name in list2:
	totalScore += i*NameScore(name)
	i += 1
	
print totalScore
		
	






