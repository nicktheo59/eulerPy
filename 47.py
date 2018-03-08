def PrimeFactors(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist
 
list1 = map(PrimeFactors, range(1,1000000))
list2 = map(set,list1)

list3 = map(len,list2)

print list3

