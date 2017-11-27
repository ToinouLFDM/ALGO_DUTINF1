def collatz(a):
    l=[a]
    i=1
    x=a
    while(l[i-1]!=1):
        if(x%2):
            x=(x*3)+1
        else:
            x=x/2
        l.append(x)
        i+=1
    return l

print collatz(3)
print collatz(5)
print collatz(7)
print collatz(25)
print collatz(51)

def prob_Syracuse(n):
    i=2
    while(i<n):
        i+=1
    return True

print prob_Syracuse(100)

def temps_vol(n):
    i=2
    dict1 ={}
    while(i<=n):
        dict1[i]=len(collatz(i))-1
        i+=1
    return dict1

print temps_vol(5)

def vol_max(n): 
    i=2
    x=0
    j=2
    while(i<=n):
        a=len(collatz(i))-1
        if(a>x):
            x=a
            j=i
        i+=1
    return (j,x)

print vol_max(10000)


def max_list(l):
    x=0;
    i=0;
    n=len(l)
    while(i<n):
        a=l[i]
        if(a>x):
            x=a
        i+=1
    return x

def alt_max(n):
    i =2
    x=0
    j=2
    while(i<=n):
        a=max_list(collatz(i))
        if(a>x):
            x=a
            j=i
        i+=1
    return (j,x)

print alt_max(10000)
