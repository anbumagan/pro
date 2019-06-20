a1=int(input())
l1=[]
for i in range(0,a1):
    l=list(map(int,input().split()))
    for i in l:
        l1.append(i)
print(*sorted(l1))
