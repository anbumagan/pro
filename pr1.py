a=int(input())
l=[]
for i in range(0,a):
    c=str(input())
    l.append(c)
def compare(st1,st2):
    a1=len(st1)
    a2=len(st2)
    res=""
    i=0
    j=0
    while(i<=a1-1 and j<=a2-1):
        if(st1[i]==st2[j]):
            res=res+st1[i]
        i=i+1
        j=j+1
    return res
op=[]
for i in range(len(l)-1):
    op.append(compare(l[i],l[i+1]))
    i=i+1
print(*set(op))
