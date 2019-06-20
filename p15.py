a=int(input())
l=list(map(int,input().split()))
l=[bin(i)[2:]for i in l]
l.sort()
l=l[::-1]
b=[int(i,2) for i in l]
for i in b:
    print(i)
