a=int(input())
b=list(map(int,input().split()))
c=1
ma=0
for i in range(len(b)-1):
    if(b[i]<=b[i+1]):
        c=c+1
    elif(c>ma):
        ma=c
print(ma)
