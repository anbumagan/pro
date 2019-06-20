from itertools import combinations
a,b=map(int,input().split())
l=list(map(int,input().split()))
c=[]
d=0
for i in range(1,a):
    d1=combinations(l,i)
    for j in list(d1):
        if(sum(j)==b):
            d=d+1
if(d>=1):
    print("yes")
else:
    print("no")
