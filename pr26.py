t1=int(input())
s=list(map(int,input().split()))

c=[]

n=1

for i in s:

  if i not in c:

    c.append(i)

for i in range(0,len(c)-1):

  if c[i]<c[i+1]:

    n+=1

print(n)
