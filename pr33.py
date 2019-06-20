f=str(input())
a=len(f)
l=[]
for i in range(0,a):
    l.append(f[i+1:])
print(sorted(l)[len(l)-1])
