import copy
SS=[[7,2,3],[4,0,1],[5,6,8]]
FS=[[0, 2, 3], [7, 4, 1], [5, 6, 8]]
FF=SS.copy()


def find_position(z):
    for i in range(3):
        for j in range(3):
            if(z[i][j]==0):
                return i, j

def printn(m):
    for c in m:
        print(*c)
print(f"Starting Node---")
printn(SS)
print()

def left(n,i,j):
    change=[]
    change = copy.deepcopy(n)   
    if(i>=0 and i<=2 and j>0 and j<=2):
        t=change[i][j]
        change[i][j]=change[i][j-1]
        change[i][j-1]=t
        return change
    else:
        return n

def right(n,i,j):
    change=[]
    change = copy.deepcopy(n)   
    if(i>=0 and i<=2 and j>=0 and j<2):
        t=change[i][j]
        change[i][j]=change[i][j+1]
        change[i][j+1]=t
        return change
    else: 
        return n

def up(n,i,j):
    change=[]
    change = copy.deepcopy(n)   
    if(i>0 and i<=2 and j>=0 and j<=2):
        t=change[i][j]
        change[i][j]=change[i-1][j]
        change[i-1][j]=t
        return change
    else: 
        return n

def down(n,i,j):
    change=[]
    change = copy.deepcopy(n)   
    if(i>=0 and i<2 and j>=0 and j<=2):
        t=change[i][j]
        change[i][j]=change[i+1][j]
        change[i+1][j]=t
        return change
    else:
        return n
           
Q=[SS]
Q2=[SS]
level=1
while Q:
    top=Q.pop(0)
    i,j=find_position(top)
    l=left(top,i,j)
    r=right(top,i,j)
    u=up(top,i,j)
    d=down(top,i,j)
    print(f"--------------{level}--------------")
    if(l not in Q2):
        Q.append(l)
        Q2.append(l)
        print("left----")
        printn(l)
        print()
    if(r not in Q2):
        Q.append(r)
        Q2.append(r)
        print("Right----")
        printn(r)
        print()
    if(u not in Q2):
        Q.append(u)
        Q2.append(u)
        print("up----")
        printn(u)
        print()
    if(d not in Q2):
        Q.append(d)
        Q2.append(d)
        print("Down-----")
        printn(d)
        print()
    if(l==FS or d==FS or r==FS or u==FS):
        print(f"AT goal node level {level}")
        break
    level=level+1    


