a1=int(input())
l=list(map(int,input().split()))
n=sum(l)
c=0
a=a1//l[0]
for i in range(0,a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            if(l[i]*l[j]*l[k]==n):
                c=c+1
print(c)
