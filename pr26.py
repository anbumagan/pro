a=int(input())
b=list(map(int,input().split()))
c=1
max=0
for i in range(len(b)-1):
    if(b[i]<=b[i+1]):
        c=c+1
    elif(c>max):
        max=c
print(max)
