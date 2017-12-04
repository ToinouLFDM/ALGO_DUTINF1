def fact(n):
	if n>0:
		return fact(n-1)*n
	else:
		return 1;
print fact(4)

def nk(n,k):
	if k>0:
		return  n*nk(n,k-1)
	else:
		return 1

print nk(2,3)

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

print nl(2,10)

def tab_is_pos(tab,i):
	if i<0:
		return True
	elif tab[i]>0:
		return tab_is_pos(tab,i-1)
	else:
		return False

tab=[1,2,3,4]
print tab_is_pos(tab,len(tab)-1)

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

print search_element(tab,5)

def recherche_dichotomique_recursive(element, tab):
 	m = len(tab)/2
 	if tab[m] == element :
		return m
	if tab[m] > element :
		return recherche_dichotomique_recursive(element, tab[1:m])
	else :
		return recherche_dichotomique_recursive(element, tab[m:-1])+m
	

tab=[1,2,3,4,5,6,7,8,9,20,22,45,68,98,105,125]
print recherche_dichotomique_recursive(45,tab)

def is_anagram(l1,l2):
	n=len(l2)
	if n==0
		return True
	elif
	


