def is_croissant(l):
    i=0
    n=len(l)
    while(i<(n-1) and l[i+1]>l[i]):
        i+=1
    return i==n-1

l=[1,2,3,4,5]
l2=[1,5,2,6,7]
print is_croissant(l)
print is_croissant(l2)

def fusion_croissant(l1,l2):
    l=[]
    i=0
    j=0
    ltmp=[]
    if (max(len(l1),len(l2)==len(l2))):
        ltmp=l1
        l1=l2
        l2=ltmp

    n=len(l1)
    m=len(l2)
    while(i<n or j<m):
        if(i<n and (j>=m or l1[i]<=l2[j])):
            l.append(l1[i])
            i+=1
        if(j<m and (i>=n or l2[j]<=l1[i])):
            l.append(l2[j])
            j+=1
    return l

l1=[1,5,5,6,9,20]
l2=[2,3,4,6,8,16,20,23]
print fusion_croissant(l1,l2)
