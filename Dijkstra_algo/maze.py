import random
taille_x=41
taille_y=41

def init_maze(M,x,y):
    for i in range(y):
        M.append([])
        for j in range(x):
            M[i].append(0)
    return M

def print_maze(M):
    n=len(M)
    m=len(M[0])
    for i in range(n):
        print (M[i])
    print ('##################################################')

def print_nice_maze(M):
    print ('##################################################')
    n=len(M)
    m=len(M[0])
    for i in range(n):
        for j in range(m):
            if(M[i][j]==0):
                print ('X',end = "")
            else:
                print (' ',end = "")
        print ('')
    print ('##################################################')

def init_maze_case(M):
    n=len(M)
    m=len(M[0])
    print (n,m)
    count=1
    i=1
    j=1
    while(i<n-1 ):
        while(j<m-1):
            M[i][j]=count
            count+=1
            j+=2
        i+=2
        j=1    
    return M

M=[]
M=init_maze(M,11,11)
print_maze(M)
M=init_maze_case(M)
print_maze(M)

def set_path(M,x,y,from_x,from_y,tab):

    if(M[x][y]==0):
        return

    if(M[x+1][y]+M[x-1][y]+M[x][y+1]+M[x][y-1]==M[x][y]):
        return
    if(M[x+1][y]!=0 and x+1!=from_x and tab[x+1][y]!=1):
        M[x+1][y]=M[x][y]
        tab[x+1][y]=1
        print ('rec1',x+1,y)
        set_path(M,x+1,y,x,y,tab)
    if (M[x-1][y]!=0 and x-1!=from_x and tab[x-1][y]!=1):
        M[x-1][y]=M[x][y]
        print ('rec2',x-1,y)
        tab[x-1][y]=1
        set_path(M,x-1,y,x,y,tab)
    if (M[x][y+1]!=0 and y+1!=from_y and tab[x][y+1]!=1):
        M[x][y+1]=M[x][y]
        print ('rec3',x,y+1)
        tab[x][y+1]=1
        set_path(M,x,y+1,x,y,tab)
    if(M[x][y-1]!=0 and y-1!=from_y and tab[x][y-1]!=1):
        M[x][y-1]=M[x][y]
        print ('rec4',x,y-1)
        tab[x][y-1]=1
        set_path(M,x,y-1,x,y,tab)

def break_wall(Map,count_not_perfect):
    a=random.randint(1,taille_x-2)
    if(a%2==1):
        b=random.randint(1,(taille_y-3)/2)*2
    else:
        b=random.randint(0,(taille_y-3)/2)*2 +1
    print (a,b) 
    tab=[]
    init_maze(tab,taille_x,taille_y)
    if(Map[a][b]==0):
        if(count_not_perfect>(2)):
            if(Map[a+1][b]!=0):
                Map[a][b]=Map[a+1][b]
            elif(Map[a][b+1]!=0):
                Map[a][b]=Map[a][b+1]
            set_path(Map,a,b,0,0,tab)
            return -3
        else:
            print ('condition1->',Map[a+1][b],Map[a-1][b])
            print ('condition2->',Map[a][b+1],Map[a][b-1])
            if( Map[a+1][b]!=0 and Map[a+1][b]!=Map[a-1][b]):
                Map[a][b]=Map[a+1][b]
                
            elif( Map[a][b+1]!=0 and Map[a][b+1]!=Map[a][b-1]):
                Map[a][b]=Map[a][b+1]
            set_path(Map,a,b,0,0,tab)
            return 1
        
    
    return 0


def is_done(Map):
    a=Map[1][1]
    print (Map[1][1])
    for i in range(taille_y):
        for j in range(taille_x):
            if (Map[i][j]!=0 and Map[i][j]!=a):
                return False
    return True

def build_maze(Map):
    count_not_perfect=0
    init_maze(Map,taille_x,taille_y)
    init_maze_case(Map)
    count=0
    while(not is_done(Map)):
        print ('count->',count)
        print ('countnotperfect ->',count_not_perfect)
        count_not_perfect+=break_wall(Map,count_not_perfect)
        print_maze(Map)
        print_nice_maze(Map)
        count+=1

    print_maze(Map)
        
Map=[]
build_maze(Map)
print_nice_maze(Map)





