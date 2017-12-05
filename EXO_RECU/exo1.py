def fact(n):
	if n>0:
		return fact(n-1)*n
	else:
		return 1;
print (fact(4))
'''
def nk(n,k):
	if k>0:
		return  n*nk(n,k-1)
	else:
		return 1

print (nk(2,3))

def nl(n,k):
	if k==1:
		return n
	elif k>0:
		if k%2:
			return  nl(n,k/2)*nl(n,k/2)
		else:
			return nl(n,(k-1)/2)*nl(n,(k-1)/2)*n
	else:
		return 1

print (nl(2,10))

def tab_is_pos(tab,i):
	if i<0:
		return True
	elif tab[i]>0:
		return tab_is_pos(tab,i-1)
	else:
		return False

tab=[1,2,3,4]
print (tab_is_pos(tab,len(tab)-1))

def search_element_rec(tab,element,lenght):
	if lenght<0:
		return False
	elif (tab[lenght]==element):
		return True
	else: 
		return search_element_rec(tab,element,lenght-1)

def search_element(tab,element):
	n=len(tab)-1
	return search_element_rec(tab,element,n)

print (search_element(tab,5))

def recherche_dichotomique_recursive(element, tab):
 	m = len(tab)/2
 	if tab[m] == element :
 		return m
 	if tab[m] > element :
 		return recherche_dichotomique_recursive(element, tab[1:m])
 	else :
 		return recherche_dichotomique_recursive(element, tab[m:-1])+m
	

tab=[1,2,3,4,5,6,7,8,9,20,22,45,68,98,105,125]
print (recherche_dichotomique_recursive(45,tab))
'''
def is_anagram_rec(l1,i):
	print(i)
	n=len(l1)-1
	if(l1[i]!=l1[n-i]):
		return False
	elif(i==(int)(n/2)):
		return True
	else:
		return is_anagram_rec(l1,i+1)



def is_anagram(l1):
	n=len(l1)
	if(n==0):
		print("error this list is empty")
		return False
	else:
		return is_anagram_rec(l1,0)

l="salas"
print(is_anagram(l))
	
def inverse_rec(list,i):
	n=len(list)-1
	if(i==(int)(n/2)):
		return
	else:
		print(list[i],list[n-i])
		tmp=list[i]
		list[i]=list[n-i]
		list[n-i]=tmp
		inverse_rec(list,i+1)

def inverse(list):
	n=len(list)
	if(n==0):
		print("error this list is empty")
		return
	else:
		inverse_rec(list,0)


l=[1,2,3,4]
inverse(l)
print(l)

def is_prefix_rec(l1,l2):
	if(len(l2)==0 or len(l1)==0):
		return True
	elif(l2[0]!=l1[0]):
		return False
	else:
		return is_prefix_rec(l1[1:],l2[1:])

def is_prefix(l1,l2):
	n=len(l1)
	m=len(l2)
	res=False
	if (n>m):
		res=is_prefix_rec(l1,l2)
	else:
		res=is_prefix_rec(l2,l1)
	return res

l1="salut"
l2="sall"
print(is_prefix(l1,l2))



def fibo_rec(n,l):
	if(n<=2):
		return 1

	else:
		res=fibo_rec(n-1,l)+fibo_rec(n-2,l)
		if(res>l[len(l)-1]):
			l.append(res)
		return res
def fibo(n,l):
	l.append(1)
	l.append(1)
	if(n>=3):
		return fibo_rec(n,l)
l=[]

print(fibo(10,l))
print(l)






	


