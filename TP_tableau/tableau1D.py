def somme_list(l):
    i=0
    n=len(l)
    somme=0
    while(i<n):
        somme+=l[i]
        i+=1
    return somme

l=[2,4,8,8,8,8]
print somme_list(l)

def max_list(l):
    i=1
    n=len(l)
    maxi=l[0]
    while(i<n):
        maxi=l[i] if (maxi<l[i]) else maxi 
        i+=1
    return maxi

print max_list(l)

def indice_max(l):
    i=0
    n=len(l)
    maxi=0
    l2=[]
    while(i<n):
        if (maxi<l[i]):
            l2=[]
            maxi=l[i]
        if(l[i]==maxi):
            l2.append(i)
        i+=1
    return l2;

print indice_max(l);

def is_palindrome(l):
    i=0
    n=len(l)
    while(i<n and l[i]==l[n-i-1]):
        i+=1
    print i
    return i==n

l2="eluparcettecrapule"
print l2
print is_palindrome(l2)


def inversion(l):
    i=0
    n=len(l)
    while(i<(n/2)):
        a=l[i]
        l[i]=l[n-i-1]
        l[n-1-i]=a
        i+=1
    return(l)

l=[1,2,3,4,5]
print l
print inversion(l)



#def prefixe_commun


def sous_mot(l1,l2):
    i=0
    j=0
    ltmp=[]
    lmax=[0]
    n=len(l1);
    m=len(l2);
    a=j
    a=0
    while(j<n):
        while(i<m and j<n):
            if(l1[j]!=l2[i]):
                if(len(ltmp)>len(lmax)):
                    lmax=[]
                    lmax=ltmp
                ltmp=[]
                j-=a
                a=0
            if(l1[j]==l2[i]):
                ltmp.append(l1[j])
                print ltmp,i
                j+=1
                a+=1
            i+=1
        i=0
        j-=a
        a=0
        j+=1
    if(len(ltmp)>len(lmax)):
        lmax=[]
        lmax=ltmp
    return lmax

lchar1="yoyoazertsalutt"
lchar2="ayoyowfadwxvsalutt"

print sous_mot(lchar1,lchar2)



