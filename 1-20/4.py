the_list =  [ a*b for a in range(334,1000) for b in range(334,1000) if list(str(a*b))[0] == list(str(a*b))[5] and list(str(a*b))[1] == list(str(a*b))[4] and list(str(a*b))[2] == list(str(a*b))[3] ]

print max(the_list)