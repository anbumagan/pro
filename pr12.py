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
    print(sum(l2))
