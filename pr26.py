a1=int(input())
b=list(map(int,input().split()))
c=[]
max=0
for i in b:
    if(i not in c):
        c.append(i)
for i in range(len(c)-1):
    if(c[i]<c[i+1]):
        max=max+1
print(max)
