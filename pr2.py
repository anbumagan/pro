from itertools import combinations
a1,b1=input().split()
a=str(a1)
b=int(b1)
e=[]
d=combinations(a,len(a)-b)
for i in list(d):
    e.append("".join(i))
print(min(e))
