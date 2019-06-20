n=int(input())
l=list(map(int,input().split()))
l1=l[1:n:2]
l2=l[0:n:2]
if(sum(l1)>=sum(l2)):
    print(sum(l1))
else:
    print(sum(l2))
