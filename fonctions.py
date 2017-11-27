import math

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


def npremier_fibbo(n):
    l=[]
    i=0
    a=1
    b=1
    while (i<n):
        b+=a
        a=b-a
        if( not b%7):
            i+=1
            l.append(b)
    return l

l5=npremier_fibbo(5)
print l5

def diviseur(n):
    l=[]
    i=0
    m=n/2
    while (i<m) :
        i+=1
        if(not n%i):
            l.append(i)

    return l


l6=diviseur(28)
print l6

def premier(n):
    l=diviseur(n)	
    return len(l)==1

x=4
print x, "est premier?"
print premier(x)

def liste_premier(n):
    l=[]
    i=1
    while i<n :
        if premier(i):
            l.append(i)
            i+=1
    return l

x=100
print "liste de nb premier de 0 a", 100
print liste_premier(x)

#avance

def nparfait(n):
    i=1
    count=2
    l=[1]
    while i<n :
        j=0
        l2=diviseur(count)
        m=len(l2)
        x=0
        while j<m:
            x+=l2[j]
            j+=1
            if (x==count and count!=1):
                l.append(x)
                i+=1
            count+=1
    return l

x=5
print "liste des",x,"premier nb parfait"
print nparfait(x)


def liste_premier2 (n):
    l=[]
    i=0
    m=len(n)
    while (i<n):
        i+=1
    return l


def collatz(a):
    l=[a]
    i=1
    x=a;
    while(l[i-1]!=1):
        if(x%2):
            x=(x*3)+1
        else:
            x=x/2
        l.append[x]
        i+=1
    return l
print collatz(5)
