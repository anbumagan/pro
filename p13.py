a,b=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(b):
    c=list(map(int,input().split()))
    l1.append(c)
for i in l1:
    c=i[0]-1
    d=i[1]
    l2=l[c:d]
    xr=l2[0]
    for j in range(len(l2)-1):
        xr=xr^l2[j+1]
    print(xr)
