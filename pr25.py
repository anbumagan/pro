n=int(input())
l=list(map(int,input().split()))
v=1
max=1
for i in range(1,n):
    if(l[i]>l[i-1]):
        v=v+1
    else:
        if(max<v):
            max=v
        v=1
if(max<v):
    max=v
print(max)
