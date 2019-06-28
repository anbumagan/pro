'''a=str(input())
b=len(a)
c=[]
for i in range(0,b):
    for j in range(i+1,b):
        c.append(a[i:j+1])
d=[]
for i in c:
    if(len(i)==len(set(i))):
        d.append(i)
d.sort(key=len)
d=d[::-1]
print(len(d[0]))'''


q=input()
l1=[]
l=len(q)
count=0
for i in range(l):
	if s[i] not in l1 and count==0:
		l1.append(s[i])
	else:
		count=1
print(len(lis1))

