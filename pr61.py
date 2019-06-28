a=str(input())
b=str(input())
z="abcdefghijklmnopqrstuvwxyz"
for i in range(len(a)):
    l1=[]
    l2=[]
    l3=[]
    c=a[i]
    e=b[i]
    if(z.index(c)<=z.index(e) and c!="z" and e!="z"):
        d=z.index(e)
        l2=z[d:]
        l1=z[:d]
        l3=l2+l1
        print(l3[z.index(c)+1],end="")
    elif(z.index(c)>z.index(e) and c!="z" and e!="z"):
        d=z.index(c)
        l2=z[d:]
        l1=z[:d]
        l3=l2+l1
        print(l3[z.index(e)+1],end="")
    else:
        print(a[i],end="")
