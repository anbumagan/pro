a,b=map(str,input().split())
c=len(a)
d=len(b)
if(c==b):
    for i in range(c):
        if(a[i]!=b[i]):
            c=c+1
    print(c)
elif(c<d):
    d1=a.ljust(d,'0')
    c=0
    for i in range(d):
        if(d1[i]!=b[i]):
            c=c+1
    print(c)
else:
    d2=b.ljust(c,'0')
    c=0
    for i in range(c):
        if(d2[i]!=a[i]):
            c=c+1
    print(c)
