a1=str(input())
a1.lower()
a1.replace(" ","")
b="abcdefghijklmnopqrstuvwxyz"
b=list(b)
l=[]
for i in range(len(a1)):
    if(a1[i] in b and a1[i] not in l):
        l.append(a1[i])
if(len(l)==26):
    print("yes")
else:
    print("no")
