a1=int(input())
l=list(map(int,input().split()))
n=sum(l)
c=0
a=len(l)
for i in range(0,a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if(l[i]<l[j]<l[k] and i<j<k):
                c=c+1
print(c)
