def matrice_pxq(p,q):
    l=[]
    i=0;
    j=0;
    while(j<p):
        l.append([])
        while(i<q):
            l[j].append(i+j*q)
            i+=1
        j+=1
        i=0
    return l

print matrice_pxq(3,4)
      
def moyenne_case(M,x,y):
    res=0
    a=x>0
    b=y>0
    c=x<len(M[0])-1
    d=y<len(M)-1
    count=0
    if(a):
        res+=M[x-1][y]
        count+=1
    if(b):
        res+=M[x][y-1]
        count+=1
    if(c):
        res+=M[x+1][y]
        count+=1
    if(d):
        res+=M[x][y+1]
        count+=1
    if(a and b):
        res+=M[x-1][y-1]
        count+=1
    if(a and d):
        res+=M[x-1][y+1]
        count+=1
    if(b and c):
        res+=M[x+1][y-1]
        count+=1
    if(c and d ):
        res+=M[x+1][y+1]
        count+=1
    return res/count

M=matrice_pxq(4,4)
print moyenne_case(M,0,0)

def matrice_moyenne(M):
    M_new=[]
    m=len(M)
    n=len(M[0])
    for j in range(m):
        M_new.append([])
        for i in range(n):
            M_new[j].append(moyenne_case(M,j,i))
    return M_new

print matrice_moyenne(M)

def max_ligne(M):
    n=len(M)
    res=M[0]
    i=1
    for i in range(n):
        if(len(res)<len(M[i])):
            res=M[i]

    return res

def mini_max(M):
    l=max_ligne(M)
    n=len(l)
    res=l[0]
    i=1
    for i in range(n):
        if(res<l[i]):
            res=l[i]
    return res

M=[[1,2,3,4],[1,4,6],[1,2,1,2,22]]
print M
print mini_max(M)


        
