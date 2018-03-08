
def f((a,b,c,d,e,f,g,h)):
	return (a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h)
	
print [ (a,b,c,d,e,f,g,h) for a in range(201) for b in range(101) for c in range(41) 
					for d in range(21) for e in range(11) for f in range(5) 
					for g in range(3) for h in range(2) ]
					
