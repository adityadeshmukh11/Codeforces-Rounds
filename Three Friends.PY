t= int(input())
l=[]
solution=[]
def abc(a,b,c):
    p=[]
    total=a+b+c
    mi=min(a,b,c)
    mx=max(a,b,c)
    md=total-mx-mi
    p.append(md+1)
    p.append(md)
    p.append(md-1)
    p.append(mi+1)
    p.append(mi)
    p.append(mi-1)
    p.append(mx+1)
    p.append(mx)
    p.append(mx-1)
    x=p[0]
    y=p[0]-min(abs(p[0]-p[3]),abs(p[0]-p[4]),abs(p[0]-p[5]))
    z=abs(p[0]-min(abs(p[0]+p[6]),abs(p[0]+p[7]),abs(p[0]+p[8])))
    final1=abs(x-y)+abs(y-z)+abs(z-x)
    x=p[1]
    y=p[1]-min(abs(p[1]-p[3]),abs(p[1]-p[4]),abs(p[1]-p[5]))
    z=abs(p[1]-min(abs(p[1]+p[6]),abs(p[1]+p[7]),abs(p[1]+p[8])))
    final2=abs(x-y)+abs(y-z)+abs(z-x) 
    x=p[2]
    y=p[2]-min(abs(p[2]-p[3]),abs(p[2]-p[4]),abs(p[2]-p[5]))
    z=abs(p[2]-min(abs(p[2]+p[6]),abs(p[2]+p[7]),abs(p[2]+p[8])))
    final3=abs(x-y)+abs(y-z)+abs(z-x)
    if(final1>final2):
        if(final3>final2):
            return(final2)
        else:
            return(final3)
    else:
        if(final3>final1):
            return(final1)
        else:
            return(final3)
for z in range(t):
    l=list(map(int, input().split()))
    a,b,c=l[0],l[1],l[2]
    final1,final2,final3=0,0,0
    solution.append(abc(a,b,c))
for i in range(len(solution)):
    print(solution[i])
    
