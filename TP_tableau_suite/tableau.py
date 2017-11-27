def zero_consecutif(l):
	ltmp=[]
	ltmp2=[]
	i=0
	n=len(l)
	while(i<n):
		if(l[i]==0):
			ltmp.append(l[i])
		else:
			if(len(ltmp2)<len(ltmp)):
				ltmp2=ltmp
			ltmp=[]

		i+=1
	return ltmp2

print zero_consecutif([1,0,0,2,3,0,0,0,0,0,5,0,5,0,0,0])

def strict_croissant_consecutif(l):
	ltmp=[]
	ltmp2=[]
	i=0
	n=len(l)
	while(i<n):
		if(i<n-1 and l[i]<l[i+1] ):
			ltmp.append(l[i])
		else:
			ltmp.append(l[i])
			if(len(ltmp2)<len(ltmp)):
				ltmp2=ltmp
			ltmp=[]

		i+=1
	return ltmp2
	
print strict_croissant_consecutif([1,2,3,2,8,9,10,11,19,25,32,5,6,7,8,3])



def plus_grand_ecart(l):
	mini=l[0]
	maxi=l[0]
	i=1
	n=len(l)
	while(i<n):
		if (l[i]>maxi):
			maxi=l[i]
		if (l[i]<mini):
			mini=l[i]
		i+=1
	return maxi-mini

print plus_grand_ecart([9,8,7,5,8,9,2,4,22,16])

def del_consecutif(l):
	i=1
	while(i<len(l)):
		print l,i
		if(l[i]==l[i-1]):
			l.pop(i)
		else:
			i+=1
	return l

print del_consecutif([1,1,1,2,3,1,2,3,3,3,4,5,6,7])

def tri_list_etudiant(l):
	i=0
	pos_f=0
	pos_n=0
	n=len(l)
	while(i<n):
		if(l[i][1]=='n'):
			print l
			tmp=l[pos_n]
			l[pos_n]=l[i]
			l[i]=tmp
			pos_n+=1
		i+=1
	i=0
	pos_f=pos_n
	while(i<n):
		if(l[i][1]=='f'):
			print l
			tmp=l[pos_f]
			l[pos_f]=l[i]
			l[i]=tmp
			pos_f+=1
		i+=1
	return l

print tri_list_etudiant([['kevin','h'],['brenda','f'],['kevin','n'],['brenda','f']])

