def liste_pair(l):
	n=len(l)
	l1=[]
	for i in range(n) :
		if  not (l[i]%2) :
			l1.append(l[i])
	return l1
	
l1=[1,4,8,16,32,522,24,31,47,89,95,64,21,33]
l2=liste_pair(l1)
print l2
		
		
#verifie si tout les entiers de la liste sont pairs	
def is_pair(l):
	n=len(l)
	i=0
	while (i<n) and not (l[i]%2):
		i=i+1
	if i>=n :
		i=i-1
		
	
	return not (l[i]%2)
	
l3=[2,4,6]
l4=[1,2,3,5]
print is_pair(l3)
print is_pair(l4)
	
	
def 7premier_fibbo(n):
	l=[]
	i=0
	a=1
	b=1
	while (i<n):
		l.append(a+b)
		a=b
		b=l[i]
	
	
	
	
	

